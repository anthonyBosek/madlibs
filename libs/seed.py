#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import MadLib
from models.template import Template


def seed_database():
    Author.drop_table()
    Author.create_table()
    # Author.create()
    MadLib.drop_table()
    MadLib.create_table()
    # MadLib.create()
    Template.drop_table()
    Template.create_table()

    
    temp = Template.create("Adventure",
                    "The Quest for the Guardian",
                    "Once upon a time, in a mysterious land far, far away, a brave adventurer named [1] set out on a quest to find the legendary [0]. The treasure was said to be hidden in a [5] guarded by a [8], rumored to be [6] and fearsome. With [4] companions by their side, armed with [7], [1] embarked on the perilous journey to reach the [5]. Along the way, they encountered [3] [8], each more curious and enchanting than the last. Despite facing numerous challenges, [1] remained determined, driven by the desire to discover the treasure. Their heart was filled with [9], and they never once [10] in their pursuit. As they finally arrived at the [5], the treasure was in sight, but a final [11] stood in their way. With a blend of courage, wits, and their trusty [7], [1] overcame the obstacle and claimed the legendary [0]. And so, the adventurer returned home victorious, with tales of their epic quest, proving that no challenge is too great when you have a determined spirit and loyal companions by your side.", 
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
                        "Obstacle"
                        ])
    
    temp2 = Template.create("Misc.",
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
                        "Song title"
                    ]
                )
    
    temp3 = Template.create("Adventure",
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
                        "Obstacle"
                    ]
                )
     
    temp4 = Template.create("Sports",
                    "The Big Game",
                    "Once upon a time, in the world of [0], the [1] from [2] prepared for the most [3] match of the season. The star player, [4], was known for their incredible [5] skills. As the game began, the team quickly took the lead, scoring [6] points within the first few minutes. The crowd's excitement was palpable, and the stadium echoed with [9] cheers. With just seconds left on the clock, [4] dribbled the [9] down the court. The fate of the game rested in their hands. With a swift move, they made the final shot, and the team emerged victorious with a [9]! The celebrations were unforgettable, and the entire city rejoiced in the team's success. It was a day of triumph, and [4] became a sports legend.", 
                    [
                        "sport",
                        "team name,"
                        "city or location",
                        "adjective",
                        "athlete's name",
                        "action verb",
                        "number",
                        "emotion",
                        "peice of sports equipment",
                        "a result",
                    ]
                )
    
    temp5 = Template.create("Sports",
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
                        "piece of sports equipment"
                        "a result",
                    ]
                )
    
    temp6 = Template.create("Mystery",
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
                    ]
                )
    
    temp7 = Template.create("Adventure",
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
                    ]
                )
      
      
      



seed_database()
print("Seeded database")
