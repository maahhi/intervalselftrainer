t = int(input())
testcases = t
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

        cond = True
        round_decreased = False
        while cond:
            if round*sign + last_state >= l or (round*sign + last_state <= 0):
                if machine_sign == sign or last_state == 0:

                    if last_state == 0 and abs ((last_state + sign * round)) // l < 2:
                        machine_sign = sign

                    if last_state + sign * round <=0:
                        machine+=1
                        last_state = 0
                        round = round-last_state

                    machine += abs ((last_state + sign * round)) // l

                    '''
                    if round_decreased:
                        machine+=1
                        round_decreased = False
                    '''

                    last_state = (last_state + sign * round) % l
                    break
                else:
                    machine_sign = sign

                    if round >= l:
                        round = round - l
                        round_decreased = True
                    else:
                        last_state = (last_state + sign * round)%l
                        break
            else:
                last_state = (last_state + sign * round)%l
                break

        print('last_state',last_state)
        print('machine',machine)
        n -= 1
    t-=1
    print("Case #" + str(testcases - t) + ":", machine)
