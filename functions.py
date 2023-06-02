def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

hours = minutes_to_hours(120)
print(f"Hours are {hours}")


# Arbitrary Keyword Arguments
def arb(**keyword):
    """ Arbitrary Keyword Arguments Function Example """
    for k in keyword:
        print(k)
arb(a="a", b="b", c="c", d="d")

print(arb.__doc__)


# Anonymous Functions in Python
def fun():
    print("normal functions in Python")

fun_v2 = lambda: print("Annonymous Functions in Python")
fun()
fun_v2()


# Class and function with wildcard arguments
class car():
    def __init__(self, *argu):
        self.one = argu[0]
        self.two = argu[1]

audi = car(100, "red")
bmw = car(120, "green")

print(audi.one)
print(bmw.two)