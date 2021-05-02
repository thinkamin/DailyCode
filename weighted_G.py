def printG():
    print("""E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 -->F""")
    print(""" \                                         ^""")
    print("""  \                                        |""")
    print("""    ----------------- 3 -------------------- """)

G = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["F", 3]],
    "F": [],
}
# printG()
