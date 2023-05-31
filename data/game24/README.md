# 24 Game data

This data is related to the "24 Game" task in the Tree of Thoughts paper. In
this task, an AI model is given four numbers and it has to find a way to use
basic arithmetic operations (addition, subtraction, multiplication, and
division) to make the numbers equal 24.

The table below provides statistics about the performance of the AI model on
different puzzles in the 24 Game task.

| Rank | Puzzles | Average solve time (s) | Solve success rate | Mean solve time within 1-sigma STD | STD solve time within 1-sigma STD (s) |
|------|---------|------------------------|--------------------|------------------------------------|---------------------------------------|
| 1    | 1 1 4 6 | 4.4                    | 99.20%             | 4.67                               | 1.48                                  |
| 2    | 1 1 11 11 | 4.41                 | 99.60%             | 4.68                               | 1.45                                  |
| 3    | 1 1 3 8 | 4.45                   | 99.20%             | 4.69                               | 1.48                                  |
| 4    | 1 1 1 8 | 4.48                   | 98.80%             | 4.66                               | 1.25                                  |
| 5    | 6 6 6 6 | 4.59                   | 99.40%             | 4.82                               | 1.49                                  |
| 6    | 1 1 2 12 | 4.63                  | 99.10%             | 4.95                               | 1.57                                  |

## Columns

- **Rank**: The rank of the puzzle based on the average solve time.
- **Puzzles**: The four numbers given to the AI model to solve the 24 Game.
- **Average solve time (s)**: The average time taken by the AI model to solve
  the puzzle.
- **Solve success rate**: The percentage of times the AI model was able to
  successfully solve the puzzle.
- **Mean solve time within 1-sigma STD**: The average solve time within one
  standard deviation (STD) of the mean solve time.
- **STD solve time within 1-sigma STD (s)**: The standard deviation of the solve
  time within one standard deviation of the mean solve time.

These statistics provide insights into the AI model's performance and efficiency
in solving the 24 Game puzzles.
