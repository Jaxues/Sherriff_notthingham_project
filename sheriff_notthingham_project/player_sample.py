import random
from sheriff_scoring import Game
from sheriff_player import Player

"""
Testing scoring functionality for different player counts. With Random samples

"""


test_players = [
    Player("a"),
    Player("b"),
    Player("c"),
    Player("d"),
    Player("e"),
    Player("f"),
]
for score_player in test_players:
    (
        score_player.coins,
        score_player.num_apples,
        score_player.num_bread,
        score_player.num_cheese,
        score_player.num_chickens,
        score_player.num_contraband,
    ) = random.sample(range(0, 20), 6)
    score_player.num_legal_goods = (
        score_player.num_apples
        + score_player.num_bread
        + score_player.num_cheese
        + score_player.num_chickens
    )
    score_player.score = score_player.scoring()
#   score_player.score,score_player.coins,score_player.num_contraband,score_player.num_legal_goods=random.sample(range(0,20),4)


test_game = Game()
test_game.players = test_players
test_game.num_players = 6
test_game.appleking()
test_game.breadking()
test_game.cheeseking()
test_game.chickenking()
test_game.rankings()
