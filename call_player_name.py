def call_player_name(player_name):
    """
    This function takes a player's name as input and prints a welcome message.
    
    Args:
        player_name (str): The name of the player.
    
    Returns:
        None
    """
    print(f"welcome to the game, {player_name}")
    return player_name
player_name = input("Enter your name: ")
new_name=input, call_player_name(player_name)
print(f"Player name set to: {new_name}")