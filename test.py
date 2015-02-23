from time import sleep
import initio
import threading
import tachreader
import temp
import traceback

try:
    initio.GPIO.setwarnings(False)

    # x = threading.Thread(target=temp.mod_a)
    # y = threading.Thread(target=temp.mod_b)

    # x.start()
    # y.start()

    # y.run
    # x.run

    left = threading.Thread(target=tachreader.left_tach)
    right = threading.Thread(target=tachreader.right_tach)

    left.start()
    right.start()

    initio.init()

    initio.forward(100)

    left.run
    right.run

    lock = threading.RLock()


    for i in range(20):
        lock.acquire()
        print 'right:', tachreader.read_right()
        print 'left:', tachreader.read_left()
        print 
        # print "a:", temp.a
        # print "b:", temp.b
        lock.release()
        sleep(1)

    initio.stop()
except Exception as e:
    print traceback.format_exc()
    initio.cleanup()
