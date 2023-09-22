a = "Найдите ошибку в коде ученика и объясните её. \n\nПояснение состоит из двух частей:\n\n1. Описание ошибки (с указанием строки на ПРИЧИНУ ошибки)\n\n2. Идея, как её исправить\n\nПодробнее в статье:\n\nhttps://wiki.yandex-team.ru/onbording-dlja-trenerov-nejjroseti-uchebnik/5-jetap-3.-objasnenie-oshibok/\n\n\n\n```\nn = 864 // 4  # дописав 00 мы увеличили число в 4 раза\nfor i in range(1, 9):\n    for j in range(1, 9):\n        if i ** j == n:\n            print(str(i)  j)\n            break\n\n```\n"
temp = a.split('```')[1]
for i, row in enumerate(temp.split('\n')):
    print(i + 1, ':', row)

for row in temp.split('\n'):
    print(row)


