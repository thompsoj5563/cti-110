# Test Average and Grade
# April 6, 2018
# CTI 110
# Jessica Thompson

def main():
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    score4 = int(input("Enter score 4: "))
    score5 = int(input("Enter score 5: "))


def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score) / 5
    
    return average

def determine_grade(score1, score2, score3, score4, score5):
    for i in score1, score2, score3, score4, score5:
        if i < 60:
            print ("F")
        elif i < 70:
            print ("D")
        elif i < 80:
            print ("C")
        elif i < 90:
            print ("B")
        elif i < 101:
            print ("A")

main()


average = calc_average(score1, score2, score3, score4, score5)
print("The average of the scores is: ", average)
determine_grade(score1, score2, score3, score4, score5)



