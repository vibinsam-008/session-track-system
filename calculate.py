from data import study_log

def calc():
    total = 0
    fi = 0
    maximum = 0
    for session in study_log:
        total += session["Duration"]

        fi +=session["Focus index"]

        if session["Duration"] > maximum:
            maximum = session["Duration"]
    avg = fi/len(study_log)
    if len(study_log) == 0:
        return 0
    return total,maximum,avg

    
