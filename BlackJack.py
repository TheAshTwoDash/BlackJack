import random
import time
running = True
dealer_card_numbers = []
dealer_card_faces = []
player_card_numbers = []
player_card_faces = []
all_numbers = []
all_faces = []
#global dealer_card_numbers,dealer_card_faces,all_numbers,all_faces,player_card_numbers,player_card_faces,running

def create_card(character):
    time.sleep(0.3)
    card_number = random.randrange(1,14)
    card_face = random.choice(["Diamond","Clover","Heart","Spade"])
    message = f"{card_number} {card_face}"
    
    if card_number > 10:
        card_number = 10
        card_face += random.choice([" Jack"," Queen"," King"])
        message = card_face
    elif card_number == 1:
        message = f"A {card_face}"

    if prevent_dupes(card_number, card_face):
        create_card(character) 
        
    elif character == "player":
        print("\nPlayer just drew",message)
        player_card_numbers.append(card_number)
        player_card_faces.append(card_face)    
        all_numbers.append(card_number)
        all_faces.append(card_face)
        
    elif character == "dealer":
        print("\nDealer just drew",message)
        dealer_card_numbers.append(card_number)
        dealer_card_faces.append(card_face)    
        all_numbers.append(card_number)
        all_faces.append(card_face)
        
def check_ace(card_number):
    for i in range(0,len(card_number)):
        if card_number[i] == 1:
            return True
    return False

def player_draw():
    create_card("player")
    global player_total
    if check_ace(player_card_numbers):
            player_total = sum(player_card_numbers) + 10
            if player_total > 21:
                player_total -= 10
                print(f"\nPlayer has \n{player_total}")
            else:
                print("\nPlayer has")
                print(player_total -10,"/", player_total)      
    elif not check_ace(player_card_numbers):
        player_total = sum(player_card_numbers)
        print(f"\nPlayer has {player_total}")

def dealer_draw():
    create_card("dealer")
    global dealer_total
    if check_ace(dealer_card_numbers):
            dealer_total = sum(dealer_card_numbers) + 10
            if dealer_total > 21:
                dealer_total -= 10
                print("\nDealer has \n{dealer_total}")
            else:
                print("\nDealer has")
                print(dealer_total -10,"/", dealer_total)      
    elif not check_ace(dealer_card_numbers):
        dealer_total = sum(dealer_card_numbers)
        print(f"\nDealer has \n{dealer_total}")

def checkwinner():
        if dealer_total >= 17:
            if dealer_total > 21:
                print("Dealer busted")
                print("You won")
            elif dealer_total > player_total:
                print("Dealer won")
            elif dealer_total < player_total and player_total<22:
                print("you win")
            elif dealer_total == player_total:
                print("it's a draw")
        elif player_total > dealer_total:
            if player_total > 21:
                print("You busted")
                print("Dealer won")

def draw():      
        if player_total <22:
            global draw_input
            draw_input = int(input("press 1 to hit and press 2 to stand "))
            if draw_input == 1 and player_total < 21:
                player_draw()
                draw()
            elif draw_input == 2:
                while dealer_total < 17:
                    dealer_draw()
        else:
            checkwinner()
            
def blackjack():
    if player_total == 21 and dealer_total == 21:
        print("\nDraw, both got blackjack")
        return True
    elif player_total == 21:
        print("\nPlayer got blackjack, you win")
        return True
    elif dealer_total == 21:
        print("\nDealer got blackjack, they win")
        return True

def prevent_dupes(card_number,card_face):
    for i in range(0,len(all_numbers)):
        if card_number == all_numbers[i] and card_face == all_faces[i]:
            return True
    return False
    
def erase():
    global dealer_card_numbers,dealer_card_faces,all_numbers,all_faces,player_card_numbers,player_card_faces, player_total, dealer_total, draw_input
    all_numbers = []
    all_faces = []
    dealer_card_numbers = []
    dealer_faces = []
    player_card_numbers = []
    player_faces = []
    player_total, dealer_total,draw_input = 0,0,0

def exit_prompt():
    exit = int(input("\nwould you like to play again? \n3 to exit \t4 to continue"))
    if exit == 3:
        global running
        running = False
    erase()
    
while running == True:
    player_draw()
    player_draw()
    dealer_draw()
    if blackjack():
        erase()
        continue
    draw()
    checkwinner()
    exit_prompt()

    
