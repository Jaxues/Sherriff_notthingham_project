from sheriff_scoring import Game
from sheriff_player import Player

# Strucutre
# Coins apples bread cheese chickens contraband


test_players = [Player("A"), Player("B"), Player("C")]
test_players[0].num_cheese = 10
test_players[1].num_cheese = 10
test_players[2].num_cheese = 10


test_players[0].num_bread = 10
test_players[1].num_bread = 10
test_players[2].num_bread = 10

test_players[0].num_apples = 10
test_players[1].num_apples = 10
test_players[2].num_apples = 10


test_players[0].num_chickens = 10
test_players[1].num_chickens = 10
test_players[2].num_chickens = 10



test_game = Game()
test_game.players = test_players
test_game.cheeseking()
test_game.appleking()
test_game.chickenking()
test_game.breadking()
test_game.rankings()
