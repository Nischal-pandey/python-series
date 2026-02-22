# Logic Truth Table Generator

def truth_table():
    print("A | B | A AND B | A OR B | NOT A | NOT B")
    print("-----------------------------------------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A} | {B} | {A and B}     | {A or B}    | {not A}   | {not B}")

truth_table()