from sheriff_player import Player


class Game:
    def __init__(self):
        """
        Intialize setup of game
        """
        self.num_players = 0
        self.kings = dict()
        self.queens = dict()
        self.players = []
        self.score_goods = {
            "apples": (20, 10),
            "cheese": (15, 10),
            "bread": (15, 10),
            "chickens": (10, 5),
        }

    def addplayers(self):
        """
        add method for adding players
        """
        counter_players = 0
        num_players_valid = False
        while num_players_valid is False:
            num_players = input(
                "How many players are in the game (Between 3 and 6 players)"
            )
            if num_players.isdigit():
                if int(num_players) >= 3 and int(num_players) <= 6:
                    print(f"Setting up a {num_players} game")
                    self.num_players = int(num_players)
                    num_players_valid = True
                else:
                    print(
                        "Invalid number of players. Please enter number between 3 and 6"
                    )
            else:
                print(
                    "Invalid input. Must be integer between 3 and 6 players inclusive"
                )
        player_list = []

        while counter_players < self.num_players:
            player_name = input(f"Enter name of Player {counter_players + 1}: ")
            if player_name not in player_list:
                self.players.append(Player(player_name.title()))
                player_list.append(player_name)
                counter_players += 1
            else:
                print(f"Enter a non repeated name for player {counter_players + 1}")

    def scoreplayers(self):
        """
        Score all players in player list
        """
        for player in self.players:
            player.scoring()
        self.appleking()
        self.cheeseking()
        self.breadking()
        self.chickenking()
        self.rankings()

    def appleking(self):
        """
        Score winner of apple king and queen
        Apple king gets 20
        Apple queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king
        """
        apple_rankings = []
        apple_rankings = sorted(
            self.players, key=lambda player: player.num_apples, reverse=True
        )
        print(apple_rankings)
        for i in apple_rankings:
            print(i.name, i.num_apples)

        if apple_rankings[0].num_apples == 0:
            self.kings["apples"] = None
            self.queens["apples"] = None

        elif apple_rankings[0].num_apples == apple_rankings[2].num_apples:
            """
            Can only be 3 players if two tied for apple queen 
            """
            self.points_king_queen(apple_rankings, "apples", threeway_tied=True)

        elif apple_rankings[0].num_apples == apple_rankings[1].num_apples:
            """
            If both players tied for apple king
            """
            self.points_king_queen(apple_rankings, "apples", first_tied=True)

        elif apple_rankings[1].num_apples == apple_rankings[2].num_apples:
            """
            Can only be 3 players if two tied for apple queen 
            """
            self.points_king_queen(apple_rankings, "apples", second_tied=True)
        else:
            self.points_king_queen(apple_rankings, "apples")

    def cheeseking(self):
        """
        Score winner of  cheese king and queen
        cheese king gets 15
        cheese queen gets 10
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king

        Rankings is a list which has tuple for data.
        Tuple stores player object, name, and amount of cheese
        """
        cheese_rankings = sorted(
            self.players, key=lambda player: player.num_cheese, reverse=True
        )
        if cheese_rankings[0].num_cheese == 0:
            self.kings["cheese"] = None
            self.queens["cheese"] = None

        elif cheese_rankings[0].num_cheese == cheese_rankings[2].num_cheese:
            self.points_king_queen(cheese_rankings, "cheese", threeway_tied=True)

        elif cheese_rankings[0].num_cheese == cheese_rankings[1].num_cheese:
            """
            If both players tied for cheese king
            """
            self.points_king_queen(cheese_rankings, "cheese", first_tied=True)

        elif cheese_rankings[1].num_cheese == cheese_rankings[2].num_cheese:
            """
            Can only be 3 players if two tied for cheese queen 
            """
            self.points_king_queen(cheese_rankings, "cheese", second_tied=True)
        else:
            self.points_king_queen(cheese_rankings, "cheese")

    def breadking(self):
        """
        Score winner of  king and queen
        bread king gets 15
        bread queen gets 10
        Don't give out queen if tied for king
        """
        bread_rankings = sorted(
            self.players, key=lambda player: player.num_bread, reverse=True
        )
        if bread_rankings[0].num_bread == 0:
            self.kings["bread"] = None
            self.queens["bread"] = None
        elif bread_rankings[0].num_bread == bread_rankings[2].num_bread:
            """
            Can only be 3 players if two tied for queen 
            """
            self.points_king_queen(bread_rankings, "bread", threeway_tied=True)

        elif bread_rankings[0].num_bread == bread_rankings[1].num_bread:
            """
            If both players tied for bread king
            """
            self.points_king_queen(bread_rankings, "bread", first_tied=True)

        elif bread_rankings[1].num_bread == bread_rankings[2].num_bread:
            """
            Can only be 3 players if two tied for queen 
            """
            self.points_king_queen(bread_rankings, "bread", second_tied=True)
        else:
            self.points_king_queen(bread_rankings, "bread")

    def chickenking(self):
        """
        Score winner of  king and queen
        chicken king gets 10
        chicken queen gets 5
        For ties of King and Queen bonus
        Add number of players rounded down.
        Don't give out queen if tied for king
        """
        chicken_rankings = sorted(
            self.players, key=lambda player: player.num_chickens, reverse=True
        )

        if chicken_rankings[0].num_chickens == 0:
            """
            Case when all players have 0
            """
            self.kings["chickens"] = None
            self.queens["chickens"] = None
        elif chicken_rankings[0].num_chickens == chicken_rankings[2].num_chickens:
            """
            Can only be 3 players if two tied for chicken queen 
            """
            self.points_king_queen(chicken_rankings, "chickens", threeway_tied=True)

        elif chicken_rankings[0].num_chickens == chicken_rankings[1].num_chickens:
            """
            If both players tied for chicken king
            """
            self.points_king_queen(chicken_rankings, "chickens", first_tied=True)

        elif chicken_rankings[1].num_chickens == chicken_rankings[2].num_chickens:
            """
            Can only be 3 players if two tied for chicken queen 
            """
            self.points_king_queen(chicken_rankings, "chickens", second_tied=True)

        else:
            self.points_king_queen(chicken_rankings, "chickens")

    def points_king_queen(
        self, good_rankings, good, first_tied=None, second_tied=None, threeway_tied=None
    ):
        """
        Condense awarding points for king and queen to one function
        Assumes a maximum tie of 2 players per position.
        Possible for more than 2 way ties.
        Logic easy to expand but in terms of practicality very unlikely to happen

        good_rankings is sorted list of players by number of legal good that they have
        good is string for type of good e.g. 'apples','cheese','bread','chickens'.
        Also key of good dictionary so case is sensitive.

        tiedfirst is flag to award points if two players have same number.
        Points to tied king is rounded down sum of first and second points of goods
        Also not award queen for good according to rulebook for tied king

        tiedsecond is there is a player with most but two players have same amount of goods. Award points of half second points rounded down
        """
        first_points = self.score_goods[f"{good}"][0]
        second_points = self.score_goods[f"{good}"][1]
        first = good_rankings[0]
        second = good_rankings[1]
        third = good_rankings[2]
        if first_tied:
            print("Tied First")
            first_half = (first_points + second_points) // 2
            first.score += first_half
            second.score += first_half
            self.kings[f"{good}"] = (
                f"{first.name} and {second.name} are tied for king of {good} "
            )
            self.queens[f"{good}"] = f"No queen of {good}"
        elif second_tied:
            print("Tied Second")
            first.score += first_points
            self.kings[f"{good}"] = f"{first.name} is the king of {good}"
            self.queens[f"{good}"] = (
                f"{second.name} and {third.name} are tied for queen of {good} "
            )
        elif threeway_tied:
            print("Tied Third")
            points = (first_points + second_points) // 3
            first.score += points
            second.score += points
            third.score += points
            self.kings[f"{good}"] = (
                f"{first.name},{second.name},{third.name} are tied for king of good"
            )
            self.kings[f"{good}"] = None

        else:
            first.score += first_points
            second.score += second_points
            self.kings[f"{good}"] = f"{first.name} is the king of {good}"
            self.queens[f"{good}"] = f"{second.name} is the queen of {good}"

    def rankings(self):
        """
        Sorting players from 1st to last based on criteria from rulebook
        """
        ranked_players = sorted(
            self.players,
            key=lambda player: (
                player.score,
                player.coins,
                player.contraband,
                player.num_legal_goods,
            ),
            reverse=True,
        )
        print(ranked_players)
        print("\n" + "=" * 65)
        print("Score|Number of coins|Number of contraband| Number of legal goods")
        print("=" * 65)
        for player in ranked_players:
            print(
                player.name,
                player.score,
                player.coins,
                player.num_contraband,
                player.num_legal_goods,
            )
        for king, queen in zip(self.kings.values(), self.queens.values()):
            print(f"\n{king}\n{queen}")
        print(
            "\nName| Number of contraband| Number of apples| Number of cheese| Number of bread| Number of chickens"
        )
        for player in ranked_players:
            print(
                player.name,
                player.num_contraband,
                player.num_apples,
                player.num_cheese,
                player.num_bread,
                player.num_chickens,
            )
