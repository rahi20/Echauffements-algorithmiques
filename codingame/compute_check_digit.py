def compute_check_digit(identification_number: str):
    id_num = list(identification_number)
    
    sum_evens = sum([ int(digit) for (digit, i) in zip(id_num, list(range(len(id_num)))) if (i % 2 == 0) ], 0) 
    #print("sum_evens = {0}".format(sum_evens))

    sum_evens *= 3
    #print("sum_evens * 3 = {0}".format(sum_evens))

    total = sum([ int(digit) for (digit, i) in zip(id_num, list(range(len(id_num)))) if (i % 2 != 0) ], sum_evens)
    #print("total = {0}".format(total))

    str_total = str(total)
    last_digit = str_total[-1]
    
    if last_digit != "0" :
        #print()
        return str_total[:-1] + str(10 - int(last_digit))

    return str_total 

print(compute_check_digit("39847"))