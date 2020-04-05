import time
import pickle

password = str(input("Dein Passwort: "))

start = time.time()
position_0 = 0
position_1 = 0
position_2 = 0
position_3 = 0
position_4 = 0

list_of_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                          'j',
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", "B", "C",
                          "D",
                          "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                          "Y",
                          "Z", "@", "#", "Ü", "Ö", "Ä", "ü", "ö", "ä", "*", "+", "/", "-", ";", ",", ".", ":", "_", "µ",
                          "!",
                          "§", "$", "%", "&", "=", "?", "ß", "(", ")"]

"""
def create_pickle():
    password_list = []
    def create_list():
        global position_3, position_2, position_1, position_0
        while True:
            string = list_of_characters[position_0]
            password_list.append(string)
            position_0 = position_0 + 1
            if position_0 > len(list_of_characters) - 1:
                position_0 = 0
                break
        while True:
            string = list_of_characters[position_1] + list_of_characters[position_0]
            password_list.append(string)
            position_0 = position_0 + 1
            if position_0 > len(list_of_characters) - 1:
                position_0 = 0
                position_1 = position_1 + 1
                if position_1 > len(list_of_characters) - 1:
                    position_1 = 0
                    break
        while True:
            string = list_of_characters[position_2] + list_of_characters[position_1] + list_of_characters[position_0]
            password_list.append(string)
            position_0 = position_0 + 1
            if position_0 > len(list_of_characters) - 1:
                position_0 = 0
                position_1 = position_1 + 1
                if position_1 > len(list_of_characters) - 1:
                    position_1 = 0
                    position_2 = position_2 + 1
                    if position_2 > len(list_of_characters) - 1:
                        position_2 = 0
                        break
        while True:
            string = list_of_characters[position_3] + list_of_characters[position_2] \
                     + list_of_characters[position_1] + list_of_characters[position_0]
            password_list.append(string)
            position_0 = position_0 + 1
            if position_0 > len(list_of_characters) - 1:
                position_0 = 0
                position_1 = position_1 + 1
                if position_1 > len(list_of_characters) - 1:
                    position_1 = 0
                    position_2 = position_2 + 1
                    if position_2 > len(list_of_characters) - 1:
                        position_2 = 0
                        position_3 = position_3 + 1
                        if position_3 > len(list_of_characters) - 1:
                            position_3 = 0
                            break
    create_list()
    pickle_out = open("password_list.pickle", "wb")
    pickle.dump(password_list, pickle_out)
    pickle_out.close()
create_pickle()
"""


pickle_in = open("password_list.pickle", "rb")
password_list = pickle.load(pickle_in)
ende = time.time()
print("Zeit zum laden:", ende - start)
#print(password_list)


for i in range(0,len(password_list)):
    if password == password_list[i]:
        print("Dein Passwort ist: ", password_list[i])
        ende_ende = time.time()
        print("Die Zeit betrug: ", ende_ende - start, " Sekunden")

print("Passwort hat mehr als 4 Stellen")

a, b = 0, 0
begin = time.time()
while True:
    password_5 = list_of_characters[b] + password_list[a]
    if password == password_5:
        ende= time.time()
        print("Dein Passwort ist: ", password_5)
        print("Zeit: ", ende-begin)
        break
    else:
        a = a+1
        if a > len(password_list)-1:
            a = 0
            b = b+1
            if b > len(list_of_characters):
                print("Passwort ist zu lang!")
                break
