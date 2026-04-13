def query_player_stats(conn):
    """Query player statistics using GetPlayerStats stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Player Statistics ---")

    cur.callproc("GetPlayerStats")

    for result in cur.stored_results():
        stats = result.fetchone()
        print(f"\nTotal Players: {stats['TotalPlayers']}")
        print(f"Total Wins: {stats['TotalWins']}")
        print(f"Total Losses: {stats['TotalLosses']}")
        print(f"Average Gold: {stats['AverageGold']:.2f}")
        print(f"Max Wins by a Player: {stats['MaxWins']}")

    cur.close()


def query_players_by_wins(conn):
    """Query players grouped by wins using GROUP BY.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Players Grouped by Wins ---")

    cur.execute("""
        SELECT ID, Name, Wins, Losses, (Wins + Losses) as TotalGames, Color
        FROM demo_players
        GROUP BY Wins
        ORDER BY Wins DESC
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Color':<15} {'Wins':<8} {'Losses':<8} {'Total Games':<12}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Color']:<15} {row['Wins']:<8} {row['Losses']:<8} {row['TotalGames']:<12}"
        )

    cur.close()


def query_players_by_gold(conn):
    """Query players with gold above average using a sub-query.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Players with Gold Above Average ---")

    cur.execute("""
        SELECT ID, Name, Gold, (SELECT AVG(Gold) FROM demo_players) as AvgGold
        FROM demo_players
        WHERE Gold > (SELECT AVG(Gold) FROM demo_players)
        ORDER BY Gold DESC
    """)

    print(f"{'ID':<15} {'Name':<20} {'Gold':<8} {'Avg Gold':<10}")
    print("-" * 60)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Gold']:<8} {row['AvgGold']:<10.2f}"
        )

    cur.close()


def query_top_players(conn):
    """Query players using HAVING clause.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- High-Winning Players (HAVING) ---")

    cur.execute("""
        SELECT ID, Name, Wins, Losses, Gold, (Wins + Losses) as TotalGames
        FROM demo_players
        GROUP BY ID, Name, Wins, Losses, Gold
        HAVING Wins > 20
        ORDER BY Wins DESC
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Wins':<8} {'Losses':<8} {'Gold':<8} {'Total Games':<12}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Wins']:<8} {row['Losses']:<8} {row['Gold']:<8} {row['TotalGames']:<12}"
        )

    cur.close()


def query_all_players_with_stats(conn):
    """Query all players with statistics using LEFT OUTER JOIN.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- All Players with Stats (LEFT OUTER JOIN) ---")

    cur.execute("""
        SELECT p.ID, p.Name, p.Color, p.Wins, p.Losses, p.Gold,
               s.AvgWins as OverallAvgWins
        FROM demo_players p
        LEFT OUTER JOIN (
            SELECT AVG(Wins) as AvgWins
            FROM demo_players
        ) s ON 1=1
        ORDER BY p.Name
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Color':<15} {'Wins':<8} {'Losses':<8} {'Gold':<8} {'Avg Wins':<10}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Color']:<15} {row['Wins']:<8} {row['Losses']:<8} {row['Gold']:<8} {row['OverallAvgWins']:<10.2f}"
        )

    cur.close()
