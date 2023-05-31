import argparse
from typing import Callable

from tasks.base import Task
from utils import get_samples


def naive_solve(args: argparse.Namespace, task: Task, task_instance: str, gpt: Callable, to_print: bool = True) -> tuple:
    x = task_instance  # input
    ys = get_samples(task, x, '', gpt, args.n_generate_sample, args.prompt_sample, stop=None)
    return ys, {}
