class Student:

    teacher = "None"
    __score = -1

    def __init__(self, name):
        self.__Name = name

    def __set_teacher(self, teacher):
        self.teacher = teacher

    def __set_score(self, score):
        self.__score = score

    def set(self, teacher, score):
        self.__set_teacher(teacher)
        self.__set_score(score)

    def output(self):
        print("Name: " + self.__Name)
        print("Teacher: " + self.teacher)
        print("score: " + str(self.__score))

Tanaka = Student("Tanaka Taro")

Yamada = Student("Yamada Aya")
Yamada.set("Tamura", 99)

Tanaka.output()
Yamada.output()
