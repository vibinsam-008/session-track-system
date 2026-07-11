#Session as dictionary
#Study log as a list of Session
#1.Add Session
#2.View Session
#3.Search Subject
#4.Remove Session
#5.Productivity Report
#6.Daily Recommendation
#7.Exit

#This is a python program to make a early MVP of a student session tracker cum reporter.
import re
study_log = [ ]
i = 1
def add_ses():
    i = int(input("Enter session number"))
    s = input("Enter Subject")
    d = int(input("Enter study Duration in minutes"))
    f = int(input("Enter focus index (1 to 10)"))
    c = input("Completed").lower()
    
    session = {
        "Session no": i,
        "Subject": s,
        "Duration":d,
        "Focus index": f,
        "Status": c
    }
    avg = sum(session["Focus index"])/len(session["Focus index"])
    study_log.append(session)
    
def dis_ses():
    for session in study_log:
        print("Session ", i)
        print("Subject: ", session["Subject"])
        print("Duration: ", session["Duration"])
        print("Focus: ", session["Focus index"])
        print("Completed: ", session["Status"])
        i +=1

def search_ses():
    s = input("Enter the Subject")
    for session in range(len(study_log)):
        if s in study_log[i]:
            dis_ses()

def remove_ses():
    r = input("Enter session to be removed")
    for session in range(len(study_log)):
        if r == study_log[i]:
            study_log.remove(session)



def insights():
    print("total session:  ", len(session["Session no"]))
    print("Total study time: ", sum(session["Duration"]))
    print("Average focus: ", avg)
    print("Longest session: ", max(session["Subject"]))
    print(max(session["Duration"]))
    print("Most studied subject: ", max(len(session["Subject"])))
    print("Least studied subject: ", min(len(session["Subject"])))

print("1.Add session")
print("2.Display session")
print("3.Search Subject")
print("4.Remove session")
print("5.View Insights")
print("6.Exit")

while True:
    d = int(input("Enter menu no: "))
    if d == 1:
        add_ses()
    elif d == 2:
        dis_ses()
    elif d == 3:
        search_ses()
    elif d == 4:
        remove_ses()
    elif d == 5:
        insights()
    elif d == 6:
        break
    else:
        print("Invalid")
