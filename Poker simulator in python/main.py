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

# Funzione per simulare le azioni degli avversari
def ai_action(player, hand, community_cards, current_bet, pot, player_money):
    # Una logica semplice per l'AI:
    strength = evaluate_hand(hand, community_cards)
    if strength in ["Four of a Kind", "Full House"]:
        # Mani molto forti, l'AI punta aggressivamente
        action = "raise"
        bet = min(current_bet + random.randint(10, 50), player_money[player])
        player_money[player] -= bet
        pot += bet
    elif strength in ["Three of a Kind", "Two Pair"]:
        # Mani decenti, l'AI può vedere o rilanciare moderatamente
        action = random.choice(["call", "raise"])
        if action == "call":
            bet = current_bet
        else:
            bet = min(current_bet + random.randint(5, 20), player_money[player])
        player_money[player] -= bet
        pot += bet
    else:
        # Mani deboli, l'AI potrebbe foldare o vedere
        action = random.choice(["fold", "call"])
        if action == "call":
            bet = current_bet
            player_money[player] -= bet
            pot += bet
        else:
            bet = 0
    return action, bet, pot

# Funzione per la gestione del gioco
def simulate_game(num_players, initial_money=1000):
    player_money = [initial_money] * num_players
    shuffle_deck(deck)
    
    hands = deal_cards(deck, num_players)
    community_cards = []
    pot = 0
    current_bet = 0
    small_blind = 10
    big_blind = 20

    print(f"\n--- New Game ---\nYou have ${player_money[0]}")
    print(f"Your hand: {hands[0]}")

    # Blinds
    player_money[1] -= small_blind
    player_money[2] -= big_blind
    pot += small_blind + big_blind
    current_bet = big_blind

    # Round of betting pre-flop
    for player in range(num_players):
        if player == 0:
            print(f"\nCurrent pot: ${pot}")
            print(f"Your hand: {hands[0]}")
            action = input(f"Your turn! [fold, call {current_bet}, raise]: ").lower()
            if action == "fold":
                print("You folded!")
                return
            elif action == "call":
                player_money[0] -= current_bet
                pot += current_bet
            elif action == "raise":
                raise_amount = int(input("Enter raise amount: "))
                current_bet += raise_amount
                player_money[0] -= current_bet
                pot += current_bet
        else:
            action, bet, pot = ai_action(player, hands[player], community_cards, current_bet, pot, player_money)
            if action == "fold":
                print(f"Player {player + 1} folded.")
                hands[player] = None
            else:
                print(f"Player {player + 1} {action}ed ${bet}.")
    
    print(f"\nPot after betting: ${pot}")

    # Flop
    community_cards += deal_community_cards(deck, 'flop')
    print(f"\nFlop: {community_cards}")

    # Round of betting on the flop
    for player in range(num_players):
        if hands[player]:
            if player == 0:
                print(f"\nCurrent pot: ${pot}")
                print(f"Your hand: {hands[0]}")
                print(f"Community cards: {community_cards}")
                action = input(f"Your turn! [fold, check, raise]: ").lower()
                if action == "fold":
                    print("You folded!")
                    return
                elif action == "raise":
                    raise_amount = int(input("Enter raise amount: "))
                    current_bet = raise_amount
                    player_money[0] -= raise_amount
                    pot += raise_amount
            else:
                action, bet, pot = ai_action(player, hands[player], community_cards, current_bet, pot, player_money)
                if action == "fold":
                    print(f"Player {player + 1} folded.")
                    hands[player] = None
                else:
                    print(f"Player {player + 1} {action}ed ${bet}.")
    
    print(f"\nPot after betting: ${pot}")

    # Turn
    community_cards += deal_community_cards(deck, 'turn')
    print(f"\nTurn: {community_cards}")

    # Round of betting on the turn
    for player in range(num_players):
        if hands[player]:
            if player == 0:
                print(f"\nCurrent pot: ${pot}")
                print(f"Your hand: {hands[0]}")
                print(f"Community cards: {community_cards}")
                action = input(f"Your turn! [fold, check, raise]: ").lower()
                if action == "fold":
                    print("You folded!")
                    return
                elif action == "raise":
                    raise_amount = int(input("Enter raise amount: "))
                    current_bet = raise_amount
                    player_money[0] -= raise_amount
                    pot += raise_amount
            else:
                action, bet, pot = ai_action(player, hands[player], community_cards, current_bet, pot, player_money)
                if action == "fold":
                    print(f"Player {player + 1} folded.")
                    hands[player] = None
                else:
                    print(f"Player {player + 1} {action}ed ${bet}.")
    
    print(f"\nPot after betting: ${pot}")

    # River
    community_cards += deal_community_cards(deck, 'river')
    print(f"\nRiver: {community_cards}")

    # Round of betting on the river
    for player in range(num_players):
        if hands[player]:
            if player == 0:
                print(f"\nCurrent pot: ${pot}")
                print(f"Your hand: {hands[0]}")
                print(f"Community cards: {community_cards}")
                action = input(f"Your turn! [fold, check, raise]: ").lower()
                if action == "fold":
                    print("You folded!")
                    return
                elif action == "raise":
                    raise_amount = int(input("Enter raise amount: "))
                    current_bet = raise_amount
                    player_money[0] -= raise_amount
                    pot += raise_amount
            else:
                action, bet, pot = ai_action(player, hands[player], community_cards, current_bet, pot, player_money)
                if action == "fold":
                    print(f"Player {player + 1} folded.")
                    hands[player] = None
                else:
                    print(f"Player {player + 1} {action}ed ${bet}.")
    
    print(f"\nPot after betting: ${pot}")

    # Showdown
    print("\n--- Showdown ---")
    for i, hand in enumerate(hands):
        if hand:
            result = evaluate_hand(hand, community_cards)
            print(f"Player {i + 1}: {hand} -> {result}")
    
    # Determinare il vincitore (qui semplificato: chi ha la mano migliore tra chi non ha foldato)
    best_hand = None
    winner = None
    for i, hand in enumerate(hands):
        if hand:
            hand_value = evaluate_hand(hand, community_cards)
            if not best_hand or hand_value > best_hand:
                best_hand = hand_value
                winner = i + 1
    
    print(f"\nPlayer {winner} wins the pot of ${pot}!")
    player_money[winner - 1] += pot
    print(f"Player {winner} now has ${player_money[winner - 1]}")

# Simulazione di una partita con 3 giocatori (tu contro 2 avversari)
simulate_game(3)
