import threading
import time

filename = 'validtest.txt'
#############
####  READING THE INPUT INTO ROWS AND COLUMNS AND SUBGRIDS IN THE KASIF-EST WAY POSSIBLE
#############
puzzle_rows =[[int(i) for i in line.strip().split(' ')] for line in open(filename).readlines()]
puzzle_cols = [[item[0] for item in puzzle_rows], [item[1] for item in puzzle_rows], [item[2] for item in puzzle_rows],
               [item[3] for item in puzzle_rows], [item[4] for item in puzzle_rows], [item[5] for item in puzzle_rows],
               [item[6] for item in puzzle_rows], [item[7] for item in puzzle_rows], [item[8] for item in puzzle_rows]]
puzzle_sqrs = [[puzzle_rows[0][0], puzzle_rows[0][1], puzzle_rows[0][2],
                puzzle_rows[1][0], puzzle_rows[1][1], puzzle_rows[1][2],
                puzzle_rows[2][0], puzzle_rows[2][1], puzzle_rows[2][2]],

                [puzzle_rows[3][0], puzzle_rows[3][1], puzzle_rows[3][2],
                puzzle_rows[4][0], puzzle_rows[4][1], puzzle_rows[4][2],
                puzzle_rows[5][0], puzzle_rows[5][1], puzzle_rows[5][2]],

                [puzzle_rows[6][0], puzzle_rows[6][1], puzzle_rows[6][2],
                puzzle_rows[7][0], puzzle_rows[7][1], puzzle_rows[7][2],
                puzzle_rows[8][0], puzzle_rows[8][1], puzzle_rows[8][2]],

                [puzzle_rows[0][3], puzzle_rows[0][4], puzzle_rows[0][5],
                puzzle_rows[1][3], puzzle_rows[1][4], puzzle_rows[1][5],
                puzzle_rows[2][3], puzzle_rows[2][4], puzzle_rows[2][5]],

                [puzzle_rows[3][3], puzzle_rows[3][4], puzzle_rows[3][5],
                puzzle_rows[4][3], puzzle_rows[4][4], puzzle_rows[4][5],
                puzzle_rows[5][3], puzzle_rows[5][4], puzzle_rows[5][5]],

                [puzzle_rows[6][3], puzzle_rows[6][4], puzzle_rows[6][5],
                puzzle_rows[7][3], puzzle_rows[7][4], puzzle_rows[7][5],
                puzzle_rows[8][3], puzzle_rows[8][4], puzzle_rows[8][5]],

                [puzzle_rows[0][6], puzzle_rows[0][7], puzzle_rows[0][8],
                puzzle_rows[1][6], puzzle_rows[1][7], puzzle_rows[1][8],
                puzzle_rows[2][6], puzzle_rows[2][7], puzzle_rows[2][8]],

                [puzzle_rows[3][6], puzzle_rows[3][7], puzzle_rows[3][8],
                puzzle_rows[4][6], puzzle_rows[4][7], puzzle_rows[4][8],
                puzzle_rows[5][6], puzzle_rows[5][7], puzzle_rows[5][8]],

                [puzzle_rows[6][6], puzzle_rows[6][7], puzzle_rows[6][8],
                puzzle_rows[7][6], puzzle_rows[7][7], puzzle_rows[7][8],
                puzzle_rows[8][6], puzzle_rows[8][7], puzzle_rows[8][8]]
                ]

#############
####  VALIDATOR IS A LIST OF 0 AND 1'S TO CHECK THE VALIDNESS (IS THAT EVEN A WORD?)
###   IF ALL ELEMENTS ARE ONE THEN ITS SUM IS 27 SO IT'S A VALID SOLUTION
#############
validator = []

#############
####  THIS FUNCTION CHECKS THE NUMBER OF UNIQUE ELEMENTS OF ITS INPUT
#############
def checker(nokhod):
    if len(list(set(nokhod))) == 9:
        validator.append(1)
    else:
        validator.append(0)

