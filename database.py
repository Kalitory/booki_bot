genres = {
    'Фантастика': ['научная', 'киберпанк', 'постапокалиптика', 'космос', 'альтернативная'],
    'Фэнтези': ['эпическое', 'гримдарк', 'историческое', 'детективное', 'романтическое'],
    'Психология': ['манипуляции', 'принять себя', 'найти себя', 'управления эмоциями', 'как отпустить человека'],
    'Ужасы': ['триллер', 'апокалиптика', 'лавкрафтовский ужас'],
    'Комедия': ['чёрный юмор', 'трагикомедия', 'романтические'],
    'Романы': ['военные', 'рыцарские', 'адюльтерные', 'бессюжетные']
}

sub_genres = {
    'научная': {
        'Туманность Андромеды - Иван Ефремов': 1,
        '«1984» - Джордж Оруэлл': 2,
        '«Цветы для Элджэрнона» - Дэниел Киз': 3,
        '«2001 год космическая одиссея» - Артур Кларк': 4,
    },
    'киберпанк': {
        '«Мечтают ли андроиды об электроовцах?» - Филип Дик': 5,
        '«Когда под ногами бездна» - Джордж Алек Эффинджер': 6,
        '«Видоизмененный углерод» - Ричард Морган': 7,
    },
    'постапокалиптика': {
        '«Дорога» - Кормак Маккарти': 8,
        '«Песня Сван» - Роберт Маккаммон': 9,
        '«Противостояние» - Стивен Кинг': 10,
    },
    'космос': {
        '«Революция в стоп-кадрах» - Питер Уоттс': 11,
        '«Химера» - Тесс Герритсен': 12,
        '«Проект "Аве Мария"» - Энди Вейер': 13,
        '«Автостопом по Галактике. Ресторан "У конца Вселенной"» - Дуглас Адамс': 14,
    },
    'альтернативная': {
        '«Человек в высоком замке» - Филип Дик': 15,
        ' «Ада, или Радости страсти» - Владимир Набоков': 16,
        '«Машина различий» - Брюс Стерлинг и Уильям Гибсон': 17,
        '«Фатерланд» - Роберт Харрис': 18,
        '«Теллурия» - Владимир Сорокин': 19,
    },
    'эпическое': {
        '«Архив Буресвета» – Брендон Сандерсон': 20,
        '«Хроники чёрного отряда» – Глен Кук': 21,
        '«Властелин колец» - Джон Р.Р. Толкиен': 22,
        '«Чёрный баламут» - Генри Лайон Олди': 23,
    },
    'гримдарк': {
        '«Без надежды на искупление» - Майкл Флетчер': 24,
        '«Печальная история братьев Гроссбарт» - Джесс Буллингтон': 25,
        '«Джаз сапожных гвоздей» - Александр Дедов': 26,
        'цикл «Багряная империя» - Джесс Буллингтон (Алекс Маршалл)': 27,
        'цикл «Нью-Кробюзон» - Чайна Мьевиль': 28,
    },
    'историческое': {
        '«Валькирия. Тот, кого я всегда жду» - Мария Семёнова': 29,
        '«Четыре жизни Хелен Ламберт» - Констанс Сэйерс': 30,
        '«Ведущий в погибель. Цикл «Конгрегация», №4» - Надежда Попова': 31,
        '«Холодные берега. Цикл «Искатели неба», №1» - Сергей Лукьяненко': 32,
        '«Финт» - Терри Пратчетт': 33,
    },
    'детективное': {
        '«Волонтеры вечности» - Макс Фрай': 34,
        '«Ночная стража Цикл «Плоский мир», №29» - Терри Пратчетт': 35,
        '«История, рассказанная сэром Джуффином Халли Цикл «Хроники Ехо», №3» - Макс Фрай': 36,
        '«Призрачное эхо. Цикл «Джекаби», №3» - Уильям Риттер': 37,
    },
    'романтическое': {
        '«Неукротимый шторм. Цикл «Изара», №3» - Юлия Диппель': 38,
        '«Академия Проклятий. Урок четвертый: Как развести нечисть на деньги Цикл «Академия проклятий», №4» - Елена Звёздная': 39,
        '«Подчиняться, чтобы править. Цикл «Академия темной магии», №2» - Анна Терешкова': 40,
        '«Я тебя рисую» - Марина Суржевская': 41,
        '«Сумерки» - Стефани Майер': 42,
    },
    'манипуляции': {
        '«Механизмы манипуляции – защита от чужого влияния» - Роберт Левин': 43,
        '«Эмоциональный шантаж. Не позволяйте использовать любовь как оружие против вас!» - Сьюзан Форвард': 44,
        '«Как завоевывать друзей и оказывать влияние на людей» - Дейл Карнеги': 45,
        '«Психология влияния» - Роберт Чалдини': 46,
    },
    'принять себя': {
        '«Безразличные матери. Исцеление от ран родительской нелюбви» - Сьюзан Форвард, Донна Фрейзер Глинн': 47,
        '«Рецепт счастья. Принимайте себя три раза в день» - Екатерина Сигитова': 48,
        '«Любовь к себе. 50 способов повысить самооценку» - Анастасия Залога': 49,
        '«Любовь к несовершенству. Принять себя и других со всеми недостатками» - Гемин Суним': 50,
    },
    'найти себя': {
        '«Сила настоящего» - Экхарт Толле': 51,
        '«Психологическая топология пути» - Мераб Мамардашвили': 52,
        '«Важные годы. Почему не стоит откладывать жизнь на потом» - Мэг Джей': 53,
        '«Эссенциализм. Путь к простоте» - Грег МакКеон': 54,
        '«Живи с чувством. Как поставить цели, к которым лежит душа» - Даниэлла Лапорт': 55,
    },
    'управления эмоциями': {
        '«Эмоциональный интеллект» - Сергей Шабанов и Алена Алешина': 56,
        '«Страх. Как одна эмоция объединяет» - Эбигейл Марш': 57,
        '«Психология эмоций» - Пол Экман': 58,
        '«Стрессоустойчивый мозг» - Мелани Гринберг': 59,
    },
    'как отпустить человека': {
        '«Отпусти меня. 12 шагов от страданий к здоровым отношениям» - Екатерина Явиц': 60,
        '«Когда любви слишком много» - В. Москаленко': 61,
        '«Женщины, которые любят слишком сильно» - Робин Норвуд': 62,
        '«Похорони своего бывшего» - Евгения Королева': 63,
        '«Пять языков любви» - Гэри Чепмен': 64,
    },
    'триллер': {
        '«55» - Джеймс Деларджи': 65,
        '«Терапия» - Себастьян Фитцек': 66,
        '«Головокружение» - Франк Тилье': 67,
        '«Я слежу за тобой» - Тереза Дрисколл': 68,
        '«Он сказал/она сказала» - Эрин Келли': 69,
    },
    'апокалиптика': {
        '«Мировая война Z» - Макс Брукс': 70,
        '«Вонгозеро» - Яна Вагнер': 71,
        '«Куколки» - Джон Уиндэм': 72,
        '«Война миров» - Герберт Уэллс': 73,
    },
    'лавкрафтовский ужас': {
        '«Дагон» - Говард Лавкрафт': 74,
        '«Картина в доме» - Говард Филлипс Лавкрафт': 75,
        '«Сияние извне» - Говард Филлипс Лавкрафт': 76,
        '«Иные боги. Повести и рассказы (сборник)» - Говард Филлипс Лавкрафт': 77,
    },
    'чёрный юмор': {
        '«Колыбель для Кошки» - Курт Воннегут': 78,
        '«Макулатура» - Чарльз Буковски': 79,
        '«Сказки тёмного леса» - Иван Фолькерт': 80,
        '«Уловка-22» -Джозеф Хеллер': 81,
    },
    'трагикомедия': {
        '«Незабвенная» - Ивлин Во': 82,
        '«Удушье» - Чак Паланик': 83,
        '«Тревожные люди» - Фредрик Бакман': 84,
    },
    'романтические': {
        '«Целуй меня в Риме» - Юлия Набокова': 85,
        '«Хороши в постели» - Дженнифер Вайнер': 86,
        '«Как я решила умереть от счастья» - Софи де Вильнуази': 87,
    },
    'военные': {
        '«В списках не значился» - Борис Васильев': 88,
        '«На Западном фронте без перемен Цикл «Потерянное поколение», №1» - Эрих Мария Ремарк': 89,
        '«Время жить и время умирать» - Эрих Мария Ремарк': 90,
        '«У войны не женское лицо Цикл «Голоса утопии», №1» - Светлана Алексиевич': 91,
        '«Повесть о настоящем человеке» - Борис Полевой': 92,
        '«Момент истины» - Владимир Богомолов': 93,
    },
    'рыцарские': {
        '«Сага о короле Артуре» - Мэри Стюарт': 98,
        '«Айвенго» - Вальтер Скотт': 99,
        '«Рыцари сорока островов» - Сергей Лукьяненко': 100,
        '«Белый отряд» - Сэр Артур Конан Дойл': 101,
    },
    'адюльтерные': {
        '«Конец одного романа» - Грэм Грин': 94,
        '«Пробуждение» - Кейт Шопен': 95,
        '«Невыносимая легкость бытия» - Милан Кундера': 96,
        '«Все закончится на нас» - Колин Гувер': 97,
    },
    'бессюжетные': {
        '«Путевые заметки» - Н. М. Карамзина, И. А. Гончарова': 102,
        '«Улисс» - Д. Джойс': 103,
    },
}