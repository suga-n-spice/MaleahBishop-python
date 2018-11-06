def main():
    print('hi')
    numClasses = input('How many classes are you in?')
    gradeList = []
    for i in range(0,int(numClasses)):
        x = input('What was your grade?')
        gradeList.append(int(x))
    print(gradeList)
    gpa = getGPA(gradeList,int(numClasses))
    print('your GPA is ' + str(gpa))

#     grade = input('What grade are you in highschool?')
#     getYearinschool(grade)
#     print(gpa)
#     getLetterGrade(gpa)

# def getYearinschool(grade):
#     if grade == '9':
#         print('You are a freshman')
#     elif grade == '10':
#         print('You are a sophomore')
#     elif grade == '11':
#         print('You are a junior')
#     elif grade == '12':
#         print('You are a senior')
#     else:
#         print('You are not in highschool')
#
def getGPA(grades,number):
    sum = 0.0
    for i in grades:
         sum = sum + int(i)
    return sum/number

# def getLetterGrade(gpa):
#     if gpa >= 92.5:
#         print('You have an A')
#     elif gpa > 80:
#         print('You have a B')
#     elif gpa > 70:
#         print('You have a C')
#     elif gpa > 60:
#         print('You have a D')
#     else:
#         print('You are failing')
#     return gpa

main()
