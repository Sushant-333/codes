class student:
    li = []  

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def accept(self, name, roll):
        ob = student(name, roll)
        student.li.append(ob)

    def dis(self, ob):
        print("Name:", ob.name, "Roll:", ob.roll)

    def up(self, roll, r):
        for i in range(len(student.li)):
            if student.li[i].roll == roll:
                student.li[i].roll = r


obj = student('', 0)

while True:
    print("1. Accept")
    print("2. Display")
    print("3. Update")
    print("4. Close")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        obj.accept(name, roll)

    if ch == 2:
        for i in range(len(student.li)):
            obj.dis(student.li[i])

    if ch == 3:
        roll = int(input("Enter roll number of student: "))
        r = int(input("Enter updated roll: "))
        obj.up(roll, r)

    if ch == 4:
        break
