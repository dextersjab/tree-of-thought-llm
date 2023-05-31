import argparse
import json
import logging
import os

from models import gpt_usage, get_gpt_func
from naive_solve import naive_solve
from tasks import get_complex_task
from tree_of_thoughts import decompose_into_steps
from utils import generate_log_file_name

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# The main function that reads arguments, selects the model and runs the tasks
def run(args: argparse.Namespace) -> None:
    # Retrieve the complex task to be decomposed
    task = get_complex_task(args.task_name, args.task_data_file)
    logs, average_accuracy, successful_solutions_count = [], 0, 0
    gpt = get_gpt_func(model=args.backend, temperature=args.temperature)

    # Generate the log file name and create the directory if it doesn't exist
    log_file_name = generate_log_file_name(args)
    os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

    # Loop through the tasks and attempt to solve them
    for task_index in range(args.task_start_index, args.task_end_index):
        # Solve the task either (1) decomposing it into steps using ToT or by (2) naively using IO or CoT
        if not args.naive_run:
            solutions, task_info = decompose_into_steps(args, task, task_index, gpt)
        else:
            solutions, task_info = naive_solve(args, task, task_index, gpt)

        # Test the solutions and log the results
        test_results = [task.test_output(task_index, solution) for solution in solutions]
        task_info.update({'idx': task_index, 'ys': solutions, 'infos': test_results, 'usage_so_far': gpt_usage(args.backend)})
        logs.append(task_info)
        with open(log_file_name, 'w') as f:
            json.dump(logs, f, indent=4)

        # Calculate the accuracy of the solutions
        accuracies = [info['r'] for info in test_results]
        average_accuracy += sum(accuracies) / len(accuracies)
        successful_solutions_count += any(accuracies)

        # Log the results for this task
        logging.info('Task index: %s, Sum of accuracies: %s, Average accuracy: %s, Successful solutions count: %s',
                     task_index, sum(accuracies), average_accuracy, successful_solutions_count)

    # Calculate the total number of tasks
    total_tasks = args.task_end_index - args.task_start_index

    # Log the final results
    logging.info('Final average accuracy: %s, Final successful solutions count: %s',
                 average_accuracy / total_tasks, successful_solutions_count / total_tasks)
    logging.info('Final usage so far: %s', gpt_usage(args.backend))


def parse_args() -> argparse.Namespace:
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, choices=['gpt-4', 'gpt-3.5-turbo'], default='gpt-4')
    args.add_argument('--temperature', type=float, default=0.7)

    args.add_argument('--task_name', type=str, required=True, choices=['game24', 'creativewriting', 'crosswords'])
    args.add_argument('--task_data_file', type=str, required=True)
    args.add_argument('--task_start_index', type=int, default=900)
    args.add_argument('--task_end_index', type=int, default=1000)

    args.add_argument('--naive_run', action='store_true')
    args.add_argument('--prompt_sample', type=str, choices=['standard', 'cot'])  # only used when method_generate = sample, or naive_run

    args.add_argument('--method_generate', type=str, choices=['sample', 'propose'])
    args.add_argument('--method_evaluate', type=str, choices=['value', 'vote'])
    args.add_argument('--method_select', type=str, choices=['sample', 'greedy'])
    args.add_argument('--n_generate_sample', type=int, default=1)  # only thing needed if naive_run
    args.add_argument('--n_evaluate_sample', type=int, default=1)
    args.add_argument('--n_select_sample', type=int, default=1)

    args = args.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print(args)
    run(args)
