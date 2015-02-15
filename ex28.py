__author__ = 'hash1'


from sys import exit

def gold_room():
    print "this room is full of gold"

    next = raw_input("what you want ?")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead ("lear to type a number")

    if how_much <50:
        print " you are not greed"
        exit(0)


def start():
    print " you are in a dark room where u want to go"

    input_given = raw_input("where u wanna go ?")

    if input_given == "left":
        print "slam"
        exit(0)
    else:
        gold_room()

def dead(mes):
    print "mess"
    exit(0)


start()
