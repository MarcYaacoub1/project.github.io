import time

def main():
    while True:
        score = 0
        print("\nWelcome to the Harry Potter Story Adventure!")
        print("You'll make choices that affect Harry's journey. Let's begin!\n")
        time.sleep(1)
        
        path1(score)
        
        restart = input("\nWould you like to play again? (yes/no): ").lower()
        if restart != 'yes':
            print("\nThanks for playing! Wizards unite!")
            break

def path1(score):
    print("Year 1: The Philosopher's Stone")
    print("Harry has just arrived at Hogwarts. What should he do first?")
    print("1. Make friends with Ron and Hermione")
    print("2. Explore the castle on his own")
    print("3. Try to find out more about the mysterious third-floor corridor")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print("\nHarry befriends Ron and Hermione. Their friendship will be crucial!")
        score += 10
        print("\nLater, Harry hears about Nicolas Flamel. What should he do?")
        print("1. Research in the library with Hermione")
        print("2. Ask Hagrid about it")
        print("3. Ignore it and focus on Quidditch")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\nYou discover Flamel is connected to the Philosopher's Stone!")
            score += 15
            print("\nAt night, you see Snape threatening Quirrell. What do you do?")
            print("1. Follow them secretly")
            print("2. Tell Dumbledore immediately")
            print("3. Confront Snape")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                print("\nYou discover Quirrell is the real villain! You help stop him and save the Stone!")
                score += 25
                ending(score)
            elif choice == '2':
                print("\nDumbledore handles the situation expertly. Hogwarts is safe!")
                score += 20
                ending(score)
            else:
                print("\nSnape turns out to be protecting Harry all along, but you lost crucial time!")
                score += 10
                ending(score)
                
        elif choice == '2':
            print("\nHagrid accidentally reveals Fluffy's weakness! This helps later.")
            score += 12
            print("\nDuring the Quidditch match, you see Snape cursing your broom. What do you do?")
            print("1. Let Hermione handle it")
            print("2. Try to fight the curse yourself")
            
            choice = input("Enter your choice (1-2): ")
            
            if choice == '1':
                print("\nHermione sets Snape's robes on fire! You win the match!")
                score += 18
                ending(score)
            else:
                print("\nYou fall off your broom but learn an important lesson about teamwork.")
                score += 8
                ending(score)
        else:
            print("\nYou become a great Quidditch player but miss important clues!")
            score += 5
            ending(score)
            
    elif choice == '2':
        print("\nHarry gets lost and ends up in the forbidden corridor! Points lost.")
        score -= 5
        print("\nYou encounter Fluffy the three-headed dog. What do you do?")
        print("1. Play music to calm it")
        print("2. Run away screaming")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            print("\nYou remember Hagrid's hint and survive! But you're in trouble with Filch.")
            score += 5
            ending(score)
        else:
            print("\nYou're caught by Filch and lose house points. Detention!")
            score -= 10
            ending(score)
    else:
        print("\nHarry gets caught by Filch! 50 points from Gryffindor!")
        score -= 20
        ending(score)

def path2(score):
    print("\nYear 3: The Prisoner of Azkaban")
    print("Harry learns Sirius Black has escaped Azkaban. What should he do?")
    print("1. Tell Professor Lupin his concerns")
    print("2. Investigate on his own")
    print("3. Focus on Quidditch and ignore the rumors")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print("\nLupin teaches you the Patronus charm! Very useful against Dementors.")
        score += 15
        print("\nYou receive a mysterious Firebolt broom. What do you do?")
        print("1. Accept it gratefully")
        print("2. Report it to McGonagall")
        print("3. Have Hermione check it for curses")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\nIt turns out to be from Sirius! You become an even better Quidditch player.")
            score += 20
            print("\nYou discover the truth about Sirius and Pettigrew. What do you do?")
            print("1. Let Sirius explain everything")
            print("2. Attack Pettigrew immediately")
            
            choice = input("Enter your choice (1-2): ")
            
            if choice == '1':
                print("\nYou learn the whole truth! Sirius is innocent!")
                score += 25
                ending(score)
            else:
                print("\nPettigrew escapes! But at least you know the truth now.")
                score += 15
                ending(score)
        elif choice == '2':
            print("\nMcGonagall confiscates it but later returns it when it's deemed safe.")
            score += 10
            ending(score)
        else:
            print("\nHermione finds no curses but you lose some time with the broom.")
            score += 12
            ending(score)
            
    elif choice == '2':
        print("\nYou sneak into Hogsmeade with the Marauder's Map!")
        score += 5
        print("\nYou overhear a conversation about Sirius Black. What do you do?")
        print("1. Confront the speakers")
        print("2. Report to Dumbledore")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            print("\nYou learn valuable information but get in trouble for being in Hogsmeade!")
            score += 8
            ending(score)
        else:
            print("\nDumbledore praises your responsibility but you miss some clues.")
            score += 12
            ending(score)
    else:
        print("\nYou win the Quidditch Cup but are unprepared for the Dementor attack!")
        score -= 5
        ending(score)

def ending(score):
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
    
    print("Thanks for playing this Harry Potter adventure!")

if __name__ == "__main__":
    main()