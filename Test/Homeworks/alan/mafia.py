import random


def night_menu_0(d, s, t):
    print("місто засинає, мафія прокидається")
    night_menu_1(d, s, t)


def night_menu_1(d, s, t):
    if t == 'Мафіозник':
        t = input('Кого ви хочете вбити' + 'p1 ' + 'p2 ' + 'p3 ' + 'p4 ' + 'p5 ')
        if t == 'p1':
            if p1 in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(p1)
                d.append(p1)
                print("Мафіозник зробив хід")
        if t == 'p2':
            if p2 in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(p2)
                d.append(p2)
                print("Мафіозник зробив хід")

        if t == 'p3':
            if p3 in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(p3)
                d.append(p3)
                print("Мафіозник зробив хід")

        if t == 'p4':
            if p4 in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(p4)
                d.append(p4)
                print("Мафіозник зробив хід")

        if t == 'p5':
            if p5 in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(p5)
                d.append(p5)
                print("Мафіозник зробив хід")

        else:
            a = random.choice(i)
            if a in d:
                t = input("виберіть іншу жертву:")
            else:
                i.remove(a)
                d.append(a)
        print("Мафіозник зробив хід")
        print("мафія засинає, лікар прокидається")
        night_menu_2(d, s, t)


def night_menu_2(d, s, t):
    if t == 'Лікар':
        t = input('Кого ви хочете вилікувати' + 'p1 ' + 'p2 ' + 'p3 ' + 'p4 ' + 'p5 ')
        if t == 'p1':
            if p1 in d:
                d.remove(p1)
                i.append(p1)
                print("ви вилікували хворого")
                print("Лікар зробив хід")
            else:
                print("ви вилікували здорового")
                print("Лікар зробив хід")
        if t == 'p2':
            if p2 in d:
                d.remove(p2)
                i.append(p2)
                print("ви вилікували хворого")
                print("Лікар зробив хід")
            else:
                print("ви вилікували здорового")
                print("Лікар зробив хід")
            if t == 'p3':
                if p3 in d:
                    d.remove(p3)
                    i.append(p3)
                    print("ви вилікували хворого")
                    print("Лікар зробив хід")
                else:
                    print("ви вилікували здорового")
                    print("Лікар зробив хід")
            if t == 'p4':
                if p4 in d:
                    d.remove(p4)
                    i.append(p4)
                    print("ви вилікували хворого")
                    print("Лікар зробив хід")
                else:
                    print("ви вилікували здорового")
                    print("Лікар зробив хід")
            if t == 'p5':
                if p5 in d:
                    d.remove(p5)
                    i.append(p5)
                    print("ви вилікували хворого")
                    print("Лікар зробив хід")
                else:
                    print("ви вилікували здорового")
                    print("Лікар зробив хід")
        else:
            a = random.choice(i)
            if a in d:
                d.remove(a)
                i.append(a)
                print("ви вилікували хворого")
                print("Лікар зробив хід")
            else:
                print("ви вилікували здорового")
                print("Лікар зробив хід")
        print("лікар засинає, шеріф прокидається")
        night_menu_3(d, s, t)


def night_menu_3(d, s, t):
    if t == 'Шеріф':
        t = input('Кого ви хочете вилікувати' + 'p1 ' + 'p2 ' + 'p3 ' + 'p4 ' + 'p5 ')
        if t == 'p1':
            if p1 in d:
                t = input("виберіть іншого підозрюваного:")
            if p1 in i:
                s.append(p1)
                print("Шеріф зробив хід")
        if t == 'p2':
            if p2 in d:
                t = input("виберіть іншого підозрюваного:")
            if p2 in i:
                s.append(p2)
                print("Шеріф зробив хід")
        if t == 'p3':
            if p3 in d:
                t = input("виберіть іншого підозрюваного:")
            if p3 in i:
                s.append(p3)
                print("Шеріф зробив хід")
        if t == 'p4':
            if p4 in d:
                t = input("виберіть іншого підозрюваного:")
            if p4 in i:
                s.append(p4)
                print("Шеріф зробив хід")
        if t == 'p5':
            if p5 in d:
                t = input("виберіть іншого підозрюваного:")
            if p5 in i:
                s.append(p5)
                print("Шеріф зробив хід")
    else:
        a = random.choice(i)
        if a in d:
            a = random.choice(i)
        if a in i:
            s.append(p5)
            print("Шеріф зробив хід")
    print("шеріф засинає, місто прокидається")
    night_menu_4(d, s, t)


def night_menu_4(d, s, t):
    print("сьогодні ми втратили " + d)
    print("шеріф підозрює " + s)
    h = input("хочеш зіграти ще одну ніч? Якщо так то пиши 'ТАК', якщо ні - 'НІ':")
    if h == 'ТАК':
        night_menu_0(t)
    if h == 'НІ':
        night_menu_x()


def night_menu_x():
    print("ДЯКУЮ ЗА ГРУ!!! Скачай ПРЕМІУМ версію лише за 999 гривень")


a = input('Привіт! Ти зараз граєш в мафію, напиши "START" що б почати грати: ')
p1 = 'Шеріф'
p2 = 'Законо слухняний громадянин_1'
p3 = 'Законо слухняний громадянин_2'
p4 = 'Лікар'
p5 = 'Мафіозник'
i = [p1, p2, p3, p4, p5]
d = []
s = []
if a == 'START':
    t = random.choice(i)
    print('ви ' + t)
    night_menu_0(d, s, t)
