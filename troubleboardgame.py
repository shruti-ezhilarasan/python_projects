# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Deepna Kanjee
#               Clara Berg
#               Saachi Jain
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Team FInal Project
# Date:         23 November 2024

import turtle
import random


yellow_border = [
    (-240, 200), (-180, 230), (-120, 230), (-50, 230), (20, 230),
    (80, 230), (170, 230),
   
    (240, 200), (260, 140), (260, 60),
    (260, 0), (260, -60), (260, -120), (240, -200),


    (240, -200), (180, -230), (100, -230), (20, -230), (-70, -230),
    (-140, -230),


    (-240, -210), (-260, -140), (-260, -60),(-260, 0), (-260, 60), (-260, 120),
    (-180, 160), (-135, 125), (-100, 100), (-55, 65)
]


blue_border = [ #all these list include the home coordinates too
    (240, 200), (260, 140), (260, 60),
    (260, 0), (260, -60), (260, -120), (240, -200),


    (240, -200), (180, -230), (100, -230), (20, -230), (-70, -230),
    (-140, -230),


    (-240, -210), (-260, -140), (-260, -60),(-260, 0), (-260, 60), (-260, 120),


    (-240, 200), (-180, 230), (-120, 230), (-50, 230), (20, 230),
    (80, 230), (170, 230),
    (185, 150), (155, 125), (120, 100), (95, 65)]
red_border = [
    (240, -200), (180, -230), (100, -230), (20, -230), (-70, -230),
    (-140, -230),


    (-240, -210), (-260, -140), (-260, -60),(-260, 0), (-260, 60), (-260, 120),


    (-240, 200), (-180, 230), (-120, 230), (-50, 230), (20, 230),
    (80, 230), (170, 230),
   
    (240, 200), (260, 140), (260, 60),
    (260, 0), (260, -60), (260, -120), (240, -200),
    (190, -150), (155, -125), (120, -100), (95, -65)
]
green_border = [
    (-240, -210), (-260, -140), (-260, -60),(-260, 0), (-260, 60), (-260, 120),


    (-240, 200), (-180, 230), (-120, 230), (-50, 230), (20, 230),
    (80, 230), (170, 230),
   
    (240, 200), (260, 140), (260, 60),
    (260, 0), (260, -60), (260, -120), (240, -200),


    (240, -200), (180, -230), (100, -230), (20, -230), (-70, -230),
    (-140, -230),
    (-185, -155), (-145,-125), (-100, -100), (-55, -55)
]
# Game setup
def display_instructions():
    """Displays the rules and instructions for the game."""
    print("""
    Welcome to Trouble!
         
    Objective: A player must get the pawn to home before the other players.
   
    How to Play:
    1. The user will be prompted the amount of players
    2. Each player will then be prompted to either enter “roll”, “instructions”, “score”, or “quit”.
    3. When the player rolls a 6 the piece will be moved to the starting position.
    4. The first player to move their piece into the home are will be claimed the winner
   
    Winner:
    Once the piece of one player has been placed in the Home Base they are the winner!


    Options:
    - Type 'roll' to roll the dice.
    - Type 'instructions' to view instructions.
    - Type 'score' to see the current standings.
    - Type 'quit' to exit the game early.
    """)


