while True:

    class student:

        def __init__(self,Name,Age,Grade):

            self.name = Name
            self.age = Age
            self.grade = Grade

        def score(self):

            if self.grade >= 70:
                print(f'{self.name} Has passed')
            else:
                print(f'{self.name} Has Failed ')

    class teacher(student):
            pass
     
    def put():
            
        pu = input('Enter Name, Age, Grade ')

        return pu


    for x in range(3):
        stud = {'Name':[],'Age':[],'Grade':[]}

        Astudent = student(put(),put(),put())

        stud['Name'][0].append(Astudent.name)
        stud['Age'][0].append(Astudent.age)
        stud['Grade'][0].append(Astudent.grade)
        
    print(stud)
    break

#Looking to add more to the dic by some how increase the numbers/location the variables are in.