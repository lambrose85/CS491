"""boggle game using python"""

import random
import itertools
class Dice:

    myDice = [['A','E','A', 'N', 'E', 'G'], ['A', 'H', 'S', 'P', 'C', 'O'], ['A','S','P', 'F', 'F', 'K'], ['O','B','J', 'O', 'A', 'B'], ['I','O','T', 'M', 'U', 'C'], ['R','Y','V', 'D', 'E', 'L']
                , ['L','R','E', 'I', 'X', 'D'], ['E','I','U', 'N', 'E', 'S'], ['W','N','G', 'E', 'E', 'H'], ['L','N','H', 'N', 'R', 'Z'], ['T','S','T', 'I', 'Y', 'D'], ['O','W','T', 'O', 'A', 'T']
                , ['E','R','T', 'T', 'Y', 'L'], ['T','O','E', 'S', 'S', 'I'], ['T','E','R', 'W', 'H', 'V'], ['N','U','I', 'H', 'M', 'Qu']]

    def ran(self, x):
        for i in x:
            letter = random.randint(0,5)
            print(i[letter])
bog = Dice()
bog.ran(bog.myDice)

