#%%
import pyjokes
import random

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    reaction = random.choice(reactions)
    
    return reaction


def print_random_joke_and_reaction():
    joke = pyjokes.get_joke()
    reaction = get_random_reaction()
    joke_and_reaction = joke + reaction

    print(joke_and_reaction)


if __name__ == "__main__":
    print_random_joke_and_reaction()
#%%