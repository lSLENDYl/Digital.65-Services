def pred(base, rebenok): #предпочтения
    result = []
    final_result = ''
    for i in base:
        num1, num2 = base[i][1].split('-')
        if base[i][0]==rebenok[0] and int(num1) <= int(rebenok[1]) <= int(num2) and base[i][2]==rebenok[2] and base[i][3]==rebenok[3] :
            result.append(i)
    for i in result:
        final_result += (i+' ')
    return final_result