#######################################
#######################################
####  LETS GET THREADYYYY :D
#######################################
#######################################
try:
    t1 = threading.Thread(target = checker, args=[puzzle_rows[0]])
    t2 = threading.Thread(target = checker, args=[puzzle_rows[1]])
    t3 = threading.Thread(target = checker, args=[puzzle_rows[2]])
    t4 = threading.Thread(target = checker, args=[puzzle_rows[3]])
    t5 = threading.Thread(target = checker, args=[puzzle_rows[4]])
    t6 = threading.Thread(target = checker, args=[puzzle_rows[5]])
    t7 = threading.Thread(target = checker, args=[puzzle_rows[6]])
    t8 = threading.Thread(target = checker, args=[puzzle_rows[7]])
    t9 = threading.Thread(target = checker, args=[puzzle_rows[8]])
    # print('ane saggg')
    t10 = threading.Thread(target = checker, args=[puzzle_cols[0]])
    t11 = threading.Thread(target = checker, args=[puzzle_cols[1]])
    t12 = threading.Thread(target = checker, args=[puzzle_cols[2]])
    t13 = threading.Thread(target = checker, args=[puzzle_cols[3]])
    t14 = threading.Thread(target = checker, args=[puzzle_cols[4]])
    t15 = threading.Thread(target = checker, args=[puzzle_cols[5]])
    t16 = threading.Thread(target = checker, args=[puzzle_cols[6]])
    t17 = threading.Thread(target = checker, args=[puzzle_cols[7]])
    t18 = threading.Thread(target = checker, args=[puzzle_cols[8]])
    # print('tokhme saggg')
    t19 = threading.Thread(target = checker, args=[puzzle_sqrs[0]])
    t20 = threading.Thread(target = checker, args=[puzzle_sqrs[1]])
    t21 = threading.Thread(target = checker, args=[puzzle_sqrs[2]])
    t22 = threading.Thread(target = checker, args=[puzzle_sqrs[3]])
    t23 = threading.Thread(target = checker, args=[puzzle_sqrs[4]])
    t24 = threading.Thread(target = checker, args=[puzzle_sqrs[5]])
    t25 = threading.Thread(target = checker, args=[puzzle_sqrs[6]])
    t26 = threading.Thread(target = checker, args=[puzzle_sqrs[7]])
    t27 = threading.Thread(target = checker, args=[puzzle_sqrs[8]])


    t1.start()
    time_t1 = time.time()
    t2.start()
    time_t2 = time.time()
    t3.start()
    time_t3 = time.time()
    t4.start()
    time_t4 = time.time()
    t5.start()
    time_t5 = time.time()
    t6.start()
    time_t6 = time.time()
    t7.start()
    time_t7 = time.time()
    t8.start()
    time_t8 = time.time()
    t9.start()
    time_t9 = time.time()
    t10.start()
    time_t10 = time.time()
    t11.start()
    time_t11 = time.time()
    t12.start()
    time_t12 = time.time()
    t13.start()
    time_t13 = time.time()
    t14.start()
    time_t14 = time.time()
    t15.start()
    time_t15 = time.time()
    t16.start()
    time_t16 = time.time()
    t17.start()
    time_t17 = time.time()
    t18.start()
    time_t18 = time.time()
    t19.start()
    time_t19 = time.time()
    t20.start()
    time_t20 = time.time()
    t21.start()
    time_t21 = time.time()
    t22.start()
    time_t22 = time.time()
    t23.start()
    time_t23 = time.time()
    t24.start()
    time_t24 = time.time()
    t25.start()
    time_t25 = time.time()
    t26.start()
    time_t26 = time.time()
    t27.start()
    time_t27 = time.time()

    t1.join()
    print('Thread1: ' + str(time.time() - time_t1) + ' s')
    t2.join()
    print('Thread2: ' + str(time.time() - time_t2) + ' s')
    t3.join()
    print('Thread3: ' + str(time.time() - time_t3) + ' s')
    t4.join()
    print('Thread4: ' + str(time.time() - time_t4) + ' s')
    t5.join()
    print('Thread5: ' + str(time.time() - time_t5) + ' s')
    # print('gohe saggg')
    t6.join()
    print('Thread6: ' + str(time.time() - time_t6) + ' s')
    t7.join()
    print('Thread7: ' + str(time.time() - time_t7) + ' s')
    t8.join()
    print('Thread8: ' + str(time.time() - time_t8) + ' s')
    t9.join()
    print('Thread9: ' + str(time.time() - time_t9) + ' s')
    t10.join()
    print('Thread10: ' + str(time.time() - time_t10) + ' s')
    t11.join()
    print('Thread11: ' + str(time.time() - time_t11) + ' s')
    t12.join()
    print('Thread12: ' + str(time.time() - time_t12) + ' s')
    t13.join()
    print('Thread13: ' + str(time.time() - time_t13) + ' s')
    t14.join()
    print('Thread14: ' + str(time.time() - time_t14) + ' s')
    t15.join()
    print('Thread15: ' + str(time.time() - time_t15) + ' s')
    t16.join()
    print('Thread16: ' + str(time.time() - time_t16) + ' s')
    t17.join()
    print('Thread17: ' + str(time.time() - time_t17) + ' s')
    t18.join()
    print('Thread18: ' + str(time.time() - time_t18) + ' s')
    t19.join()
    print('Thread19: ' + str(time.time() - time_t19) + ' s')
    t20.join()
    print('Thread20: ' + str(time.time() - time_t20) + ' s')
    t21.join()
    print('Thread21: ' + str(time.time() - time_t21) + ' s')
    t22.join()
    print('Thread22: ' + str(time.time() - time_t22) + ' s')
    t23.join()
    print('Thread23: ' + str(time.time() - time_t23) + ' s')
    t24.join()
    print('Thread24: ' + str(time.time() - time_t24) + ' s')
    t25.join()
    print('Thread25: ' + str(time.time() - time_t25) + ' s')
    t26.join()
    print('Thread26: ' + str(time.time() - time_t26) + ' s')
    t27.join()
    print('Thread27: ' + str(time.time() - time_t27) + ' s')


    if (sum(validator) == 27):
        print('result: valid solution')
    else:
        print('result: invalid solution')
except:
    print('Couldn\'t start threads')
