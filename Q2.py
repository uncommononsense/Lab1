def first():
    second()
    print("I am first")

def second():
    third()
    print("I am second")

def third():
    fourth()
    print("I am third")

def fourth():
    print("I am fourth")
    
first()
