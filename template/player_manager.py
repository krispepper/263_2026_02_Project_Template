def add_player(conn):
    """Add a new player to the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for: Player ID, Name, Color, Wins, Losses, Gold
    # Write INSERT query to add the player to the demo_players table
    # Commit the transaction
    # Print success message
    # Close the cursor
    pass


def change_player(conn):
    """Update player information in database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID to change
    # Write SELECT query to fetch player data
    # If player not found, print message and return
    # Display current player data
    # Print menu of fields to change (1-5):
    #   1. Name
    #   2. Color
    #   3. Wins
    #   4. Losses
    #   5. Gold
    # Prompt user for field choice
    # If invalid choice, print message and return
    # Map choice to field name using a dictionary
    # Prompt user for new value for selected field
    # Write UPDATE query to modify only that field
    # Commit the transaction
    # Print success message
    # Close the cursor
    pass


def delete_player(conn):
    """Delete a player from the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID to delete
    # Write DELETE query to remove the player
    # Commit the transaction
    # Print deletion message
    # Close the cursor
    pass


def list_players(conn):
    """List all players in the database.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Write SELECT query to fetch all players
    # If no players found, print message and return
    # Print header row with column names
    # Loop through results and print each player
    # Close the cursor
    pass


def update_player_score(conn):
    """Update a player's wins using UpdatePlayerScore stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    # Create a cursor with dictionary=True
    # Prompt user for Player ID and new number of wins
    # Call the UpdatePlayerScore stored procedure using cur.callproc()
    # Commit the transaction
    # Print success message
    # Close the cursor
    pass
