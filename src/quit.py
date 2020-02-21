import time


def quit(user):
    print("are you sure you want to quit?")
    q_put = input("yes or no...\n----> ")
    if q_put == "no":
        print("ok... was worried there for a second")
    elif q_put == "yes":
        print('aaaaah... fine see you later')
        time.sleep(1)
        print(f'Goodbye {user}!')
        time.sleep(2)
        exit()
    else:
        print("not sure what that meant.... ")
        time.sleep(1)
        quit(user)
