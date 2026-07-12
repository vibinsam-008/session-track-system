from data import study_log
from calculate import calc
def insight():
    total,maximum,avg = calc()
    print("Total no of session: ", len(study_log))
    print("Total Focus Duration: ", total)
    print("Longest session: ", maximum)
    print("Average Focus: ", avg)
