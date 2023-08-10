import threading
import time


def thread_kontrol(thread_id,timer):
    print("Thread {} True -> başladı.".format(thread_id))
    time.sleep(timer)
    print("Thread {} False -> bitti.".format(thread_id))


def run_threads(threadId_second):
    listThread = []

    for thread_id,timer in threadId_second:
        thread = threading.Thread(target=thread_kontrol, args=(thread_id,timer))
        listThread.append(thread)

    for thread in listThread:
        thread.start()

    for thread in listThread:
        thread.join()








