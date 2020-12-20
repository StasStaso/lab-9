"""--------------------Завдання--------------------------
Довідник кондитера. База даних кондитерських підприємств:
назва підприємства, адреса, рейтинг, спеціалізація.
Організувати вибір за довільним запитом. Дані зберігаються
в масиві записів, який створюється динамічно."""
# --------------------Рішення---------------------------
#                ---  Змінні  ---

productionDict = {"Name": "", "Adress": "", "Rating": 0, "Specialization": "", }
arrayOfProductionDict = []


#               ---  Рішення ---
def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Name"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 2:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Adress"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 3:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Rating"] == criteria:
                print(arrayOfProductionDict[i])
    if choose == 4:
        for i in range(len(arrayOfProductionDict)):
            if arrayOfProductionDict[i]["Specialization"] == criteria:
                print(arrayOfProductionDict[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про підприємство\n"
          "3. Знайти підприємство\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayOfProductionDict)
    elif choose == 2:
        '''----Ввід даних про підприємство----'''
        name = input("Введіть назву: ")
        adress = input("Введіть адресу: ")
        rating = int(input("Введіть рейтинг: "))
        specialization = input("Введіть спеціалізацію: ")

        '''---Заповнення словника---'''
        productionDict["Name"] = name
        productionDict["Adress"] = adress
        productionDict["Rating"] = rating
        productionDict["Specialization"] = specialization
        arrayOfProductionDict.append(productionDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Назва\n"
              "2.Адреса\n"
              "3.Рейтинг\n"
              "4.Спеціалізація\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchCriteria = input("Введіть назву: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = int(input("Введіть адресу: "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = int(input("Введіть рейтинг: "))
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Введіть спеціалізацію: "))
            serch(4, searchCriteria)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Ведіть коректне число\n")
