# -*- coding: utf-8 -*-
"""
Author: Jennie Garcia
Description: First Poetry Generator
License: GNU General Public License v2
Date Created: Monday, September 3, 2018

"""

import random

random.seed()

# list of nouns
nouns = ["pup", "puppy", "doggy", "hound", "mutt", "pooch", "canine"]

verbs = ["guards", "defends", "assures", "looks after", "fends",
         "screens", "protects", "watches"]

adjectives = ["loyal", "devoted", "steadfast", "trustworthy", "attached",
             "unfailing", "unswerving"]


#i = 0
#
#for noun in nouns:
#    print nouns [i]
#    i = i + 1

#noun = random.choice(nouns)
#print noun 

noun = random.choice(nouns)

verb = random.choice(verbs)

adjective = random.choice(adjectives)

second_adjective = random.choice(adjectives)

second_noun = random.choice(nouns)
second_verb = random.choice(verbs)
second_adjective = random.choice(adjectives)

#word poem

#print "The" " " + adjective + " " + noun + " " + verb 
#
##for loop to iterate through verbs
#i = 1
#
#for verbs in verbs:
#    whitespace = " " * i
#    print whitespace + verb
#    i = i + 1
#    
##concatenation
#    print "The" " " + adjective + " " + noun + " " + verb

# string format
print "The {adj} {n} {v}" .format(adj=adjective, n=noun, v=verb)

print "while the {sec_adj} {sec_n} {sec_v}." .format(sec_adj=second_adjective,
                 sec_n=second_noun, sec_v=second_verb)



    
    