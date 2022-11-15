import random
import os
from playsound import playsound
from bidict import bidict

current_path = ['.']
number_of_test_per_instrument_groups = 35

answerinterp = bidict(
    {'u': 0, 's': 1, '2': 2, '3min': 3, '3maj': 4, '4': 5, '5dim': 6, '5': 7, '6min': 8, '6maj': 9, '7min': 10,
     '7maj': 11, 'o': 12,
     '-s': -1, '-2': -2, '-3min': -3, '-3maj': -4, '-4': -5, '-5dim': -6, '-5': -7, '-6min': -8, '-6maj': -9,
     '-7min': -10, '-7maj': -11, '-o': -12, })


def play_interval (interval = 0):
    # https://theremin.music.uiowa.edu/MISpiano.html
    pass

def assign_groups():
    path = current_path+ ['groups']
    groupA_filename = os.path.join(*path, 'groupA.txt')
    groupB_filename = os.path.join(*path, 'groupb.txt')
    if os.path.exists(groupA_filename) and os.path.exists(groupB_filename):
        print('files already exist, delet them manually if you want to change groups')
        #ans = input()
        # TODO ask if they want to rewrite
    else:
        intervals = [i for i in range(-12,13)]
        intervals.remove(0)
        random.shuffle(intervals)
        groupA = intervals[:12]+[0]
        groupB = intervals[12:]+[0]
        with open(groupA_filename, 'w') as f:
            for interv in groupA:
                f.write(str(interv) + '\n')
        with open(groupB_filename, 'w') as f:
            for interv in groupB:
                f.write(str(interv)+'\n')


def load_groups (group_name = 'A'):
    path = current_path+['groups']
    file_name = os.path.join(*path, 'group'+group_name+'.txt')
    group = []
    with open(file_name, 'r') as f:
        for line in f:
            group.append(int(line))
    return group

def instrument_min_max(instrument = 'piano'):
    min_note = 52
    max_note = 69
    return min_note,max_note


def generate_interval_set(instrument,intervalgroup ,number_of_intervals):
    # https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
    instrument_min, instrument_max = instrument_min_max(instrument)
    tests = []

    while True:
        if number_of_intervals < len(intervalgroup):
            for interval in intervalgroup[0:number_of_intervals]:
                root = random.randint(max(instrument_min, instrument_min - interval),
                                      min(instrument_max, instrument_max - interval))
                tests.append((root, root + interval))
            break
        else:
            for interval in intervalgroup:
                root = random.randint(max(instrument_min, instrument_min - interval),
                                      min(instrument_max, instrument_max - interval))
                tests.append((root,root+interval))
            number_of_intervals -= len(intervalgroup)

    random.shuffle(tests)
    return tests


def save_questions(test_name='pretest',groups = ['A', 'B'], instruments = ['piano', 'singer', 'vocal']):
    question_list = [[] for i in instruments]
    instrument_counter_pretest = 0
    for instrument in instruments:
        for group in groups:
            group_list = load_groups(group)  # groupA = [7 ,-12, 12, -1, ...]
            test_set = generate_interval_set(instrument, group_list,
                                             number_of_test_per_instrument_groups)  # [(69,67),(102,110),...]
            if test_name == 'posttest':
                for t in test_set:
                    question_list[instrument_counter_pretest].append((t,group))
            else:
                # save questions
                path = current_path + [test_name, instrument, 'group' + group]
                q_filename = os.path.join(*path, 'question.txt')
                #print(group, instrument, test_set, q_filename)
                with open(q_filename, 'w') as f:
                    for interv in test_set:
                        f.write(str(interv[0]) + ' ' + str(interv[1]) + '\n')
        instrument_counter_pretest += 1

    if test_name == 'posttest':
        for index , test_set in enumerate(question_list):
            #print(test_set)
            random.shuffle(test_set)
            instrument = instruments[index]
            path = current_path + [test_name, instrument]
            q_filename = os.path.join(*path, 'question.txt')
            with open(q_filename, 'w') as f:
                for interv in test_set:
                    f.write(str(interv[0][0]) + ' ' + str(interv[0][1]) + '\n')

            path = current_path + [test_name, instrument]
            g_filename = os.path.join(*path, 'groups.txt')
            with open(g_filename, 'w') as f:
                for interv in test_set:
                    f.write(str(interv[1])+ '\n')


