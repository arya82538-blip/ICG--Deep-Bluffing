import random

from agent import CustomPokerBot, create_deck, best_hand

class DumbOpponent:
   
    def __init__(self, name="Challenger"):
        self.name = name
    def get_action(self, hole_cards, community_cards, pot_size, stack_size, amount_to_call, legal_actions):
        if amount_to_call == 0:
            return "CALL" 
        return "CALL" if "CALL" in legal_actions else legal_actions[0]

def play_test_game():
    my_bot = CustomPokerBot("DeepBluff")
    opponent = DumbOpponent("Challenger_Bot")
    
    deck = create_deck()
    random.shuffle(deck)
    
    p1_hand = [deck.pop(), deck.pop()]
    p2_hand = [deck.pop(), deck.pop()]
    community = []
    
    p1_stack = 1000
    p2_stack = 1000
    pot = 0
    
    print("\n" + "=" * 50)
    print("        POKER GAME ARENA LOCAL SIMULATOR       ")
    print("=" * 50)
    print(f"DeepBluff (You) Cards : {p1_hand}")
    print(f"Opponent Cards        : {p2_hand}\n")
    
    # --- Round 1: Pre-Flop ---
    print("--- ROUND: PRE-FLOP ---")
    pot += 20
    p1_stack -= 10
    p2_stack -= 10
    
    action1 = my_bot.get_action(p1_hand, community, pot, p1_stack, 0, ["CHECK", "RAISE"])
    action2 = opponent.get_action(p2_hand, community, pot, p2_stack, 0, ["CHECK", "RAISE"])
    print(f"-> DeepBluff chooses : {action1}")
    print(f"-> Opponent chooses  : {action2}\n")
    
    # --- Round 2: Flop ---
    community = [deck.pop(), deck.pop(), deck.pop()]
    print(f"--- ROUND: FLOP --- (Board: {community})")
    
    action1 = my_bot.get_action(p1_hand, community, pot, p1_stack, 10, ["CALL", "RAISE", "FOLD"])
    action2 = opponent.get_action(p2_hand, community, pot, p2_stack, 0, ["CHECK", "RAISE"])
    print(f"-> DeepBluff chooses : {action1}")
    print(f"-> Opponent chooses  : {action2}\n")
    
    # --- Round 3: Turn ---
    community.append(deck.pop())
    print(f"--- ROUND: TURN --- (Board: {community})")
    
    action1 = my_bot.get_action(p1_hand, community, pot, p1_stack, 20, ["CALL", "RAISE", "FOLD"])
    action2 = opponent.get_action(p2_hand, community, pot, p2_stack, 0, ["CHECK", "RAISE"])
    print(f"-> DeepBluff chooses : {action1}")
    print(f"-> Opponent chooses  : {action2}\n")
    
    # --- Round 4: River ---
    community.append(deck.pop())
    print(f"--- ROUND: RIVER --- (Board: {community})")
    
    action1 = my_bot.get_action(p1_hand, community, pot, p1_stack, 20, ["CALL", "RAISE", "FOLD"])
    action2 = opponent.get_action(p2_hand, community, pot, p2_stack, 0, ["CHECK", "RAISE"])
    print(f"-> DeepBluff chooses : {action1}")
    print(f"-> Opponent chooses  : {action2}\n")
    
    # --- Showdown ---
    print("--- SHOWDOWN ---")
    p1_score = best_hand(p1_hand + community)
    p2_score = best_hand(p2_hand + community)
    
    print(f"Your Total Hand Score  : {p1_score}")
    print(f"Opponent's Hand Score  : {p2_score}")
    
    if p1_score > p2_score:
        print("\n RESULT: DeepBluff Wins the Pot!")
    elif p2_score > p1_score:
        print("\n RESULT: Opponent Wins!")
    else:
        print("\n RESULT: It's a TIE (Split Pot)!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    play_test_game()