# 263_2026_02_Project_Template

This repo contains a template for the CSC 263 Final Project that you may use to
get started.

In order to do the example exercise outlined by the comments in the template,
read the following section.

## Doing the Template Exercise

The repository is split into two different directories:

- `template/` contains the template to be used by the exercise
- `example/` contains the answers to the exercise

The queries to be completed for the exercise live in `template/queries.sql`

To get started, clone this repo to the compsci server,
create a virtual environment, activate it, and install the
required libraries:

```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

#macOS / Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After setting up the environment, edit the database connection credentials in 
`template/app.py` to reflect your own (lines 18-24). You will only need to change
your username (match your compsci server username), and your database (match your
database name). Password will still be left blank.

Test your database connection by running `template/app.py`. If the connection does
not work, an error will be thrown. Otherwise, the connection was established and closed.

Once done, create the demo_players table in your database:

```sql
CREATE TABLE demo_players (
    ID varchar(20) PRIMARY KEY,
    Name varchar(100),
    Color varchar(50),
    Wins int,
    Losses int,
    Gold int
);

CREATE TABLE IF NOT EXISTS demo_scorelog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    LogDate DATE,
    PlayerID varchar(20),
    PlayerName varchar(100),
    Wins INT,
    Losses INT,
    Gold INT
);
```

With the table in place, you can start writing queries. Start with the queries
in `player_manager.py`, and test each one along the way by adding a menu option.
If you get stuck on a query, you may refer to its answer in `example/`.
