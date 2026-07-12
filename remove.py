from data import study_log
def remove_ses():
    r = input("Enter the subject to be removed")
    j = int(input("Enter the session number to be removed"))

    for session in study_log:
        if session["Subject"] == r and session["Session no"] == j:
            study_log.remove(session)
            print("Session and its corresponding session number removed")
