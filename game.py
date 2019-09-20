import pickle

from settings import NUM_TOKENS, GEMS, WILD, CARDS_FILE, TILES_FILE
from components import Player, Token, Card, Tile
from manager import ItemManager


class Game:
    def __init__(self, num_players):
        self.players = []
        self.tokens = {gem: ItemManager() for gem in GEMS+WILD}
        self.cards = {}
        self.tiles = ItemManager()

        # create tokens
        num_tokens = NUM_TOKENS[num_players]
        for token in GEMS:
            for _ in range(num_tokens)
            self.tokens[token].register_item(Token())
        for _ in range(5):
            self.tokens[WILD].register_item(Token())

        # define the playing cards
        with open(CARDS_FILE, 'rb') as f:
            card_dataset = pickle.load(f)
        
        for level in card_dataset:
            self.cards[level] = ItemManager()
            for c in level:
                self.cards[level].register_item(Card(level=c[0], gem=c[1], cost=c[2], prestige=c[3]))

        for level in self.cards:
            # TODO: up to here, continue refactoring to use ItemManager features
            random.shuffle(self.cards[level])

        # define the tiles
        with open(TILES_FILE, 'rb') as f:
            tiles = pickle.load(f)
        
        for tile in tiles:
            self.tiles.append(Tile(*tile))

        random.shuffle(self.tiles)

        # add players
        for _ in range(num_players):
            self.players.append(Player())

        # set up first turn
        self.current_player = self.players[0]

        # set up currently shown cards


        self.take_turn()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass

    def take_token(self, gem):
        '''
        Method for Player to get a token

        Args:
            gem: string of Gem to take (must exist in settings.GEMS)

        returns True if token can be taken, False if otherwise
        '''
        if self.tokens[gem] ≤ 0:
            return False
        self.tokens[gem] -= 1
        return True

    def return_token(self, gem):


    def take_turn(self):
        pass
