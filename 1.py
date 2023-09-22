for n in range(5, 100)

    if int('1' + bin(n)[2:][:-2] + '01'
           if bin(n)[2:][:3].count('1') % 2 == 0
           else
           '10' + bin(n)[2:][2:] + '1', 2) > 50:
        print(n)
        break