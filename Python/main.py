from kahoot import client
from random import choices 
from string import ascii_letters
from threading import Thread
from queue import Queue
from sys import argv
queue = Queue()
THREAD_COUNT = 5

def joinfunc(game_invite_code):
    while True:
        try:
            bot_username = queue.get_nowait()
            bot = client()
            bot.join(game_invite_code, bot_username)
            print(f'--- Joined game: "{game_invite_code}" with bot: "{bot_username}" ---')
        except Exception as e:
            print(f'~-- Got error: "{e}" while attempting to join game: "{game_invite_code}" with bot: "{bot_username}" --~')
            break
    
def main():
    threads = []
    if len(argv) == 3:
        try:
            print('=== Generating Usernames ===')
            for x in range(int(argv[2])):
                queue.put_nowait(''.join(choices(ascii_letters, k=29)))
            print(f'=== Generated {argv[2]} Usernames ===')
            print(f'=== Creating {THREAD_COUNT} Threads ===')
            for x in range(THREAD_COUNT):
                thr = Thread(target=joinfunc, args=(argv[1],))
                threads.append(thr) 
                thr.start()
            print('Press CTRL + C to exit [THIS WILL MAKE THE BOTS LEAVE THE GAME]')
            for thread in threads:
                thread.join()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
