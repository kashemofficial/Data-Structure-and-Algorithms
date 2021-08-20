class Student:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name

    def __eq__(self, other):
        return self.roll == other.roll and self.name == other.name

    def __hash__(self):
        print("The hash is : ",end="")
        return hash((self.roll,self.name))

if __name__ == '__main__':
    kashem = Student(165110,'MD Abul Kashem')
    helal = Student(165071,'Helal')
    tareq = Student(165108,'Tareq')
    print(hash(kashem))
    print(hash(helal))
    print(hash(tareq))
