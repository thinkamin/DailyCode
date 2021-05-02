G = {'A':['B','C'],
     'B':['A','D','E'],
     'C':['A','F'],
     'D':['B'],
     'E':['B','F'],
     'F':['C','E']}
def printG():
    print('''
            A-B-D
            | |
            C E
            |/   
            F
            ''')
