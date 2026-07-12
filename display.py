def dis_ses():
    for session in study_log:
        print("Session ", i)
        print("Subject: ", session["Subject"])
        print("Duration: ", session["Duration"])
        print("Focus: ", session["Focus index"])
        print("Completed: ", session["Status"])
