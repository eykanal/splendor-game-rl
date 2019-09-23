from settings import GEMS, WILD


class Player:
    def __init__(self):
        self.tiles = []
        self.num_turns_played = 0

    def prestige(self):
        card_prestige = sum([c.prestige for c in self.cards])
        tile_prestige = sum([t.prestige for t in self.tiles])
        return card_prestige + tile_prestige

    def card_counts(self):
        return list(self.cards.values())

    def play_turn(self):
        pass

    def _take_three_tokens(self, tokens, game):
        '''
        User chooses the "takes three tokens" action.

        Args:
            tokens: list of the three gem names (from settings.GEMS)
            game: instance of Game from which tokens should be taken

        Returns:
            game: updated Game instance
        '''
        for token in tokens:
            if game.tokens[token] == 0:
                raise RuntimeError('Requested token from empty stack')
            game.tokens[token] -= 1
            self.tokens[token] += 1
        return game

    def _take_two_tokens(self, token, game):
        '''
        User chooses the "takes two tokens" action.

        Args:
            tokens: string of chosen token (from settings.GEMS)
            game: instance of Game from which tokens should be taken

        Returns:
            game: updated Game instance
        '''
        if game.tokens[token] < 4:
            raise RuntimeError('Requested two token from stack of 3 or less')
        game.tokens[token] -= 2
        self.tokens[token] += 2
        return game

    def _take_card(self, card, game):
        pass

    def _discard_tokens(self):
        '''
        Called at the end of a turn, this discards tokens if the Player has
        more than the allowable number of tokens.
        '''


class Ownable:
    '''
    Base class for any game element which can shift ownership
    '''
    def __init__(self):
        self.owner = None


class Token(Ownable):
    def __init__(self, gem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gem = gem


class Card(Ownable):
    def __init__(self, level, gem, cost, prestige, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = level
        self.gem = gem
        self.cost = cost
        self.prestige = prestige
        self.in_hand = False
        self.in_play = False


class Tile(Ownable):
    def __init__(self, requirement, prestige, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requirement = requirement
        self.prestige = prestige
