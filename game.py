import pickle

from settings import NUM_TOKENS, GEMS, WILD, CARDS_FILE, TILES_FILE
from components import Player, Token, Card, Tile
from manager import CardManager, TokenManager, TileManager


class Game:
    def __init__(self, num_players):
        self.players = []
        self.tokens = {gem: TokenManager() for gem in GEMS+WILD}
        self.cards = CardManager()
        self.tiles = TileManager()

        # create tokens
        num_tokens = NUM_TOKENS[num_players]
        for token in GEMS:
            for _ in range(num_tokens):
              self.tokens[token].register_item(Token())
        for _ in range(5):
            self.tokens[WILD].register_item(Token())

        # define the playing cards
        with open(CARDS_FILE, 'rb') as f:
            card_dataset = pickle.load(f)
        
        for card in card_dataset:
            self.cards.register_item(Card(*card))
        self.cards.shuffle()

        # define the tiles
        with open(TILES_FILE, 'rb') as f:
            tiles = pickle.load(f)
        
        for tile in tiles:
            self.tiles.register_item(Tile(*tile))

        tiles.shuffle()

        # add players
        for _ in range(num_players):
            self.players.append(Player())

        # set up first turn
        self.current_player = self.players[0]

        # set up four cards in play
        def f1(x): return x.owner == None
        for level in self.cards:
            self.cards[level].put_four_in_play([f1,])

        # run main loop
        self.play()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass

    def play(self):
        while not any(map(lambda x: ))
        for player in self.players:
            self.players[player].move()

        pass
