def rot(num):
    str_num = str(num)
    num_list = list(str_num)

    flag = True

    for i in range(0, len(num_list)):
        if num_list[i] == '6' and flag:
            num_list[i] = '9'
            flag = False

    return int(''.join(num_list))