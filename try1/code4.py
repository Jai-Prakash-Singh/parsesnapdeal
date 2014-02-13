from Queue import Queue
from threading import Thread
import time
import code3
import os 

num_fetch_threads = 2
enclosure_queue = Queue()


def main2(i, q):
    while True:
        directory, line = q.get()
        code3.main(directory, line)
        time.sleep(2)
	q.task_done()
	



def main():

    directory = "dir1" + time.strftime("%d%m%Y")

    if not os.path.exists(directory):
        os.makedirs(directory)

    f = open("code2_menu_smenu_cat_slink.csv")
    
    for i in range(num_fetch_threads):
        worker = Thread(target=main2, args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()

    for line in f:
        enclosure_queue.put((directory,str(line)))
      

    print '*** Main thread waiting ***'
    enclosure_queue.join()
    print '*** Done ***'
    f.close()


if __name__=="__main__":
    main()
