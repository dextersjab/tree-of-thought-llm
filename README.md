# Tree of Thoughts (ToT) Rewrite

A rewrite for Tree of Thoughts to make it (subjectively) easier to read and 
navigate the code.

This code is the implementation and results for the popular paper
[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)
.

Original
repository: [https://github.com/ysymyth/tree-of-thought-llm](https://github.com/ysymyth/tree-of-thought-llm)
.

## Introduction

In the experiment, Tree of Thoughts is applied to 3 `complex_tasks`:

1. [Game of 24](data/game24/README.md)
2. [Creative writing](data/creativewriting/README.md)
3. [Mini crosswords](data/crosswords/README.md)

I restructured the main functions of the code to reflect 4 questions posed
in the paper. You can find them in `tree_of_thoughts.py`:

| Function                  | "Question"                                       | Description                                                                                                                                                                                                 |
|---------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| decompose_into_steps      | How to decompose the intermediate process into thought steps | This function is responsible for breaking down the problem-solving process into smaller, manageable steps, known as "thoughts". |
| generate_potential_thoughts | How to generate potential thoughts from each state | This function generates potential thoughts or solutions for each step in the problem-solving process. It can use different strategies to generate these thoughts, such as sampling i.i.d. thoughts or proposing thoughts sequentially. |
| evaluate_states           | How to heuristically evaluate states           | This function evaluates the progress made towards solving the problem for each state in the problem-solving process. It serves as a heuristic for the search algorithm to determine which states to keep exploring and in which order. |
| select_best_thoughts      | What search algorithm to use                   | This function determines the search algorithm to use in the problem-solving process. It could be a breadth-first search (BFS), depth-first search (DFS), or other advanced search algorithms. |

## Get started

1. Set your OpenAI API key as the environment variable `OPENAI_API_KEY`.
2. run `pip install -r requirements.txt`

### Running the experiments

The "cheaper run options" below use the `naive_run` strategy and GPT-3.5 to allow
you to experiment with running the tests without incurring major costs.
The naive run uses Input-Output aka single (zero-shot) prompting.

The default runs use breadth-first search and depth-first search tree-of-thought
combined with GPT-4, so will significantly more costs.

#### Game of 24

**Default**:
```shell
./scripts/game24/bfs.sh
```

**Cheaper run option**:
```shell
./scripts/game24/bfs.sh --backend gpt-3.5-turbo --naive_run --prompt_sample standard
```

#### Creative writing

**Default**:
```shell
./scripts/creativewriting/bfs.sh
```

**Cheaper run option**:
```shell
./scripts/creativewriting/bfs.sh --backend gpt-3.5-turbo --naive_run
```

#### Crosswords

**Default**:
```shell
./scripts/crosswords/standard_sampling.sh 
```

**Default**:
```shell
./scripts/crosswords/standard_sampling.sh --backend gpt-3.5-turbo --naive_run 
```

## Experiments

Run experiments
via ``sh scripts/{game24, text, crosswords}/{standard_sampling, cot_sampling, bfs}.sh``
, except in crosswords we use a DFS algorithm for ToT, which can be run
via ``scripts/crosswords/search_crosswords-dfs.ipynb``.

The very simple ``run.py`` implements the ToT + BFS algorithm, as well as the
naive IO/CoT sampling. Some key arguments:

- ``--naive_run``: if True, run naive IO/CoT sampling instead of ToT + BFS.
- ``--prompt_sample`` (choices=[``standard``, ``cot``]): sampling prompt
- ``--method_generate`` (choices=[``sample``, ``propose``]): thought generator,
  whether to sample independent thoughts (used in Creative Writing) or propose
  sequential thoughts (used in Game of 24)
- ``--method_evaluate`` (choices=[``value``, ``vote``]): state evaluator,
  whether to use the value states independently (used in Game of 24) or vote on
  states together (used in Creative Writing)
- ``--n_generate_sample``: number of times to prompt for thought generation
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--n_select_sample``: number of states to keep from each step (i.e. ``b`` in
  the paper's ToT + BFS algorithm)

## Original results (trajectories)

``logs/`` contains all the trajectories from the paper's experiments, except
for ``logs/game24/gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json``
which was reproduced after the paper (as the original experiment was done in a
notebook) and achieved a 69\% score instead of the original 74\% score due to
randomness in GPT decoding. We hope to aggregate multiple runs in the future to
account for sampling randomness and update the paper, but this shouldn't affect
the main conclusions of the paper.

