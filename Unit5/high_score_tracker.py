"""
The High-Score Tracker Game
------------------------------
Continuously asks an arcade player for their game score until they type
"stop" to end the session.
"""

# 1. Start an intentional infinite loop
while True:

    # 2. Ask the user to enter a game score next to the flashing cursor
    user_input = input("Enter your game score (or type 'stop' to end): ")

    # 3. Clean up the input and check if the player wants to stop
    if user_input.strip().lower() == "stop":
        print("Game session ended!")
        break

    # 4. Otherwise, cast the input to an int and check the score
    else:
        score = int(user_input)

        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")