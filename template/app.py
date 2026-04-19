import mysql.connector
from player_manager import (
    add_player,
    change_player,
    delete_player,
    list_players,
    update_player_score,
)
from player_stats import (
    query_player_stats,
    additional_query_1,
    additional_query_2,
    additional_query_3,
    additional_query_4,
)

# Establish connection to database (edit accordingly)
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="pepper",
    password="",
    database="pepper",
)


def main():
    """Main program loop with menu system."""
    while True:
        # Print menu header
        # Print all menu options:

        # 1. Maintain Player
        #   1. Add Player
        #   2. Change Player
        #   3. Delete Player
        #   4. List Players
        #   5. Update Player Score (Stored Procedure)

        # 2. Player Reports
        #   1. Player Statistics (Stored Procedure)
        #   2. Additional Query 1 (GROUP BY)
        #   3. Additional Query 2 (Subquery)
        #   4. Additional Query 3 (HAVING)
        #   5. Additional Query 4 (LEFT OUTER JOIN)

        # 3. Exit

        # Prompt user for choice

        # Use match-case statement to handle menu options:
        # - For each option, call corresponding function with conn
        # - For option 3, print goodbye and break from loop
        # - Use case _ to handle invalid choices
        break

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
