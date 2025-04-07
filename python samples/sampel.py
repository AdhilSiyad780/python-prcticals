def calculate_informatics1_grade(bool1,bool2,ass1,ass2,lppt,lecturexam,bonuspt):
    practical = ass1+ass2+lppt
    total = 0
    grade = 0
    if bool1==False:
        return   "​​​​As you didn't submit Assignment 1, you were deregistered from the course and receive no grade."

    elif bool2==False:
        return "​​​​As you didn't submit Assignment 2, your Informatics 1 grade is 5."
    elif lppt <= 7.5:
        return "​​​​As you didn't passed the Lecture Exam, your Informatics 1 grade is 5."
    elif  practical>50:
        result = practical+bonuspt
        if result > 85:
            result = 85
        total = result+lecturexam
    elif practical < 50:

        if total>=90:
            grade = 1
        elif total <90 and total>80:
            grade = 2
        elif total <80 and total>65:
            grade = 3
        elif total <65 and total>50:
            grade = 4
        elif total < 50:
            grade = 5

    return grade
    
    
    

   
  



    
    

is_ass1_submitted = False
is_ass2_submitted = False
val1 = input('have you submitted the first assigment : y for YES  n for NO ')
if val1 == 'y':
    is_ass1_submitted = True
elif val1 == 'n':
    is_ass1_submitted == False
else:
    print('enter a valid input')
# ------------------------------------------------
val2 = input('have you submitted the second assigment : y for YES  n for NO ')
if val2 == 'y':
    is_ass2_submitted = True
elif val2 == 'n' :
    is_ass2_submitted == False
else:
    print('enter a valid input')
# -----------------------------------------------
ass1_points = int(input('enter the first assigment points'))
ass2_points = int(input('enter the second assigment points'))
lp_points = int(input(' enter The points received for the Live Programming'))
exam_points =int(input('enter the exam points'))
bonus_points = int(input('enter the bonus point'))



print(calculate_informatics1_grade(is_ass1_submitted,is_ass2_submitted,ass1_points,ass2_points,lp_points,exam_points,bonus_points))        