# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.


init:
    

    $ prais = 0

    $ pelmeni = 0

    
    define me = Character('Я', color="#fffefe")
    define pr = Character('Кассир', color="#c01616")

    transform start1:
        linear 3 xpos -0.10

    
    
    



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    show xata_1
    "Я сидел за компьютером, когда мой живот предательски заурачал. Я встал с кресла и отправился на кухню."
    show int_semen_kitchen_7dl with dissolve
    "Там я открыл холодильник, в которым было пусто."

    me "Да..."

    me "Надо идти в магазин."
    show xata_1 with dissolve
    "Я оделся. Накинул на себя пальто. Я взял карту, на который был ограничен бюджет.Так же взял с собой наушники." 
    show int_access_day_7dl with dissolve
    pause(1)
    show ext_khruschevka_winter_7dl with dissolve

    "На улице был вечер, такой морозный вечер. Дул ветер, снег шумел под ногами. Машины ездили туда сюда."

    "Я надел наушники. И принялся выбирать песню."

    show ext_street_night_7dl with dissolve
    pause(5)
    
    "Пока играла пара песен, я дошёл до магазина."
    "Перед входом я снял с себя наушники."
    show maga with dissolve
    "Я вошёл в магазин. Там играла раслабляющая музыка."

    "Я взял тележку."

    "Куда мне пойти в первую очередь?"




label menu_fubor:
    menu:
        "Отдел холодильников":
            jump xolod
        "Хлебный отдел":
            jump xleb
        "Отдел с напитками":
            jump gaz
        "Отдел сладостей":
            jump sweetness
        "Отдел вредной пищи":
            jump cipsu
        "Овощьной и фруктовый отдел":
            jump fruit
        "Молочный отдел":
            jump milk
        "Бакалея":   
            jump grocery
        "Пойти на кассу":
            if prais == 0:
                "Я ещё ничего не купил. Я так голодным отстанусь."
                jump menu_fubor
            else:
                jump exit_maga

            
label xolod:
    menu:
        "Мясо":
            "Стоимость 500 рублей. К мясу надо что-то купить."
            $ prais += 500
            jump xolod
        "Морепродукты":
            "Стоимость 300 рублей, можно так есть. Но лучше с чем-то."
            $ prais += 300
            jump xolod
        "Пельмени":
            "Стоимость 300, вкусно."
            $ prais += 300
            $ pelmeni +=1
            jump xolod
        "Выйти из отдела":
            jump menu_fubor
        

    
label xleb:
    menu:
        "Хлеб":
            "Стоимость 50 рублей."
            $ prais += 50
            jump xleb
        "Батон":
            "Стоимость 50 рублей, можно так есть. Но лучше с чем-то. С колбасой или сыром."
            $ prais += 50
            jump xleb
        "Хлебобулочные изделия":
            "Пицца или пирожок?"
            menu:
                "Пицца?":
                    "Стоимость 100 рублей. Вкусно."
                    $ prais += 100
                    jump xleb
                "Пирожок?":
                    "Не так вкусно, как пицца, но дешевле.Стоимость 30"
                    $ prais += 30
                    jump xleb
        "Выйти из отдела":
            jump menu_fubor



    
label gaz:
    jump menu_fubor
label sweetness:
    jump menu_fubor
label cipsu:
    jump menu_fubor
label fruit:
    jump menu_fubor
label milk:
    jump menu_fubor
label grocery:
    jump menu_fubor
    



label exit_maga:
    "Я набрал всё что мне надо. И пошёл на кассу."
    pr "Здравстуйте!"
    me "Здравствуйте!"
    "Я выложил покупки на кассу."

    "..."

    pr "С вас %(prais)d."

    me "Картой."

    "Я приложил карту к терминалу, тот пикнул."
    if prais >=10000:
                jump luchai_con
    
    
    
    if pelmeni > 0:
            jump samai_luchai_con
    


    if prais >= 1:
        jump good_con
    if prais < 1:
        jump zanovo
    
    

label good_con:
    "Я сложил еду в пакет и отправился домой."
    
    scene ext_street_night_7dl with dissolve
    scene ext_khruschevka_winter_7dl with dissolve
    scene int_access_day_7dl with dissolve
    scene int_semen_kitchen_7dl with dissolve
    

    "Конец."
    return
label zanovo:
    $ prais *= 0
    "Как то мало я набрал. Мне этого даже на день не хватит."

    "Пойдем заново."
    jump menu_fubor
label luchai_con:
    "Слишком много лежало в пакетах."
    "Столько пакетов я не унесу."
    "..."
    "Вызову такси."
    return
label samai_luchai_con:
    "Я сложил еду в пакет и отправился домой."
    
    scene ext_street_night_7dl with dissolve
    scene ext_khruschevka_winter_7dl with dissolve
    scene int_access_day_7dl with dissolve
    scene int_semen_kitchen_7dl with dissolve

    "В пакети лежала такая сочная большая упаковка пельмений."

    "Я достал кострюли из шкафа. Налил в неё воду."
    "Поставил на плиту."
    "Включил газ."
    "В течение того времени, как вода закипала, я смотрел на упаковку пельмений."
    "Вода закипела. Я открыл пакет с пельменими. Высопал все пельмени в бурлящию воду."
    "Сыпнул туда гортску соли и спокойно мешал их, до того как они вспыли."
    return