import argparse
import itertools
from typing import Callable

import numpy as np

from tasks.base import Task
from tasks.game24 import Game24Task
from tasks.creativewriting import CreativeWritingTask
from utils import get_samples, get_proposals, get_votes, get_values


# 1. Decompose the intermediate process into thought steps
def decompose_into_steps(args: argparse.Namespace, task: Game24Task | CreativeWritingTask, idx: int, gpt: Callable, to_print: bool = True) -> tuple:
    x = task.get_input(idx)  # input
    ys = ['']  # current output candidates
    infos = []
    for step in range(task.steps):
        # 2. Generate potential thoughts from each state
        new_ys = generate_potential_thoughts(args, task, x, ys, step, gpt)
        ids = list(range(len(new_ys)))
        # 3. Heuristically evaluate states
        values = evaluate_states(args, task, x, new_ys, gpt)
        # 4. What search algorithm to use?
        ys = select_best_thoughts(args, ids, values, new_ys)
        infos.append({'step': step, 'x': x, 'ys': ys, 'new_ys': new_ys, 'values': values, 'select_new_ys': ys})
    return ys, {'steps': infos}


# 2. Generate potential thoughts from each state
def generate_potential_thoughts(args: argparse.Namespace, task: Task, x: str, ys: list, step: int, gpt: Callable) -> list:
    new_ys = []
    if args.method_generate == 'sample':
        new_ys = [get_samples(task, x, y, gpt, args.n_generate_sample, prompt_sample=args.prompt_sample, stop=task.stops[step]) for y in ys]
    elif args.method_generate == 'propose':
        new_ys = [get_proposals(task, x, y, gpt) for y in ys]
    new_ys = list(itertools.chain(*new_ys))
    return new_ys


# 3. Heuristically evaluate states
def evaluate_states(args: argparse.Namespace, task: Game24Task | CreativeWritingTask, x: str, new_ys: list, gpt: Callable) -> list:
    values = []
    if args.method_evaluate == 'vote':
        values = get_votes(task, x, new_ys, gpt, args.n_evaluate_sample)
    elif args.method_evaluate == 'value':  # only applies to game24
        values = get_values(task, x, new_ys, gpt, args.n_evaluate_sample)
    return values


# 4. Decide which search algorithm to use
def select_best_thoughts(args: argparse.Namespace, ids: list, values: list, new_ys: list) -> list:
    select_ids = []
    if args.method_select == 'sample':
        ps = np.array(values) / sum(values)
        select_ids = np.random.choice(ids, size=args.n_select_sample, p=ps).tolist()
    elif args.method_select == 'greedy':
        select_ids = sorted(ids, key=lambda x: values[x], reverse=True)[:args.n_select_sample]
    select_new_ys = [new_ys[select_id] for select_id in select_ids]
    return select_new_ys
