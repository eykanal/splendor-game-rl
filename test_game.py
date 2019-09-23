import unittest

from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game_2 = Game(2)
        self.game_3 = Game(3)
        self.game_4 = Game(4)

    def test_assert_correct_num_tokens(self):
        self.game_2.TokenManager

    def test_player_take_three_tokens(self):
        player1 = self.game_3.players[0]
        game_3 = player1._take_three_tokens(['diamond', 'emerald', 'onyx'], self.game_3)
        self.assertEqual(game_3.players[0].tokens,
                         {'diamond': 1, 'emerald': 1, 'onyx': 1, 'ruby': 0, 'sapphire': 0, 'gold': 0})
        self.assertEqual(game_3.tokens,
                         {'diamond': 4, 'emerald': 4, 'onyx': 4, 'ruby': 5, 'sapphire': 5, 'gold': 5})

if __name__ == '__main__':
    unittest.main()
