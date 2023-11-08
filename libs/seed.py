#!/usr/bin/env python3

from models.author import Author
from models.madlib import MadLib
from models.template import Template

# from rich.console import Console


def seed_database():
    Author.drop_table()
    Author.create_table()
    MadLib.drop_table()
    MadLib.create_table()
    Template.drop_table()
    Template.create_table()

    # seed authors
    Author.create("Alberto", "Sierra")
    Author.create("Austin", "Ohlfs")
    Author.create("Anthony", "Bosek")

    # seed templates
    Template.create(
        "Fantasy",
        "The Quest for the Guardian",
        "Once upon a time, in a mysterious land far, far away, a brave adventurer named [Author] set out on a quest to find the legendary [0]. The treasure was said to be hidden in a [1] guarded by a [2], rumored to be [3] and fearsome. With [4] companions by their side, armed with a [5], [Author] embarked on the perilous journey to reach the treasure. Along the way, they encountered [6] [7], each more curious and enchanting than the last. Despite facing numerous challenges, [Author] remained determined, driven by the desire to discover the treasure. Their heart was filled with [8], and they never once [9] in their pursuit. As they finally arrived, the treasure was in sight, but a final [10] stood in their way. With a blend of courage, wits, and their trusty [11], [Author] overcame the obstacle and claimed the legendary treasure. And so, the adventurer returned home victorious, with tales of their epic quest, proving that no challenge is too great when you have a determined spirit and loyal companions by your side.",
        [
            "Treasure",
            "Place",
            "Creature",
            "Adjective",
            "Number",
            "Weapon",
            "Adjective",
            "Noun",
            "Emotion",
            "Verb (past tense)",
            "Obstacle",
            "Noun",
        ],
    )
    Template.create(
        "Fairy Tale",
        "Day in the Life",
        "Once upon a time in a far-off land, there lived a(n) [1] [2] named [Your Name]. One sunny morning, they woke up and [3] out of bed. The clock on the wall struck [4], and the room was bathed in a soft, [5] light.[Your Name] had a pet [6] named [6's Name], who eagerly awaited breakfast. [Your Name] fed [6's Name] a delicious meal of [7], and the [6] happily wagged its tail. Feeling [8], [Your Name] decided to go for a walk with [6's Name]. They strolled [9] through the [10], enjoying the fresh air and the beauty of nature. Suddenly, they spotted a colorful [5] butterfly fluttering by. [Your Name] reached out and touched it, feeling a sense of wonder. After the walk, they returned home and noticed a tiny scratch on their [11]. It must have happened during the adventure with the butterfly. [Your Name] decided to put on their favorite band's [12] and spent the rest of the day relaxing, feeling content and thankful for the little moments that made their life special.",
        [
            "",
            "Adjective",
            "Noun",
            "Verb past tense",
            "Number",
            "Color",
            "Animal",
            "Food",
            "Emotion",
            "Adverb",
            "Place",
            "Body par",
            "Song title",
        ],
    )
    Template.create(
        "Adventure",
        "The Lost Treasure",
        "Once upon a time, in a [7] land far, far away, a brave adventurer named [2] set out on a quest to find the lost [1]. The treasure was said to be hidden in a [6] guarded by a [9], rumored to be [2] and fearsome. With [4] companions by their side, armed with [8], [2] embarked on the [3] journey to reach the [6]. Along the way, they encountered [4] [9], each more curious and enchanting than the last. Despite facing numerous challenges, [2] remained determined, driven by the desire to discover the treasure. Their heart was filled with [10], and they never once [11] in their pursuit. As they finally arrived at the [6], the treasure was in sight, but a final [12] stood in their way. With a blend of courage, wits, and their trusty [8], [2] overcame the obstacle and claimed the lost [1]. And so, the adventurer returned home victorious, with tales of their epic quest, proving that no challenge is too great when you have a determined spirit and loyal companions by your side.",
        [
            "Treasure",
            "Adjective",
            "Verb",
            "Number",
            "Color",
            "Place",
            "Adjective",
            "Weapon",
            "Creature",
            "Emotion",
            "Verb (past tense)",
            "Obstacle",
        ],
    )
    Template.create(
        "Sports",
        "The Big Game",
        "Once upon a time, in the world of [0], the [1] from [2] prepared for the most [3] match of the season. The star player, [4], was known for their incredible [5] skills. As the game began, the team quickly took the lead, scoring [6] points within the first few minutes. The crowd's excitement was palpable, and the stadium echoed with [9] cheers. With just seconds left on the clock, [4] dribbled the [9] down the court. The fate of the game rested in their hands. With a swift move, they made the final shot, and the team emerged victorious with a [9]! The celebrations were unforgettable, and the entire city rejoiced in the team's success. It was a day of triumph, and [4] became a sports legend.",
        [
            "sport",
            "team name," "city or location",
            "adjective",
            "athlete's name",
            "action verb",
            "number",
            "emotion",
            "peice of sports equipment",
            "a result",
        ],
    )
    Template.create(
        "Sports",
        "The Championship Match",
        "Once upon a time, in the world of [0], the [1] from [2] were gearing up for the [3] championship match. The star player, [4], was known for their incredible [5] skills. The tension was high as the match began. Both teams gave their all, aiming to secure the victory. The crowd held its breath, eagerly watching the game. In the final moments, with the score tied at [6], [4] stepped up to the challenge. They used their remarkable [5] abilities to seize the moment and, with a powerful strike, brought their team to victory. The stadium erupted in [7] cheers as the team celebrated their [9]. The city celebrated this thrilling win for days, and [4] became a hero among sports fans. It was a moment of triumph, marking the team's place in history.",
        [
            "sport",
            "team name",
            "location",
            "adjective",
            "athlete's name",
            "action verb",
            "number",
            "emotion",
            "piece of sports equipment",
            "a result",
        ],
    )
    Template.create(
        "Mystery",
        "Mystery in the Old Manor",
        "Once upon a time, in an eerie old manor, a curious investigator named [0] decided to explore the place. The manor was known for its [1] atmosphere and [2] history. [0] was equipped with their trusty [3] and a determination to uncover the secrets hidden within. As they ventured deeper into the manor, they discovered [4] [5] that hinted at a long-forgotten story. The clues led [0] to a hidden [6] that was said to hold the key to the mystery. With a sense of [7], they unlocked the door and were met with a surprising revelation. It turned out that [9] had been hiding in the manor all along. In the end, [0] left the manor with a newfound sense of [9] and a tale of an extraordinary discovery.",
        [
            "Noun",
            "Adjective",
            "Noun",
            "Weapon",
            "Noun",
            "Noun",
            "Noun",
            "Emotion",
            "Noun",
            "Emotion",
        ],
    )
    Template.create(
        "Adventure",
        "A Magical Encounter",
        "In a world of enchantment, a young [0] with a heart full of [1] set out on a journey to find [2], the fabled [4]. Guided by a [4] [5], [0] traversed through the mystical [6], where they encountered [7] creatures that spoke in riddles. With the help of their magical [8], [0] unraveled the mysteries and grew closer to their goal. At the heart of the [6], they faced a powerful [9] and, with unwavering determination, [0] [10] the magical [3]. As they returned to their village, the people celebrated their courage and the wonder of the [2].",
        [
            "Noun",
            "Emotion",
            "Noun",
            "Noun",
            "Adjective",
            "Noun",
            "Place",
            "Noun",
            "Noun",
            "Noun",
            "Verb (past tense)",
        ],
    )
    
    Template.create(
    "Avatar",
    "The Elemental Journey",
    "In a world divided into four nations, a young [0] named [1] discovered their extraordinary ability to [2]. With the guidance of a wise [3], [1] embarked on a quest to master the art of [2]. Along the way, they encountered a [4] [5] who became their loyal companion. Together, they traveled through the [6] landscapes of the [7] Nation, facing challenges and meeting intriguing characters. As they honed their skills, [1] also learned about the ancient prophecy of the [8] and their role in restoring balance to the world. With determination in their heart and the power of [2] at their fingertips, [1] faced the formidable [9], an evil force threatening to plunge the world into chaos. With the support of newfound friends and the wisdom of their mentor, [1] confronted the darkness and emerged victorious, proving that even the most unexpected heroes can change the course of destiny and bring peace to a war-torn world.",
    [
        "bender type (e.g., waterbender, earthbender, firebender, airbender)",
        "character name",
        "bend an element (e.g., bend water, bend fire)",
        "element (e.g., water, earth, fire, air)",
        "mythical creature (e.g., dragon, spirit)",
        "creature's name",
        "geographical feature (e.g., mountains, forests, deserts)",
        "elemental nation (e.g., Water Tribe, Earth Kingdom, Fire Nation, Air Nomads)",
        "ancient artifact",
        "villain's name",
    ],
)

    # seed madlibs
    MadLib.create(
        [
            "white glove",
            "Neverland Ranch",
            "Bubbles the Monkey",
            "dirty",
            "777",
            "foam finger",
            "shadowy",
            "McDonalds",
            "anger",
            "elated",
            "road kill",
            "rain cloud",
        ],
        3,
        1,
    )
    MadLib.create(
        [
            "pop-tarts",
            "Wisconsin",
            "cave troll",
            "wooly",
            "17",
            "pool noodle",
            "slippery",
            "cacti",
            "angst",
            "slept",
            "chainlink fence",
            "line cook",
        ],
        3,
        2,
    )
    MadLib.create(
        [
            "white glove",
            "Neverland Ranch",
            "Bubbles the Monkey",
            "dirty",
            "777",
            "foam finger",
            "shadowy",
            "McDonalds",
            "anger",
            "elated",
            "road kill",
            "rain cloud",
        ],
        1,
        4,
    )
    MadLib.create(
        [
            "pop-tarts",
            "Wisconsin",
            "cave troll",
            "wooly",
            "17",
            "pool noodle",
            "slippery",
            "cacti",
            "angst",
            "slept",
            "chainlink fence",
            "line cook",
        ],
        2,
        6,
    )


# seed database
seed_database()
print("Seeded database")
