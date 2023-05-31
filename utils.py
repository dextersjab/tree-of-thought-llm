import argparse
from typing import Callable
from tasks.base import Task
from tasks.game24 import Game24Task
from tasks.creativewriting import CreativeWritingTask


def generate_log_file_name(args: argparse.Namespace) -> str:
    if args.naive_run:
        file_name = f'logs/{args.task_name}/{args.backend}_{args.temperature}_naive_{args.prompt_sample}_sample_{args.n_generate_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
    else:
        file_name = f'logs/{args.task_name}/{args.backend}_{args.temperature}_{args.method_generate}{args.n_generate_sample}_{args.method_evaluate}{args.n_evaluate_sample}_{args.method_select}{args.n_select_sample}_start{args.task_start_index}_end{args.task_end_index}.json'
    return file_name


def get_value(task: Game24Task, x: str, y: str, gpt: Callable, n_evaluate_sample: int, cache_value: bool = True) -> float:
    value_prompt = task.value_prompt_wrap(x, y)
    if cache_value and value_prompt in task.value_cache:
        return task.value_cache[value_prompt]
    value_outputs = gpt(value_prompt, n=n_evaluate_sample, stop=None)
    value = task.value_outputs_unwrap(x, y, value_outputs)
    if cache_value:
        task.value_cache[value_prompt] = value
    return value


def get_values(task: Game24Task, x: str, ys: list, gpt: Callable, n_evaluate_sample: int, cache_value: bool = True) -> list:
    values = []
    local_value_cache = {}
    for y in ys:  # each partial output
        if y in local_value_cache:  # avoid duplicate candidates
            value = 0
        else:
            value = get_value(task, x, y, gpt, n_evaluate_sample, cache_value=cache_value)
            local_value_cache[y] = value
        values.append(value)
    return values


def get_votes(task: CreativeWritingTask, x: str, ys: list, gpt: Callable, n_evaluate_sample: int) -> list:
    vote_prompt = task.vote_prompt_wrap(x, ys)
    vote_outputs = gpt(vote_prompt, n=n_evaluate_sample, stop=None)
    values = task.vote_outputs_unwrap(vote_outputs, len(ys))
    return values


def get_proposals(task: Task, x: str, y: str, gpt: Callable) -> list:
    propose_prompt = task.propose_prompt_wrap(x, y)
    proposals = gpt(propose_prompt, n=1, stop=None)[0].split('\n')
    return [y + _ + '\n' for _ in proposals]


def get_samples(task: Task, x: str, y: str, gpt: Callable, n_generate_sample: int, prompt_sample: str, stop: str | None) -> list:
    if prompt_sample == 'standard':
        prompt = task.standard_prompt_wrap(x, y)
    elif prompt_sample == 'cot':
        prompt = task.cot_prompt_wrap(x, y)
    else:
        raise ValueError(f'prompt_sample {prompt_sample} not recognized')
    samples = gpt(prompt, n=n_generate_sample, stop=stop)
    return [y + _ for _ in samples]
