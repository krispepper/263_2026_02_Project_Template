-- Create the demo_players table
CREATE TABLE demo_players (
    ID varchar(20) PRIMARY KEY,
    Name varchar(100),
    Color varchar(50),
    Wins int,
    Losses int,
    Gold int
);

-- Stored procedure to update a player's score (Wins)
DELIMITER //
CREATE PROCEDURE UpdatePlayerScore(IN player_id varchar(20), IN new_wins int)
BEGIN
    -- Write SQL statement to update player's Wins
    -- Use the player_id and new_wins parameters
    -- Update the demo_players table
END //
DELIMITER ;

-- Stored procedure to query player statistics
DELIMITER //
CREATE PROCEDURE GetPlayerStats()
BEGIN
    -- Write a SELECT query that returns:
    -- COUNT(*) as TotalPlayers
    -- SUM(Wins) as TotalWins
    -- SUM(Losses) as TotalLosses
    -- AVG(Gold) as AverageGold
    -- MAX(Wins) as MaxWins
    -- Query from the demo_players table
END //
DELIMITER ;

-- Create log table for nightly batch process
-- This table will store end of day score logs
CREATE TABLE IF NOT EXISTS demo_scorelog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    LogDate DATE,
    PlayerID varchar(20),
    PlayerName varchar(100),
    Wins INT,
    Losses INT,
    Gold INT
);

-- Stored procedure for nightly batch process - log end of day scores
DELIMITER //
CREATE PROCEDURE LogEndOfDayScores()
BEGIN
    -- Write an INSERT statement that:
    -- - Inserts into demo_scorelog table
    -- - Gets LogDate from CURDATE()
    -- - Gets all players with high wins (e.g., Wins > 20)
    -- - Reads those players from the demo_players table
    -- - Records PlayerID, PlayerName, Wins, Losses, and Gold
END //
DELIMITER ;

-- Insert sample data
INSERT INTO demo_players (ID, Name, Color, Wins, Losses, Gold) VALUES
-- Add 25 sample player records here with:
-- - Unique IDs (P001-P025)
-- - Player names
-- - Colors (Red, Blue, Green, Yellow, Purple, Orange, Black, Pink)
-- - Wins, Losses, and Gold values
('P001', 'Sample Name 1', 'Red', 15, 8, 450);
