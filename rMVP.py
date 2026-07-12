from add import add_ses
from display import dis_ses
from search import search_ses
from calculate import calc
from insights import insight

print("1.Add session")
print("2.Display session")
print("3.Remove session")
print("4.Search subject")
print("5.View insights")
print("6.Exit")

while True:
    d = int(input("Enter menu number"))
    if d == 1:
        add_ses()
    elif d == 2:
        dis_ses()
    elif d == 3:
        remove_ses()
    elif d == 4:
        search_ses()
    elif d == 5:
        insight()
    elif d == 6:
        break
    else:
        print("Invalid menu option")
