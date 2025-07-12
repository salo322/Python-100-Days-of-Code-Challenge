# Treasure Island
print("Welcome to the treasure island!\nYour mission is to find the treasure!")

left_or_right = input("You are at the cross road. Where do you want to go?\n  Type 'left' or 'right'\n")

if left_or_right == 'right':
    print("You fell into a hole. Game Over!")
else:
    wait_or_swim = input("You have come to lake. There is a island in the middle of the lake.\n"
                         "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if wait_or_swim == 'swim':
        print("You got attacked by angry troat. Game Over!")
    else:
        color = input("You arrive at the island unharmed. There is a house with 3 doors.\n"
                      "One red, one yellow and one blue. Which color do you choose?\n")
        if color == 'red':
            print("It's a room full of fire. Game Over!")
        elif color == 'blue':
            print("You enter a room of beasts. Game Over!")
        else:
            print("You found a treasure. You win!")
