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
