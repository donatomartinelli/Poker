# Poker Hand Simulator hands.py

This Python script simulates the generation and evaluation of poker hands. It is designed to create a deck of cards, deal a specified number of hands, sort the hands, and rank each hand according to standard poker rules. Finally, it displays the results with the hands ranked and sorted.

## Features

- **Deck Creation**: A deck of 52 cards is generated with 4 suits (Hearts, Diamonds, Clubs, Spades) and 13 values (2-10, J, Q, K, A). The deck is shuffled randomly.
  
- **Hand Dealing**: Hands are created by dealing a specified number of cards (default is 5) from the deck.

- **Hand Evaluation**: Each hand is evaluated and ranked according to the following poker combinations:
  - Royal Flush
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pair
  - One Pair
  - High Card

- **Hand Sorting**: The hands are sorted from highest to lowest based on their ranking.

- **Result Display**: The hands are printed in a readable format, showing both the cards and the ranking obtained.

## Usage

1. **Hand Generation**: The script can generate and evaluate a specified number of hands. This number can be set using the `n` variable (default: 4).

2. **Script Execution**: When the script is executed, it deals the hands, evaluates them, and then prints the result for each hand.

3. **Output**: For each generated hand, the script prints:
   - The cards in the hand.
   - The type of poker hand (e.g., Full House).
   - The numerical values of the cards in the hand.