def load_question_set(file_name):
    question_set = []
    with open(file_name, 'r') as f:
        for line in f:
            question_set.append((int(line.split(' ')[0]), int(line.split(' ')[1])))
    return question_set


def ask_questions(test_name='pretest', groups=['A', 'B'],instruments = ['piano', 'singer', 'vocal']):
    print( 'your options are:', * list(answerinterp.keys())[0:13], '\n add \'-\' for decsendings')
    if test_name == 'posttest':
        groups = ['A']
    for instrument in instruments:
        for group in groups:
            group_list = load_groups(group)  # groupA = [7 ,-12, 12, -1, ...]
            path = current_path + [test_name, instrument, 'group' + group]
            if test_name == 'posttest':
                path = current_path + [test_name, instrument]
            q_filename = os.path.join(*path, 'question.txt')
            question_set=load_question_set(q_filename)
            a_filename = os.path.join(*path, 'given_answer.txt')
            wave_path = ['instruments',instrument]
            with open(a_filename, 'w') as f:
                counter = 1
                for q in question_set:
                    print(counter,'listen!')
                    root = q[0]
                    root_file = os.path.join(*current_path,*wave_path, instrument[0]+str(root)+'.wav')
                    interv = q[1]
                    interv_file = os.path.join(*current_path, *wave_path, instrument[0]+str(interv) + '.wav')
                    while True:
                        playsound(root_file)
                        # TODO : play silence
                        playsound(interv_file)
                        ans = input("type the interval you just heared: ").replace(" ", "").lower()
                        if ans in answerinterp.keys():
                            break
                        print('what?')
                    counter+=1
                    answer = answerinterp[ans]
                    f.write(str(answer)+'\n')
                    if test_name[0] == 't':
                        # show real answer
                        if answer == interv-root:
                            print('Correct')
                        else:
                            print('wrong \n correct answer was', answerinterp.inverse[interv-root] ,'\n listen again' )
                            while True:
                                print( 'correct answer', answerinterp.inverse[interv-root])
                                playsound(root_file)
                                playsound(interv_file)
                                mi , ma =  instrument_min_max()
                                ans_midi = q[0] + answer
                                if ans_midi <= ma and ans_midi >= mi :
                                    print('your answer', answerinterp.inverse[answer] )
                                    ans_file = os.path.join(*current_path, *wave_path,instrument[0] + str(ans_midi) + '.wav')
                                    playsound(root_file)
                                    playsound(ans_file)
                                if 'p'==input('for pass insert p :'):
                                    break
                        pass


def run_pretest():
    groups = ['A', 'B']
    instruments = ['piano', 'singer', 'vocal']
    # should not show the correct answer
    save_questions('pretest')
    ask_questions('pretest',groups,instruments)#,groups,instruments)


def run_posttest():
    #save_questions('posttest')
    ask_questions('posttest', ['A'],['piano'])


def training_session(session_number,group):
    if group == 'A':
        instrument = 'vocal'
    else:
        instrument = 'singer'
    # create directory :
    dir = os.path.join(*current_path,'train_'+session_number, instrument, 'group' + group)
    print(dir)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    save_questions('train_'+session_number,[group],[instrument])
    ask_questions('train_'+session_number,[group],[instrument])




#
#play_interval(0)
#assign_groups()
#run_pretest()
#g = load_groups('B')
#print(g)
#print(generate_interval_set('piano',g ,20))
#run_posttest()
#print(load_question_set(".\\posttest\\vocal\\groupB\\question.txt"))
#run_posttest()

A = sorted(load_groups('A'), key=lambda x:abs(x))
B = sorted(load_groups('B'), key=lambda x:abs(x))
for a in A:
    print(answerinterp.inverse[a],end=' ')
print('')
'''
for b in B:
    print(answerinterp.inverse[b],end=' ')
'''
#training_session('10','B')
run_posttest()