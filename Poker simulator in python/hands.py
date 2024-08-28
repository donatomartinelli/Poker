import random
from collections import Counter

# Creare un mazzo di carte
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

# Convertire il valore di una carta in un numero
def card_value(card):
    value, _ = card
    if value.isdigit():
        return int(value)
    elif value == 'J':
        return 11
    elif value == 'Q':
        return 12
    elif value == 'K':
        return 13
    elif value == 'A':
        return 14

# Creare una mano di carte
def create_hand(deck, hand_size=5):
    hand = deck[:hand_size]
    del deck[:hand_size]
    return hand

# Ordinare le mani
def sort_hands(hands):
    return [sorted(hand, key=card_value, reverse=True) for hand in hands]

# Identificare il rango di una mano di poker
def get_hand_rank(hand):
    values = [card_value(card) for card in hand]
    suits = [card[1] for card in hand]
    
    value_counts = Counter(values)
    sorted_values = sorted(value_counts.keys(), reverse=True)
    
    is_flush = len(set(suits)) == 1
    is_straight = len(sorted_values) == 5 and (sorted_values[0] - sorted_values[-1] == 4)
    is_royal = sorted_values == [14, 13, 12, 11, 10]
    
    if is_straight and is_flush and is_royal:
        return (10, sorted_values)  # Royal Flush
    elif is_straight and is_flush:
        return (9, sorted_values)   # Straight Flush
    elif 4 in value_counts.values():
        four_kind_value = max(value_counts, key=lambda x: value_counts[x])
        kicker = [v for v in value_counts if value_counts[v] != 4][0]
        return (8, [four_kind_value] * 4 + [kicker])  # Four of a Kind
    elif 3 in value_counts.values() and 2 in value_counts.values():
        three_kind_value = max(value_counts, key=lambda x: value_counts[x] if value_counts[x] == 3 else 0)
        pair_value = max(value_counts, key=lambda x: value_counts[x] if value_counts[x] == 2 else 0)
        return (7, [three_kind_value] * 3 + [pair_value] * 2)  # Full House
    elif is_flush:
        return (6, sorted_values)   # Flush
    elif is_straight:
        return (5, sorted_values)   # Straight
    elif 3 in value_counts.values():
        three_kind_value = max(value_counts, key=lambda x: value_counts[x])
        kickers = sorted([v for v in value_counts if value_counts[v] < 3], reverse=True)
        return (4, [three_kind_value] * 3 + kickers)  # Three of a Kind
    elif list(value_counts.values()).count(2) == 2:
        pairs = sorted([k for k, v in value_counts.items() if v == 2], reverse=True)
        kicker = [k for k, v in value_counts.items() if v == 1][0]
        return (3, pairs * 2 + [kicker])  # Two Pair
    elif 2 in value_counts.values():
        pair_value = max(value_counts, key=lambda x: value_counts[x] if value_counts[x] == 2 else 0)
        kickers = sorted([k for k, v in value_counts.items() if v == 1], reverse=True)
        return (2, [pair_value] * 2 + kickers)  # One Pair
    else:
        return (1, sorted_values)   # High Card

# Generare e valutare n mani
def generate_and_evaluate_hands(n):
    deck = create_deck()
    hands = [create_hand(deck) for _ in range(n)]
    sorted_hands = sort_hands(hands)
    evaluated_hands = [(hand, get_hand_rank(hand)) for hand in sorted_hands]
    evaluated_hands.sort(key=lambda x: x[1], reverse=True)
    return evaluated_hands

# Esempio d'uso
n = 4  # Numero di mani da generare
evaluated_hands = generate_and_evaluate_hands(n)

# Visualizzare le mani ordinate
for i, (hand, rank) in enumerate(evaluated_hands):
    hand_str = ' '.join([f"{value} {suit}," for value, suit in hand])
    
    rank_name = {
        10: "Royal Flush",
        9: "Straight Flush",
        8: "Four of a Kind",
        7: "Full House",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pair",
        2: "One Pair",
        1: "High Card"
    }[rank[0]]
    
    # Associare i valori ordinati alle carte della mano
    value_str = ', '.join([f"{card_value(card)}" for card in hand])
    
    print(f"Mano {i+1}: {hand_str}\nClassifica: {rank_name} con valori [{value_str}]\n\n")
