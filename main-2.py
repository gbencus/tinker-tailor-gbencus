class TinkerTailor:

    def __init__(self, k=5, n=3):
        self.k = k
        self.n = n
        self.tinker = []

    def tinker_maker(self):
        for x in range(1, self.k + 1):
            self.tinker.append(x)

    def tinker_game(self):
        n = self.n - 1
        count = n
        print('This is the start: ', self.tinker)

        while len(self.tinker) > 1:
            self.tinker.pop(count)
            count = (count + n) % len(self.tinker)
        print('The winner is: ', self.tinker[0])

if __name__ == '__main__':
    game = TinkerTailor()
    game.tinker_maker()
    game.tinker_game()