def draw_board():
    """Sets the background image of the game board."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Trouble Game Board")
   
    # Set the background image to 'Board_v1.gif'
    screen.bgpic("Troubleboard.gif")  # Make sure 'Board_v1.gif' is in the same directory or provide the full path to the image file


    # Hide the turtle cursor as we only want the image to be visible
    pen = turtle.Turtle()
    pen.hideturtle()


def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)


def draw_piece(x, y, color):
    """Draws a player piece at a given location."""
    piece = turtle.Turtle()
    piece.shape("circle")
    piece.color(color)
    piece.penup()
    piece.goto(x, y)
    piece.speed(0)
    return piece
count_yellow = []
count_blue = []
count_green = []
count_red = []
def main():
    global x
    global y
    global count_yellow, count_blue, count_green, count_red
    """Main function to manage the game."""
    # Display the rules
    display_instructions()
   
    # Let the user choose the number of players
    while True:
        try:
            players = int(input("Enter the number of players (2, 3, or 4): "))
            if players not in [2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please choose 2, 3, or 4 players.")
   
    # Initialize player data
    player_colors = ['yellow', 'blue', 'green', 'red']
    player_positions = {f"Player {i+1}": [0] for i in range(players)}  # 4 pieces per player
    game_log = "game_log.txt"
   
    # Write initial game state to file
    with open(game_log, "w") as file:
        file.write("Game Start\n")
        file.write(f"Players: {', '.join([f'Player {i+1}' for i in range(players)])}\n")
   
    # Draw the board
    draw_board()
   
    # Set initial positions for pieces in the four corners of the board
    player_start_positions = {
        "Player 1": [(-300, 150)],  # Top-left corner
        "Player 2": [(300, 150)],          # Top-right corner
        "Player 3": [(-300, -50)],  # Bottom-left corner
        "Player 4": [(300, -50)],       # Bottom-right corner
    }
   
    # Create players' pieces and place them in the starting corners
    player_pieces = {}
    for i in range(players):
        pieces = []
        for j in range(1):
            color = player_colors[i]
            start_position = player_start_positions[f"Player {i+1}"][j]
            pieces.append(draw_piece(start_position[0], start_position[1], color))
        player_pieces[f"Player {i+1}"] = pieces
   
    turn = 0
    while True:


        current_player = f"Player {turn + 1}"
        print(f"\n{current_player}'s turn!")
        action = input("Choose an action (roll/instructions/score/quit): ").strip().lower()
       
        if action == "roll":
            dice = roll_dice()
            print(f"{current_player} rolled a {dice}!")
           
            if dice == 6 and player_positions[current_player][0] == 0:
                print(f"{current_player} moves their piece onto the board!")
                player_positions[current_player][0] = 1
                if current_player == "Player 1":
                    player_pieces[current_player][0].goto(yellow_border[0])  # Move the first piece to the start
                elif current_player == "Player 2":
                    player_pieces[current_player][0].goto(blue_border[0])  # Move the first piece to the start
                elif current_player == "Player 3":
                    player_pieces[current_player][0].goto(green_border[0])  # Move the first piece to the start
                elif current_player == "Player 4":
                    player_pieces[current_player][0].goto(red_border[0])  # Move the first piece to the start
               
            elif any(pos > 0 for pos in player_positions[current_player]):
                # Move the first piece that is on the board
                for i, pos in enumerate(player_positions[current_player]):
                    if pos > 0:
                        player_positions[current_player][i] += dice
                       
                        # Move the piece visually
                        if current_player == "Player 1":
                           
                            count_yellow.append(dice)
                            total = sum(count_yellow)
                            try:
                                player_pieces[current_player][i].goto(yellow_border[total])
                            except:
                                dice = roll_dice()
                                print(f"{current_player} rolled a {dice}!")
                                                               


                        elif current_player == "Player 2":
                           
                            count_blue.append(dice)
                            total = sum(count_blue)
                            try:
                                player_pieces[current_player][i].goto(blue_border[total])
                            except:
                                dice = roll_dice()
                                print(f"{current_player} rolled a {dice}!")


                        elif current_player == "Player 3":
                           
                            count_green.append(dice)
                            total = sum(count_green)
                            try:
                                player_pieces[current_player][i].goto(green_border[total])
                            except:
                                dice = roll_dice()
                                print(f"{current_player} rolled a {dice}!")


                        elif current_player == "Player 4":
                           
                            count_red.append(dice)
                            total = sum(count_red)
                            try:
                                player_pieces[current_player][i].goto(red_border[total])
                            except:
                                dice = roll_dice()
                                print(f"{current_player} rolled a {dice}!")
                       
                        break
            else:
                print(f"{current_player} cannot move until they roll a 6.")
           
            # Log the move
            with open(game_log, "a") as file:
                file.write(f"{current_player} rolled {dice}\n")
                file.write(f"{current_player} positions: {player_positions[current_player]}\n")
           
            # Check for win condition
            if current_player == "Player 1":
                win_positions = yellow_border[-4:]  # Last four coordinates for Player 1
            elif current_player == "Player 2":
                win_positions = blue_border[-4:]  # Last four coordinates for Player 2
            elif current_player == "Player 3":
                win_positions = green_border[-4:]  # Last four coordinates for Player 3
            elif current_player == "Player 4":
                win_positions = red_border[-4:]  # Last four coordinates for Player 4


            # Check if any piece of the current player is at a win position
            for piece_position in player_pieces[current_player]:
                if piece_position.pos() in win_positions:
                    print(f"🎉 {current_player} wins the game! 🎉")
                    with open(game_log, "a") as file:
                        file.write(f"{current_player} wins the game!\n")
                    return  # Exit the game after a win
       
        elif action == "instructions":
            display_instructions()
       
        elif action == "score":
            print("Current standings:")
            for player, pos in player_positions.items():
                print(f"{player}: Positions {pos}")
       
        elif action == "quit":
            print(f"{current_player} chose to quit. Game over!")
            with open(game_log, "a") as file:
                file.write("Game quit early.\n")
            break
       
        else:
            print("Invalid option. Try again.")
       
        # Move to the next player's turn
        turn = (turn + 1) % players


# Run the game
if __name__ == "__main__":
    main()



