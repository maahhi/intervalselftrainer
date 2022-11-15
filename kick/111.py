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

        #seeing machine again?
        # if last_state + sign * round >= l:  # C
            #print('a')
        if sign == machine_sign:
            # print('ass')
            machine += abs((last_state + round)) // l
            # last_state = (last_state + sign * round) % l
            last_state = (last_state + round) % l
        # elif last_state+sign*round < 2*l:
        #     last_state = (last_state + sign * round) % l
        #     machine_sign = sign
        # else:
        #     machine_sign = sign
        #     round = round - (l-last_state)
        #     machine += round// l
        #     last_state =  round % l
        # added by a
        else:
            # print('trrr', round, last_state)
            if round >= last_state:
                # print('fff')
                sign *= -1
            machine += abs((last_state - round)) // l
            # last_state = (last_state + sign * round) % l
            last_state = abs(last_state - round) % l
            if round >= last_state:
                machine_sign *= -1


        # elif (last_state > 0 and last_state + round * sign <= 0):  # last state + sign -
        #     #print('b')
        #     if sign == machine_sign:
        #         #print('00')
        #         machine += 1
        #         round = (round*sign + last_state)/sign
        #         last_state = 0
        #         machine +=  round// l
        #         last_state = (sign * round) % l
        #     elif last_state+sign*round > -l:
        #         #print('01')
        #         last_state = (last_state + sign * round) % l
        #         machine_sign = sign
        #     else:
        #         #print('02')
        #         machine_sign = sign
        #         round = (round * sign + last_state) / sign
        #         last_state = 0
        #         machine += round // l
        #         last_state = (sign * round) % l
        #
        # elif  (last_state == 0 and round * sign <= 0):  # last state 0 sign -
        #     #print('c')
        #     if round * sign > -l: #not passing machine
        #         #print('00')
        #         last_state = (round*sign) % l
        #     elif sign == machine_sign:
        #         #print('01')
        #         machine += round // l
        #         last_state = (sign * round) % l
        #     else:
        #         #print('02')
        #         #round = round-l
        #         machine_sign = sign
        #         machine += round // l
        #         last_state = (sign * round) % l
        #
        # else: #  sing +
        #     #print('d')
        #     last_state = (last_state + sign * round) % l
        # #print('last_state',last_state)
        # #print('machine',machine)
        # print(last_state, sign, machine)
        n -= 1
    t-=1
    print("Case #" + str(testcases - t) + ":", int(machine))
