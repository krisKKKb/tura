
anserw_a = "1"
anserw_b = "2"
anserw_c = "3"
anserw = input("Choose your door 1,2 or 3: ")
if anserw == anserw_a:
    print("You chose door one, you move to the living room")
    livingroom_a = ["a","A"]
    livingroom_b = ["b","B"]
    livingroom_c = ["c","C"]
    fight_living = input("You meet an ghost in the living room choose your weapon, A for knife, B for vaccuum cleaner and C for assault rifle: ")
    if fight_living == livingroom_a:
        print("You died to a ghost because knife could not harm him and he killed you, You lost the game!")
    elif fight_living == livingroom_b:
        print("You sucked ghost into the vaccum cleaner and it neutralized him, You won the game!")
    elif fight_living == livingroom_c:
        print("Oh no you chose assault rifle and the bullets did go right through him and he killed you, You lost the game!")
    else:
        print("You chose to fight it barefists and it just gut you with knife, You lost the game!")
elif anserw == anserw_b:
    print("You chose door two, you move to the basement")
    basement_a = ["A"]
    basement_b = ["B"]
    basement_c = ["C"]
    fight_basement = input("You meet an Giant human squid hybrid in basement choose your weapon, A for shotgun, B for assault rifle, C for sword: ")
    if fight_basement == basement_a:
        print("Shotgun bullets spread out too far away it harmed him very little and while you were reloading he killed you, You lost the game")
    elif fight_basement == basement_b:
        print("You killed him with assault rifle, You won the game")
    elif fight_basement == basement_c:
        print("You killed the giant squid with sword but you injuries were too crucial to escape and you died next to him, You lost the game")
    else:
        print("You chose to fight him bare hand you died,You lost the game")
elif anserw == anserw_c:
    print("You chose door three, you move to the kitchen")
    print("It was the easiest escape, you won the game!")
else:
    print("You stand in one place, you couldnt decide in time and you died to starvation,Game Over")