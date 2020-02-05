import threading
import statistics

data = []

def avg():
    print('The Average Value is: ', statistics.mean(data))

def mini():
    print('The Minimum Value is: ', min(data))

def maxi():
    print('The Maximum Value is: ', max(data))

def devi():
    print('The Standard Deviation is: ', statistics.stdev(data))

count = input("Enter the number of your numbers: ")
for i in range(int(count)):
    data.append(int(input()))
try:
    t1 = threading.Thread(target=avg)
    t2 = threading.Thread(target=mini)
    t3 = threading.Thread(target=maxi)
    t4 = threading.Thread(target=devi)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
except:
    print('Error: unable to start thread')
