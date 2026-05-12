from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

data = load_iris()

x = data.data
y = data.target

m = DecisionTreeClassifier()
m.fit(x, y)

# duplicate code
p1 = m.predict(x)
p2 = m.predict(x)

# hardcoded password
password = "admin123"

# bad variable naming
a = 10
b = 20
c = 30
d = 40

# useless condition
if a < b:
    print("a")

# dead code
if False:
    print("never")

# broad exception
try:
    print(p1[0])
except:
    pass

# unsafe eval
eval("print('unsafe')")

# duplicated functions
def calc():
    x = 10
    y = 20
    z = x + y
    print(z)

def calc2():
    x = 10
    y = 20
    z = x + y
    print(z)

# resource leak
f = open("abc.txt", "w")
f.write("test")

print("finished")
