import pickle

from settings import NUM_TOKENS, GEMS, WILD, CARDS_FILE, TILES_FILE
from components import Player, Token, Card, Tile
from manager import CardManager, TokenManager, TileManager


class Game:
    def __init__(self, num_players):
        self.players = []
        self.tokens = TokenManager()
        self.cards = CardManager()
        self.tiles = TileManager()

        # create tokens
        num_tokens = NUM_TOKENS[num_players]
        for token in GEMS:
            for _ in range(num_tokens):
              self.tokens.register_item(Token(gem=token))
        for _ in range(5):
            self.tokens.register_item(Token(gem=WILD))

        # define the playing cards
        with open(CARDS_FILE, 'rb') as f:
            card_dataset = pickle.load(f)
        
        card_params = ("level", "gem", "cost", "prestige")
        for card in card_dataset:
            self.cards.register_item(Card(*zip(card_params, card)))
        self.cards.shuffle()

        # define the tiles
        with open(TILES_FILE, 'rb') as f:
            tiles = pickle.load(f)
        
        for tile in tiles:
            self.tiles.register_item(Tile(*tile))

        self.tiles.shuffle()

        # add players
        for _ in range(num_players):
            self.players.append(Player(self.tokens, self.cards, self.tiles))

        # set up first turn
        self.current_player = self.players[0]
        # self.cards.put_four_in_play()

        # run main loop
        # self.play()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass

    def play(self):
        for player in self.players:
            self.players[player].move()

        pass
