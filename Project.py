import time
import random

# Constants for scoring
FRIENDSHIP_SCORE = 10
DISCOVERY_SCORE = 15
HEROIC_SCORE = 25
PENALTY_SCORE = -20

def main():
    """Main function that runs the Harry Potter adventure game."""
    print("\nWelcome to the Harry Potter Story Adventure!")
    print("You'll make choices that affect Harry's journey. Your score changes with each decision!\n")
    
    while True:
        score = 0
        play_game(score)
        
        restart = input("\nWould you like to play again? (yes/no): ").lower()
        if restart != 'yes':
            print("\nThanks for playing! Wizards unite!")
            break

def play_game(score):
    """Main game loop that handles the adventure paths."""
    # Randomly choose which story path to take
    if random.choice([True, False]):
        score = path_philosophers_stone(score)
    else:
        score = path_prisoner_of_azkaban(score)
    
    ending(score)

def path_philosophers_stone(score):
    """Handle the Philosopher's Stone storyline."""
    print("\nYear 1: The Philosopher's Stone")
    print("Harry has just arrived at Hogwarts. What should he do first?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Make friends with Ron and Hermione")
        print("2. Explore the castle on his own")
        print("3. Try to find out about the mysterious third-floor corridor")
        
        choice = get_valid_input("Enter your choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            score += FRIENDSHIP_SCORE
            print(f"\nHarry befriends Ron and Hermione. (+{FRIENDSHIP_SCORE} points)")
            score = handle_flamel_discovery(score)
            break
        elif choice == '2':
            score -= 5
            print("\nHarry gets lost and ends up in the forbidden corridor! (-5 points)")
            score = handle_fluffy_encounter(score)
            break
        else:
            score += PENALTY_SCORE
            print(f"\nHarry gets caught by Filch! {PENALTY_SCORE} points from Gryffindor!")
            ending(score)
            break
    
    return score

def handle_flamel_discovery(score):
    """Handle the Nicolas Flamel discovery path."""
    print("\nLater, Harry hears about Nicolas Flamel. What should he do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Research in the library with Hermione")
        print("2. Ask Hagrid about it")
        print("3. Ignore it and focus on Quidditch")
        
        choice = get_valid_input("Enter your choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            score += DISCOVERY_SCORE
            print(f"\nYou discover Flamel is connected to the Philosopher's Stone! (+{DISCOVERY_SCORE} points)")
            score = handle_quirrell_confrontation(score)
            break
        elif choice == '2':
            score += 12
            print("\nHagrid accidentally reveals Fluffy's weakness! (+12 points)")
            score = handle_quidditch_match(score)
            break
        else:
            score += 5
            print("\nYou become a great Quidditch player but miss important clues! (+5 points)")
            ending(score)
            break
    
    return score

def handle_fluffy_encounter(score):
    """Handle the encounter with Fluffy the three-headed dog."""
    print("\nYou encounter Fluffy the three-headed dog. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Play music to calm it")
        print("2. Run away screaming")
        
        choice = get_valid_input("Enter your choice (1-2): ", ['1', '2'])
        
        if choice == '1':
            score += 5
            print("\nYou remember Hagrid's hint and survive! But you're in trouble with Filch. (+5 points)")
            break
        else:
            score -= 10
            print("\nYou're caught by Filch and lose house points. Detention! (-10 points)")
            break
    
    ending(score)
    return score

def handle_quidditch_match(score):
    """Handle the Quidditch match scenario."""
    print("\nDuring the Quidditch match, you see Snape cursing your broom. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Let Hermione handle it")
        print("2. Try to fight the curse yourself")
        
        choice = get_valid_input("Enter your choice (1-2): ", ['1', '2'])
        
        if choice == '1':
            score += 18
            print("\nHermione sets Snape's robes on fire! You win the match! (+18 points)")
            break
        else:
            score += 8
            print("\nYou fall off your broom but learn an important lesson about teamwork. (+8 points)")
            break
    
    ending(score)
    return score

def handle_quirrell_confrontation(score):
    """Handle the confrontation with Quirrell."""
    print("\nAt night, you see Snape threatening Quirrell. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Follow them secretly")
        print("2. Tell Dumbledore immediately")
        print("3. Confront Snape")
        
        choice = get_valid_input("Enter your choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            score += HEROIC_SCORE
            print(f"\nYou discover Quirrell is the real villain! You help stop him! (+{HEROIC_SCORE} points)")
            break
        elif choice == '2':
            score += 20
            print("\nDumbledore handles the situation expertly. Hogwarts is safe! (+20 points)")
            break
        else:
            score += 10
            print("\nSnape turns out to be protecting Harry all along! (+10 points)")
            break
    
    ending(score)
    return score

def path_prisoner_of_azkaban(score):
    """Handle the Prisoner of Azkaban storyline."""
    print("\nYear 3: The Prisoner of Azkaban")
    print("Harry learns Sirius Black has escaped Azkaban. What should he do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Tell Professor Lupin his concerns")
        print("2. Investigate on his own")
        print("3. Focus on Quidditch and ignore the rumors")
        
        choice = get_valid_input("Enter your choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            score += 15
            print("\nLupin teaches you the Patronus charm! Very useful against Dementors. (+15 points)")
            score = handle_firebolt(score)
            break
        elif choice == '2':
            score += 5
            print("\nYou sneak into Hogsmeade with the Marauder's Map! (+5 points)")
            score = handle_hogsmeade_conversation(score)
            break
        else:
            score -= 5
            print("\nYou win the Quidditch Cup but are unprepared for Dementors! (-5 points)")
            ending(score)
            break
    
    return score

def handle_firebolt(score):
    """Handle the Firebolt broom scenario."""
    print("\nYou receive a mysterious Firebolt broom. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Accept it gratefully")
        print("2. Report it to McGonagall")
        print("3. Have Hermione check it for curses")
        
        choice = get_valid_input("Enter your choice (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            score += 20
            print("\nIt turns out to be from Sirius! You become an even better Quidditch player. (+20 points)")
            score = handle_sirius_revelation(score)
            break
        elif choice == '2':
            score += 10
            print("\nMcGonagall confiscates it but later returns it when it's deemed safe. (+10 points)")
            break
        else:
            score += 12
            print("\nHermione finds no curses but you lose some time with the broom. (+12 points)")
            break
    
    ending(score)
    return score

def handle_hogsmeade_conversation(score):
    """Handle the Hogsmeade conversation scenario."""
    print("\nYou overhear a conversation about Sirius Black. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Confront the speakers")
        print("2. Report to Dumbledore")
        
        choice = get_valid_input("Enter your choice (1-2): ", ['1', '2'])
        
        if choice == '1':
            score += 8
            print("\nYou learn valuable information but get in trouble for being in Hogsmeade! (+8 points)")
            break
        else:
            score += 12
            print("\nDumbledore praises your responsibility but you miss some clues. (+12 points)")
            break
    
    ending(score)
    return score

def handle_sirius_revelation(score):
    """Handle the revelation about Sirius Black."""
    print("\nYou discover the truth about Sirius and Pettigrew. What do you do?")
    
    while True:
        print(f"\nCurrent score: {score}")
        print("1. Let Sirius explain everything")
        print("2. Attack Pettigrew immediately")
        
        choice = get_valid_input("Enter your choice (1-2): ", ['1', '2'])
        
        if choice == '1':
            score += 25
            print("\nYou learn the whole truth! Sirius is innocent! (+25 points)")
            break
        else:
            score += 15
            print("\nPettigrew escapes! But at least you know the truth now. (+15 points)")
            break
    
    ending(score)
    return score

def get_valid_input(prompt, valid_options):
    """Get and validate user input with retry on invalid input."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def ending(score):
    """Display the final results and score evaluation."""
    print("\n--- Story Conclusion ---")
    print(f"Your final score: {score} points")
    
    if score >= 40:
        print("Excellent! You're a true wizard hero!")
    elif score >= 20:
        print("Good job! You made some great choices.")
    elif score >= 0:
        print("You survived, but could have done better.")
    else:
        print("Oh dear... Maybe stay away from adventures next time.")

if __name__ == "__main__":
    main()
