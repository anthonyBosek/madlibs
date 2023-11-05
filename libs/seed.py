#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import MadLib
from models.template import Template


def seed_database():
    Template.drop_table()
    Template.create_table()
    Template.create("Adventure", "The Quest for the Guardian", "Once upon a time, in a mysterious land far, far away, a brave adventurer named [1] set out on a quest to find the legendary [0]. The treasure was said to be hidden in a [5] guarded by a [8], rumored to be [6] and fearsome. With [4] companions by their side, armed with [7], [1] embarked on the perilous journey to reach the [5]. Along the way, they encountered [3] [8], each more curious and enchanting than the last. Despite facing numerous challenges, [1] remained determined, driven by the desire to discover the treasure. Their heart was filled with [9], and they never once [10] in their pursuit. As they finally arrived at the [5], the treasure was in sight, but a final [11] stood in their way. With a blend of courage, wits, and their trusty [7], [1] overcame the obstacle and claimed the legendary [0]. And so, the adventurer returned home victorious, with tales of their epic quest, proving that no challenge is too great when you have a determined spirit and loyal companions by your side.", ["treasure", "Adjective", "Verb", "Number", "Color", "Place", "Adjective", "Weapon", "Creature", "Emotion", "Verb (past tense)", "Obstacle"])


seed_database()
print("Seeded database")
