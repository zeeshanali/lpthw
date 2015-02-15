__author__ = 'hash1'


print "Lets Practice Everything"

print "you \'d need to know \'bout escape sequences that do \n lines and \t tabs"

poem = """
Allahu Akbar \n
Allahuakbar \n
La Ilaha illallah

Allahu akbar
Walilahil Hamd\n

"""

print "."*10
print poem
print "."*10


five = 10-2+3-6

print "this should be five %s" %five

def secret_formula(sec):
    j=sec*50
    k=sec*100
    return j,k
print " we can also do this way %s %s " % secret_formula(20)

