import random
from collections import Counter

# Definizione delle carte e dei semi
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Costruzione del mazzo
deck = [(rank, suit) for suit in suits for rank in ranks]

# Funzione per mescolare il mazzo
def shuffle_deck(deck):
    random.shuffle(deck)

# Funzione per distribuire le carte ai giocatori
def deal_cards(deck, num_players):
    hands = []
    for _ in range(num_players):
        hand = [deck.pop(), deck.pop()]
        hands.append(hand)
    return hands

# Funzione per il flop, turn e river
def deal_community_cards(deck, stage):
    if stage == 'flop':
        return [deck.pop(), deck.pop(), deck.pop()]
    elif stage == 'turn' or stage == 'river':
        return [deck.pop()]

# Funzione per valutare una mano (semplificata)
def evaluate_hand(hand, community_cards):
    all_cards = hand + community_cards
    all_ranks = [card[0] for card in all_cards]
    rank_count = Counter(all_ranks)
    
    # Check for pairs, three of a kind, etc.
    if 4 in rank_count.values():
        return "Four of a Kind"
    elif 3 in rank_count.values() and 2 in rank_count.values():
        return "Full House"
    elif 3 in rank_count.values():
        return "Three of a Kind"
    elif list(rank_count.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_count.values():
        return "One Pair"
    else:
        return "High Card"

# Simulazione di una partita semplice
def simulate_game(num_players):
    shuffle_deck(deck)
    
    hands = deal_cards(deck, num_players)
    print("Hands dealt:")
    for i, hand in enumerate(hands):
        print(f"Player {i+1}: {hand}")
    
    community_cards = []
    community_cards += deal_community_cards(deck, 'flop')
    print("\nFlop:", community_cards)
    
    community_cards += deal_community_cards(deck, 'turn')
    print("Turn:", community_cards)
    
    community_cards += deal_community_cards(deck, 'river')
    print("River:", community_cards)
    
    print("\nFinal hands evaluation:")
    for i, hand in enumerate(hands):
        result = evaluate_hand(hand, community_cards)
        print(f"Player {i+1}: {result}")

# Simulazione di una partita con 3 giocatori
simulate_game(3)
