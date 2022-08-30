# Skrypy został przygotowany do teorzenia postaci człowieka w grze Warhammer
# Tworzymy postać
# Wybieramy kolor oczy postaci
print('Zaczniemy od wybrania koloru oczu Twojej postaci')
eye_color = input('Rzuć k100 i wpisz liczbę która wypadła ')
if eye_color <= "10":
    print('Kolor oczu Twojej postaci to "Jasnoszary".')
elif eye_color >="11" and eye_color <="20":
    print('Kolor oczu Twojej postaci to "Szaroniebieski".')
elif eye_color >="21" and eye_color <="35":
    print('Kolor oczu Twojej postaci to "Niebieski".')
elif eye_color >="36" and eye_color <="40":
    print('Kolor oczu Twojej postaci to "Zielony".')
elif eye_color >="41" and eye_color <="50":
    print('Kolor oczu Twojej postaci to "Orzechowy".')
elif eye_color >="51" and eye_color <="70":
    print('Kolor oczu Twojej postaci to "Jasnobrązowy".')
elif eye_color >="71" and eye_color <="85":
    print('Kolor oczu Twojej postaci to "Brązowy".')
elif eye_color >="86" and eye_color <="95":
    print('Kolor oczu Twojej postaci to "Ciemny brązowy".')
else:
    print('Kolor oczu Twojej postaci to "Purpurowy".')
# Wybieramy kolor włosów postaci
print('Wybieramy kolor włosów Twojej posatci')
hair_color = input('Rzuć k100 i wpisz liczbę która wypadła ')
if hair_color <= "10":
    print('Kolor włosów Twojej postaci to "Biały".')
elif hair_color >="11" and hair_color <="20":
    print('Kolor włosów Twojej postaci to "Siwy".')
elif hair_color >="21" and hair_color <="25":
    print('Kolor włosów Twojej postaci to "Płowy".')
elif hair_color >="26" and hair_color <="40":
    print('Kolor włosów Twojej postaci to "Jasny blond".')
elif hair_color >="41" and hair_color <="45":
    print('Kolor włosów Twojej postaci to "Blond".')
elif hair_color >="46" and hair_color <="55":
    print('Kolor włosów Twojej postaci to "Miedziany".')
elif hair_color >="56" and hair_color <="60":
    print('Kolor włosów Twojej postaci to "Rudy".')
elif hair_color >="61" and hair_color <="70":
    print('Kolor włosów Twojej postaci to "Jasny brązowy".')
elif hair_color >="71" and hair_color <="80":
    print('Kolor włosów Twojej postaci to "Brązowy".')
elif hair_color >="81" and hair_color <="90":
    print('Kolor włosów Twojej postaci to "Ciemny brązowy".')
elif hair_color >="91" and hair_color <="95":
    print('Kolor włosów Twojej postaci to "Kasztanowy".')
else:
    print('Kolor oczu twojej postaci to "Czarny".')
