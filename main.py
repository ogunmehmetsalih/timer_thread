from timer_project import run_threads


if __name__ == "__main__":

    threadId_second = [(1, 3),(2, 7),(3, 10)]
    run_threads(threadId_second)

    print("Tüm threadler tamamlandı.")
