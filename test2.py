from collections import deque
import numpy as np
from pynput.keyboard import Listener, Key

store = set()
def handleKeyPress(key):
    store.add(key)

    print('Press: {}'.format(store))
    store.remove(key)


def handleKeyRelease(key):
    print('Released: {}'.format(key))

    if key in store:
        store.remove(key)

    # 종료
    if key == Key.esc:
        return False


with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()


def main():
    a = [1,2,3,4,5,6]
    del_a = []
    a.append(7)
    print(a)
    a.append((8))
    print(a)

    print(a[-2])
    print(len(a))

    del_a.append(a[-1])
    del a[len(a)-1]

    print(a)
    print(del_a)

    a.append(del_a[-1])
    del del_a[len(del_a) - 1]

    print(a)
    print(del_a)


# '''Main function'''
if __name__ == "__main__":
    main()