# Skrypt został przygotowany do teorzenia postaci człowieka w grze Warhammer
# Tworzymy postać
# Wybieramy kolor oczy postaci
print('Zaczniemy od wybrania koloru oczu Twojej postaci')
eye_color = input('Rzuć k100 i wpisz liczbę która wypadła ')
if eye_color <= '10':
    print('Kolor oczu Twojej postaci to "Jasnoszary".')
elif '11' <= eye_color <= '20':
    print('Kolor oczu Twojej postaci to "Szaroniebieski".')
elif '21' <= eye_color <= '35':
    print('Kolor oczu Twojej postaci to "Niebieski".')
elif '36' <= eye_color <= '40':
    print('Kolor oczu Twojej postaci to "Zielony".')
elif '41' <= eye_color <= '50':
    print('Kolor oczu Twojej postaci to "Orzechowy".')
elif '51' <= eye_color <= '70':
    print('Kolor oczu Twojej postaci to "Jasnobrązowy".')
elif '71' <= eye_color <= '85':
    print('Kolor oczu Twojej postaci to "Brązowy".')
elif '86' <= eye_color <= '95':
    print('Kolor oczu Twojej postaci to "Ciemny brązowy".')
else:
    print('Kolor oczu Twojej postaci to "Purpurowy".')
# Wybieramy kolor włosów postaci
print('Wybieramy kolor włosów Twojej posatci')
hair_color = input('Rzuć k100 i wpisz liczbę która wypadła ')
if hair_color <= '10':
    print('Kolor włosów Twojej postaci to "Biały".')
elif '11' <= hair_color <= '20':
    print('Kolor włosów Twojej postaci to "Siwy".')
elif '21' <= hair_color <= '25':
    print('Kolor włosów Twojej postaci to "Płowy".')
elif '26' <= hair_color <= '40':
    print('Kolor włosów Twojej postaci to "Jasny blond".')
elif '41' <= hair_color <= '45':
    print('Kolor włosów Twojej postaci to "Blond".')
elif '46' <= hair_color <= '55':
    print('Kolor włosów Twojej postaci to "Miedziany".')
elif '56' <= hair_color <= '60':
    print('Kolor włosów Twojej postaci to "Rudy".')
elif '61' <= hair_color <= '70':
    print('Kolor włosów Twojej postaci to "Jasny brązowy".')
elif '71' <= hair_color <= '80':
    print('Kolor włosów Twojej postaci to "Brązowy".')
elif '81' <= hair_color <= '90':
    print('Kolor włosów Twojej postaci to "Ciemny brązowy".')
elif '91' <= hair_color <= '95':
    print('Kolor włosów Twojej postaci to "Kasztanowy".')
else:
    print('Kolor oczu twojej postaci to "Czarny".')
# Dodatkowy opis postaci
# Najpierw sprawdzamy czy postać ma dodatkowe cechy
print('Teraz sprawdzimy czy Twoja postać ma jakieś charakterystyczne cechy')
description_how_many = input('Rzuć k6 i podaj wynik ')
description_how_many = int(description_how_many) - 2
if description_how_many <= 0:
    print('Twoja postać nie ma szczególnych cech charakterystycznych')
elif description_how_many == 1:
    print('Twoja postać ma 1 charakterystyczną cechę')
elif description_how_many == 2:
    print('Twoja postać ma 2 charakterystyczne cechy')
elif description_how_many == 3:
    print('Twoja postać ma 3 charakterystyczne cechy')
elif description_how_many == 4:
    print('Twoja postać ma 4 charakterystyczne cechy')
