# Crosswords Data Structure

The crosswords data is stored in a JSON file with a specific structure designed
for efficient processing. Here's a breakdown of the structure:

The entire file contains a list of crossword puzzles. Each crossword puzzle is
represented as a list with two elements:

1. **Clues**: This is a list of 10 strings, each representing a clue for a word
   in the crossword puzzle. The first 5 clues correspond to the horizontal
   words (from top to bottom), and the last 5 clues correspond to the vertical
   words (from left to right).

2. **Grid**: This is a list of 25 characters, representing a 5x5 crossword grid.
   The characters are listed in row-major order, meaning that the first 5
   characters correspond to the first row (top), the next 5 characters
   correspond to the second row, and so on.

Here's an example of the crossword puzzle:

| Clue | Horizontal Word | Vertical Word |
|------|-----------------|---------------|
| An agendum; something to be done | A G E N D | M O T A R |
| An engine | M O T O R | A R T S Y |
| Pretentious; flowery | A R T S Y | S A L L E |
| A salon; a hall | S A L L E | L E E R |

And here's the first puzzle in its JSON format:

```json
[
    [
        [
            "An agendum; something to be done",
            "An engine",
            "Pretentious; flowery",
            "A salon; a hall",
            "To mock; to sneer",
            "To heap",
            "An Indian antelope",
            "To intend; to plan; to devise; a nettle; to guess",
            "A nozzle",
            "Desiccator; more dry"
        ],
        [
            "A",
            "G",
            "E",
            "N",
            "D",
            "M",
            "O",
            "T",
            "O",
            "R",
            "A",
            "R",
            "T",
            "S",
            "Y",
            "S",
            "A",
            "L",
            "L",
            "E",
            "S",
            "L",
            "E",
            "E",
            "R"
        ]
    ]
]
