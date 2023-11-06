from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import MadLib
from models.template import Template

# import ipdb
ml1 = Template(
    "Story",
    "Day in the Life",
    "Once upon a time in a far-off land, there lived a(n) [1] [2] named [Your Name]. One sunny morning, they woke up and [3] out of bed. The clock on the wall struck [4], and the room was bathed in a soft, [5] light.[Your Name] had a pet [6] named [6's Name], who eagerly awaited breakfast. [Your Name] fed [6's Name] a delicious meal of [7], and the [6] happily wagged its tail. Feeling [8], [Your Name] decided to go for a walk with [6's Name]. They strolled [9] through the [10], enjoying the fresh air and the beauty of nature. Suddenly, they spotted a colorful [5] butterfly fluttering by. [Your Name] reached out and touched it, feeling a sense of wonder. After the walk, they returned home and noticed a tiny scratch on their [11]. It must have happened during the adventure with the butterfly. [Your Name] decided to put on their favorite band's [12] and spent the rest of the day relaxing, feeling content and thankful for the little moments that made their life special.",
    [
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
ml2 = Template(
    "Adventure",
    "The Lost [1] of [6]",
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
ml3 = Template(
    "Adventure",
    "The Quest for the Guardian",
    "Once upon a time, in a mysterious land far, far away, a brave adventurer named [2] set out on a quest to find the legendary [1]. The treasure was said to be hidden in a [6] guarded by a [9], rumored to be [7] and fearsome. With [4] companions by their side, armed with [8], [2] embarked on the perilous journey to reach the [6]. Along the way, they encountered [4] [9], each more curious and enchanting than the last. Despite facing numerous challenges, [2] remained determined, driven by the desire to discover the treasure. Their heart was filled with [10], and they never once [11] in their pursuit. As they finally arrived at the [6], the treasure was in sight, but a final [12] stood in their way. With a blend of courage, wits, and their trusty [8], [2] overcame the obstacle and claimed the legendary [1]. And so, the adventurer returned home victorious, with tales of their epic quest, proving that no challenge is too great when you have a determined spirit and loyal companions by your side.",
    [
        "treasure",
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
ml5 = Template("category", "title", "text-for-the-madlib", ["pos_list"])
ml6 = Template("category", "title", "text-for-the-madlib", ["pos_list"])
ml7 = Template("category", "title", "text-for-the-madlib", ["pos_list"])
# ml4 = Template("Rap", "Boyz-in-the-hood", "Cruisin' down the street in my '64 Jockin' the freaks, clockin' the dough, Went to the park to get the scoop, Knuckleheads out there cold-shootin' some hoops, A car pulls up, who can it be?, A fresh El Camino rollin', Kilo G, He rolls down his window and he started to say, "It's all about makin' that GTA", 'Cause the boys in the hood are always hard, You come talkin' that trash, we'll pull your card, Knowin' nothin' in life, but to be legit, Don't quote me, boy, 'cause I ain't said shit", ["name of animal", "type of people", "type of people", "location", "type of people", "type of people", "mode of transportation", "a guy you know", "body part", "name a decease", "adjective", "verb ending in-ing", "noun", "adjective", "a name you give someone you don’t like", "curse word"])


def reset_database():
    pass


print("debugg")

reset_database()
# ipdb.set_trace()