# Opisy postaci
description = ''
while description_how_many >= 1 and description != 'stop':
    description = input('Wpisz "stop" jeżeli rezygnujesz z opisów lub rzuć k100 i podaj wynik ')
    if description == 'stop':
        print('Twoja postać nie będzie maiała charakterystycznych cech')
    else:
        characteristics = ''
        modifier = ''
        description = int(description)
        if description <= 2:
            characteristics = 'duży nos'
            modifier = 'brak'
        elif description <= 5:
            characteristics = 'płaski nos',
            modifier = 'brak'
        elif description <= 7:
            characteristics = 'haczykowaty nos'
            modifier = 'brak'
        elif description <= 10:
            characteristics = 'szrama na twarzy'
            modifier = '- 10 Ogd'
        elif description <= 12:
            characteristics = 'jedno oko'
            modifier = 'US * 0,5'
        elif description <= 15:
            characteristics = 'jedna ręka'
            modifier = '- 10 Zr'
        elif description <= 17:
            characteristics = 'charyzmatyczne oczy'
            modifier = '+ 10 Ogd'
        elif description <= 20:
            characteristics = 'atrakcyjna twarz'
            modifier = '+ 10 Ogd'
        elif description <= 22:
            characteristics = 'potężna budowa ciała'
            modifier = '+ 10% wagi'
        elif description <= 25:
            characteristics = 'wielki brzuch'
            modifier = '+ 10% wagi'
        elif description <= 27:
            characteristics = 'kulawy'
            modifier = '- 1 Sz (min. 2)'
        elif description <= 30:
            characteristics = 'łysy'
            modifier = 'brak'
        elif description <= 32:
            characteristics = 'bardzo długie włosy'
            modifier = 'brak'
        elif description <= 35:
            characteristics = 'kręcone włosy'
            modifier = 'brak'
        elif description <= 40:
            characteristics = 'wypadające włosy'
            modifier = 'brak'
        elif description <= 42:
            characteristics = 'bardzo krótkie włosy'
            modifier = 'brak'
        elif description <= 45:
            characteristics = 'garbienie się'
            modifier = 'brak'
        elif description <= 47:
            characteristics = 'szeroka klatka piersiowa'
            modifier = '+ 1 siły'
        elif description <= 50:
            characteristics = 'wysoki'
            modifier = '10 Cp'
        elif description <= 52:
            characteristics = 'niski'
            modifier = '- 1 Sz (minimum 2), -10 do wagi'
        elif description <= 55:
            characteristics = 'chudy'
            modifier = '- 10% do wagi'
        elif description <= 57:
            characteristics = 'bardzo blada cera'
            modifier = 'brak'
        elif description <= 60:
            characteristics = 'cera z bliznami po wrzodach'
            modifier = '- 10 Ogd'
        elif description <= 62:
            characteristics = 'szyderczy sposób bycia'
            modifier = '- 5 Ogd'
        elif description <= 65:
            characteristics = 'arogancki wyraz twarzy'
            modifier = '-5 Ogd, +5 Cp'
        elif description <= 67:
            characteristics = 'połamane zęby'
            modifier = '-10 Ogd'
        elif description <= 70:
            characteristics = 'bardzo białe zęby'
            modifier = '+5 Ogd'
        elif description <= 72:
            characteristics = 'seplenienie'
            modifier = '-10 Ogd'
        elif description <= 75:
            characteristics = 'jąkanie się'
            modifier = '- 10 do testów porozumiewania się'
        elif description <= 76:
            characteristics = 'bardzo czysty głos'
            modifier = '+5 do testów porozumiewania się'
        elif description <= 80:
            characteristics = 'mocny akcent'
            modifier = '-5 do testów porozumiewania się'
        elif description <= 82:
            characteristics = 'donośny głos'
            modifier = '+5 CP, -5O Ogd'
        elif description <= 85:
            characteristics = 'krzaczaste brwi'
            modifier = 'brak'
        elif description <= 87:
            characteristics = 'duże uszy'
            modifier = 'brak'
        elif description <= 90:
            characteristics = 'wąsy'
            modifier = 'brak'
        elif description <= 92:
            characteristics = 'znamię'
            modifier = 'brak'
        elif description <= 95:
            characteristics = 'krótkie nogi'
            modifier = '- 1 Sz (minimum 2)'
        elif description <= 97:
            characteristics = 'niezgrabne ręce'
            modifier = '-10 Zr'
        elif description <= 100:
            characteristics = 'długie paznokcie'
            modifier = 'brak'
        print(f'Cecha charakterystyczna Twojej postaci to {characteristics}, modyfikator postaci {modifier}.')
        description_how_many -= 1
