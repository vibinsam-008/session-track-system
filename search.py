def search_ses():
    s = input("Enter the subject")
    from data import study_log
    for session in study_log:
        if session["Subject"] == s:
            print("Session Number: ", session["Session no"])
            print("Subject: ", session["Subject"])
            print("Duration: ", session["Duration"])
            print("Focus Index: ", session["Focus index"])
            print("Completion Status: ", session["Status"])
