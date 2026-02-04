class Player:
    def __init__(self, name):
        self.name = name
        self.num_apples = 0
        self.num_bread = 0
        self.num_cheese = 0
        self.num_chickens = 0
        self.contraband = False
        self.royal_goods = False
        self.coins = 0
        self.num_contraband = 0
        self.num_legal_goods = 0
        self.score = 0

    def score_coins(self):
        """
        Score players point for coins.
        Every $1 of coin is 1 victory point.
        So $5 is 5 vp, etc
        Coins also act for tie breaking for first and other positions.
        """
        denom = [1, 5, 20, 50]
        counter_coins = 0
        while counter_coins < 4:
            num_coins = input(
                f"How many ${denom[counter_coins]} coins does {self.name} have? "
            )
            if num_coins.isdigit():
                self.coins += denom[counter_coins] * int(num_coins)
                counter_coins += 1
            else:
                print(f"Please enter a valid number of coins for {self.name}")

    def scoring(self):
        """
        Score player for all legal goods they have.
        Also consider if they have contraband.
        Subset of contraband is royal goods
        """
        # tuple of tuples for good type and points per good
        legal_goods = (("apples", 2), ("cheese", 3), ("chickens", 4), ("bread", 3))
        counter_legal = 0
        amount_goods = []
        self.score_coins()
        self.score += self.coins
        while counter_legal < 4:
            if counter_legal % 2 == 0:
                num_legal = input(
                    f"How much {legal_goods[counter_legal][0]} does {self.name} have? "
                )
            elif counter_legal % 2 == 1:
                num_legal = input(
                    f"How many {legal_goods[counter_legal][0]} does {self.name} have? "
                )
            if num_legal.isdigit():
                self.score += legal_goods[counter_legal][1] * int(num_legal)
                self.num_legal_goods += int(num_legal)
                amount_goods.append(int(num_legal))
                counter_legal += 1
            else:
                print(f"Enter a valid number for {self.name}")
        self.num_apples, self.num_cheese, self.num_chickens, self.num_bread = (
            amount_goods
        )
        self.has_contraband()
        if self.contraband is True:
            self.contrabandscoring()
            if self.royal_goods is True:
                self.royal_scoring()

    def has_contraband(self):
        """
        Determines if player has any illegal goods.
        """
        determine_contraband = False
        while determine_contraband is False:
            has_counter = input(
                f"Does {self.name} have any contraband. Answer with y or n: "
            )
            if has_counter.lower() == "y":
                self.contraband = True
                determine_contraband = True
                self.has_royal()
            elif has_counter.lower() == "n":
                determine_contraband = True
            else:
                print("Please enter valid input")

    def has_royal(self):
        """
        Determines if player has any royal goods.
        A player must have smuggled contraband to have royal goods.
        But royal goods have additional scoring than standard contraband

        """
        determine_royal = False
        while determine_royal is False:
            has_counter = input(
                f"Does {self.name} have any royal goods. Answer with y or n: "
            )
            if has_counter.lower() == "y":
                self.royal_goods = True
                determine_royal = True
            elif has_counter.lower() == "n":
                determine_royal = True
            else:
                print("Please enter valid input")

    def contrabandscoring(self):
        """
        Contraband are hidden goods that are confusicated if bag is opened by sheriff. They are worth more points.

        Only has contraband from basegame of 2nd edition.
        """
        illegal_goods = (("Pepper", 6), ("Silks", 8), ("Mead", 7), ("Crossbows", 8))
        counter_illegal = 0
        while counter_illegal < 4:
            if counter_illegal % 2 == 0:
                num_illegal = input(
                    f"How many {illegal_goods[counter_illegal][0]} does {self.name} have? "
                )
            elif counter_illegal % 2 == 1:
                num_illegal = input(
                    f"How much {illegal_goods[counter_illegal][0]} does {self.name} have? "
                )
            if num_illegal.isdigit():
                num_illegal = int(num_illegal)
                self.score += illegal_goods[counter_illegal][1] * num_illegal
                self.num_contraband += num_illegal
                counter_illegal += 1
            elif not num_illegal.isdigit():
                print("Enter valid number for {self.name}")

    def royal_scoring(self):
        """
        Royal goods are subset of contraband that also count as additonal legal goods.
        """
        counter_royal = 0
        type_royal = ""
        royal_goods = (
            ("Green Apples", 4, 2),
            ("Gouda Cheese", 6, 2),
            ("Rye Bread", 6, 2),
            ("Golden Apples", 6, 3),
            ("Blue Cheese", 9, 3),
            ("Pumpernickel Bread", 9, 3),
            ("Royal Roosters", 8, 2),
        )
        while counter_royal < 7:
            if counter_royal % 7 == 0 or counter_royal % 7 == 3:
                num_royal = input(
                    f"How many {royal_goods[counter_royal][0]} does {self.name} have? "
                )
                type_royal += "apples"
            elif counter_royal % 7 == 1 or counter_royal % 7 == 4:
                num_royal = input(
                    f"How much {royal_goods[counter_royal][0]} does {self.name} have? "
                )
                type_royal += "cheese"

            elif counter_royal % 7 == 2 or counter_royal % 7 == 5:
                num_royal = input(
                    f"How much {royal_goods[counter_royal][0]} does {self.name} have? "
                )
                type_royal = "bread"

            elif counter_royal % 7 == 6:
                num_royal = input(
                    f"How many {royal_goods[counter_royal][0]} does player have? "
                )
                type_royal = "chickens"
            if num_royal.isdigit():
                num_royal = int(num_royal)
                self.score += royal_goods[counter_royal][1] * num_royal
                if type_royal == "apples":
                    self.num_apples += royal_goods[counter_royal][2]
                elif type_royal == "cheese":
                    self.num_cheese += royal_goods[counter_royal][2]
                elif type_royal == "bread":
                    self.num_bread += royal_goods[counter_royal][2]
                elif type_royal == "chickens":
                    self.num_chickens += royal_goods[counter_royal][2]
                type_royal = ""
                counter_royal += 1
            else:
                print(f"Enter valid number of royal goods for {self.name}")
