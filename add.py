from data import study_log
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
    study_log.append(session)
