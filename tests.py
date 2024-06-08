import _thread
from logic import *
from spide4 import Connect4
import time

DEPTH1 = 1
DEPTH2 = 4
def rest(c4):
    c4.c=np.array([[3,3,3,3,3],
                    [3,0,0,0,3],
                    [3,0,0,0,3],
                    [3,0,0,0,3],
                    [3,3,3,3,3]])
def test(depth, eval1, eval2):
    c4 = Connect4()
    while(1):
        try:
            col,row = get_best_move(c4, 1, eval1,depth)
            #if c4.move(get_best_move(c4, 1, eval1, depth), 1):
            if c4.move(col,row, 1):
                c4.c[col,row]=5
                if(c4.is_gameover(1)):
                    return 1
            else:
                return -1
        except:
            return -1
        try:
            col,row=get_best_move(c4, 2, eval2, depth)
            #if c4.move(get_best_move(c4, 2, eval2, depth), 2):
            if c4.move(col,row, 2):
                c4.c[col,row]=5
                if(c4.is_gameover(2)):
                    return 2
            else:
               return -1

        except:
            return -1
    rest(c4)


# Agent 1 vs Agent 1
def a1va1():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav1, fav1)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav1, fav1)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))


# Agent 1 vs Agent 2
def a1va2():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav1, fav2)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav1, fav2)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 1 vs Agent 3
def a1va3():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav1, fav3)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav1, fav3)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))
# Agent 1 vs Agent 4
def a1va4():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav1, fav4)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav1, fav4)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent1 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 2 vs Agent 1
def a2va1():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav2, fav1)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav2, fav1)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 2 vs Agent 2
def a2va2():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav2, fav2)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav2, fav2)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 2 vs Agent 3
def a2va3():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav2, fav3)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav2, fav3)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 2 vs Agent 4
def a2va4():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav2, fav4)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav2, fav4)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent2 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 3 vs Agent 1
def a3va1():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav3, fav1)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav3, fav1)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 3 vs Agent 2
def a3va2():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav3, fav2)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav3, fav2)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 3 vs Agent 3
def a3va3():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav3, fav3)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav3, fav3)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 3 vs Agent 4
def a3va4():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav3, fav4)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav3, fav4)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent3 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 4 vs Agent 1
def a4va1():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav4, fav1)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav4, fav1)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent1 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 4 vs Agent 2
def a4va2():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav4, fav2)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav4, fav2)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent2 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 4 vs Agent 3
def a4va3():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav4, fav3)
        done=time.time()
        r1.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav4, fav3)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent3 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

# Agent 4 vs Agent 4
def a4va4():
    r1 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH1, fav4, fav4)
        done=time.time()
        r1.append(r)
        elapsed = done - start
    sum+=elapsed/10

    print("----- Agent4 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH1,r1.count(1), r1.count(2), r1.count(-1),format(sum,".4f")))

    r2 = []
    sum=0
    for i in range(10):
        start=time.time()
        r = test(DEPTH2, fav4, fav4)
        done=time.time()
        r2.append(r)
        elapsed = done - start
        sum+=elapsed/10

    print("----- Agent4 vs Agent4 -----\n\
    Depth: {}\n\
    > Player1: {} wins\n\
    > Player2: {} wins\n\
    > Draws: {}\n\
    > Average time: {}".format(DEPTH2,r2.count(1), r2.count(2), r2.count(-1),format(sum,".4f")))

a1va1()
a1va2()
a1va3()
a1va4()
a2va1()
a2va2()
a2va3()
a2va4()
a3va1()
a3va2()
a3va3()
a3va4()
a4va1()
a4va2()
a4va3()
a4va4()
