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
    query_players_by_wins,
    query_players_by_gold,
    query_top_players,
    query_all_players_with_stats,
)

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="pepper",
    password="",
    database="pepper",
)


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Maintain Player")
        print("2. Player Reports")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        match choice:
            case "1":
                print("\n--- Maintain Player ---")
                print("1. Add Player")
                print("2. Change Player")
                print("3. Delete Player")
                print("4. List Players")
                print("5. Update Player Score (Stored Procedure)")

                subchoice = input("Enter your choice (1-5): ").strip()

                match subchoice:
                    case "1":
                        add_player(conn)
                    case "2":
                        change_player(conn)
                    case "3":
                        delete_player(conn)
                    case "4":
                        list_players(conn)
                    case "5":
                        update_player_score(conn)
                    case _:
                        print("Invalid choice. Please try again.")
            case "2":
                print("\n--- Player Reports ---")
                print("1. Player Statistics (Stored Procedure)")
                print("2. Players Grouped by Wins (GROUP BY)")
                print("3. Players with Gold Above Average (Sub-query)")
                print("4. High-Winning Players (HAVING)")
                print("5. All Players with Stats (LEFT OUTER JOIN)")

                subchoice = input("Enter your choice (1-5): ").strip()

                match subchoice:
                    case "1":
                        query_player_stats(conn)
                    case "2":
                        query_players_by_wins(conn)
                    case "3":
                        query_players_by_gold(conn)
                    case "4":
                        query_top_players(conn)
                    case "5":
                        query_all_players_with_stats(conn)
                    case _:
                        print("Invalid choice. Please try again.")
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
