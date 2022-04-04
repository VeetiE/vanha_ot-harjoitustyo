```mermaid
classDiagram
	Player "*" --> "1" Gameboard
	class Player{
		id
		pawn
		moneyamount
	}
	class Gameboard{
	}
