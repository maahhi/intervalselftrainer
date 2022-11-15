t = int(input())
while t > 0:
    l,n = map(int,input().split())
    machine = 0
    machine_sign = None
    last_state = 0
    while n > 0:
        inp = input().split()
        round = int(inp[0])
        if inp[1] == 'C':
            sign = +1
        else:
            sign = -1
        if machine_sign is None:
            machine_sign = sign

        flag = True
        if ( last_state + sign * round ) >= l and flag:
            if machine_sign == sign :
                machine +=1
            else:
                machine_sign = sign

            last_state = (last_state + sign * round)%l
            flag = False
        elif ( last_state + sign * round ) <= 0:
            if machine_sign == sign :
                machine +=1
            else:
                machine_sign = sign
            last_state = (last_state + sign * round) % l
        else:
            if flag:
                last_state = last_state + sign * round


