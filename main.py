
from scripts_of_tribute.game import Game
from RandomBot import RandomBot


def main():
    bot1 = RandomBot(bot_name="RandomBot1")
    bot2 = RandomBot(bot_name="RandomBot2")

    game = Game()
    game.register_bot(bot1)
    game.register_bot(bot2)

    for i in range(10):
        game.run(
            bot1.bot_name,
            bot2.bot_name,
            start_game_runner=True,
            runs=32,
            threads=4,
        )


if __name__ == "__main__":
    main()