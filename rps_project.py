import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class repeatPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayre(Player):
    def move(self):
        move = input("Please choose Rock, Paper, Scissors:").lower()
        while move not in moves:
            print("That's not a valid play. Check your spelling!\n")
            move = input("Please choose Rock,  Paper, or Scissors: ").lower()
        return move


class RflecetPlayer(Player):

    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return "rock"
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == "rock" and move2 == "scissors":
            self.count1 += 1
            print(f"P1 score:{self.count1}\t P2 score:{self.count2}")
        elif move1 == "scissors" and move2 == "rock":
            self.count2 += 1
            print(f"P1 score:{self.count1}\t P2 score: {self.count2}")
        elif move1 == "scissors" and move2 == "paper":
            self.count1 += 1
            print(f"P1 score:{self.count1}\t P2 score: {self.count2}")
        elif move1 == "paper" and move2 == "scissors":
            self.count2 += 1
            print(f"P1 score:{self.count1}\t P2 score: {self.count2}")
        elif move1 == "paper" and move2 == "rock":
            self.count1 += 1
            print(f"P1 score:{self.count1}\t P2 score: {self.count2}")
        elif move1 == "rock" and move2 == "paper":
            self.count2 += 1
            print(f"P1 score:{self.count1}\t P2 score: {self.count2}")
        else:
            print("TIE!!")

    def single_round(self):

        print("Welcome, Game Start!!")
        for round in range(1):
            print(f"Round{round}:")
            self.play_round()
        print("Game over! \n Good Bye")

    def play_game(self):
        rounds = int(input("Please write, How many rounds you want to play:"))
        print(" Welcome, Game start!")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over! \n Good Bye")


if __name__ == '__main__':
    while True:
        stratagy = input(
            "Please Choose a player stratagy from this\n" +
            "Repeat, Random, Reflect and Cycle:\n").lower()
        if stratagy == "repeat":
            while True:
                round = input("Please choose single round or several round:\n")
                if round == "single round":
                    game = Game(HumanPlayre(), repeatPlayer())
                    game.single_round()
                    break
                elif round == "several round":
                    game = Game(HumanPlayre(), repeatPlayer())
                    game.play_game()
                    break
            break

        if stratagy == "random":
            while True:
                round = input("Please choose single round or several round:\n")
                if round == "single round":
                    game = Game(HumanPlayre(), RandomPlayer())
                    game.single_round()
                    break
                elif round == "several round":
                    game = Game(HumanPlayre(), RandomPlayer())
                    game.play_game()
                    break
            break

        if stratagy == "reflect":
            while True:
                round = input("Please choose single round or several round:\n")
                if round == "single round":
                    game = Game(HumanPlayre(), RflecetPlayer())
                    game.single_round()
                    break
                elif round == "several round":
                    game = Game(HumanPlayre(), RflecetPlayer())
                    game.play_game()
                    break
            break

        if stratagy == "cycle":
            while True:
                round = input("Please choose single round or several round:\n")
                if round == "single round":
                    game = Game(HumanPlayre(), CyclePlayer())
                    game.single_round()
                    break
                elif round == "several round":
                    game = Game(HumanPlayre(), CyclePlayer())
                    game.play_game()
                    break
            break
        if stratagy == "exit":
            break
