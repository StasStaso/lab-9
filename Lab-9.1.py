''' --------------------Завдання--------------------------
Довідник студента. База даних вузів: адреса,
кількість факультетів, рівень акредитації, рейтинг.
Організувати вибір за довільним запитом. Дані
зберігаються в масиві, який створюється динамічно. '''
# --------------------Рішення---------------------------
#                ---  Змінні  ---
studentDict = {"Adress": "", "Count of faculty": 0, "Level of accreditation": "", "Rating": 0}
arrayOfStudentDict = []


#               ---  Рішення ---
def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Adress"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 2:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Count of faculty"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 3:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Level of accreditation"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 4:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Rating"] == criteria:
                print(arrayOfStudentDict[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про студента\n"
          "3. Знайти студента\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayOfStudentDict)
    elif choose == 2:
        '''----Ввід даних про студента----'''
        adress = input("Введіть адресу: ")
        countOfFaculty = int(input("Введіть к-ть факультетів: "))
        levelOfAcreditation = input("Рівень акредитації: ")
        rating = int(input("Рейтинг: "))

        '''---Заповнення словника---'''
        studentDict["Adress"] = adress
        studentDict["Count of faculty"] = countOfFaculty
        studentDict["Level of accreditation"] = levelOfAcreditation
        studentDict["Rating"] = rating
        arrayOfStudentDict.append(studentDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Адресса\n"
              "2.К-ть факультетів\n"
              "3.Рівень акредитації\n"
              "4.Рейтинг\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchCriteria = input("Введіть адресу: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = int(input("Введіть к-ть факультетів: "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = int(input("Введіть рівень акредитацї: "))
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Введіть рейтинг: "))
            serch(4, searchCriteria)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Ведіть коректне число\n")
