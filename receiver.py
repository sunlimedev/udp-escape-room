from socket import *
import cv2
from time import sleep


def connection_info():
    # set tower (server) ip address
    server_ip = '192.168.1.100'

    # set server port
    server_port = 12000

    # create client socket
    client_socket = socket(AF_INET, SOCK_DGRAM)

    return server_ip, server_port, client_socket


def load_images():
    # get the images ready prior to starting
    img_locked = cv2.imread('locked_gemini.png')
    img_alarm_clock = cv2.imread('alarm_clock_gemini.png')
    img_unlocked = cv2.imread('unlocked_gemini.png')

    return img_locked, img_alarm_clock, img_unlocked


def build_freq_dict_list():
    # dictionary for displaying clock frequency slider in terminal ( frequency : string_index )
    freq_pairs = {
        90.0: 8,
        90.5: 10,
        91.0: 13,
        91.5: 16,
        92.0: 18,
        92.5: 20,
        93.0: 23,
        93.5: 26,
        94.0: 28,
        94.5: 30,
        95.0: 33,
        95.5: 36,
        96.0: 38,
        96.5: 40,
        97.0: 43,
        97.5: 46,
        98.0: 48,
        98.5: 50,
        99.0: 53,
        99.5: 56,
        100.0: 58
    }

    # list of accepted frequencies
    allowed_freq = [90.0, 90.5, 91.0, 91.5, 92.0, 92.5, 93.0, 93.5, 94.0, 94.5, 95.0, 95.5, 96.0, 96.5, 97.0, 97.5, 98.0, 98.5, 99.0, 99.5, 100.0]

    return freq_pairs, allowed_freq


def build_clock():
    # list for clock ascii strings
    clock_ascii = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    # ascii alarm clock used as gemini prompt
    clock_ascii[0] = "╔═══════════════════════════════════════════════════════════════════════════════════╗"
    clock_ascii[1] = "║     CASIO    Alarm Clock w/ FM Receiver                                           ║"
    clock_ascii[2] = "╠═══════════════════════════════════════════════════════════════════════════════════╣"
    clock_ascii[3] = "║                                                                                   ║"
    clock_ascii[4] = "║                                                                                  ║"
    clock_ascii[5] = "║       | -  =  - | -  =  - | -  =  - | -  =  - | -  =  - |         TUNE (.5 MHz)   ║"
    clock_ascii[6] = "║                                                                     _________     ║"
    clock_ascii[7] = "║  FM  90.       92.       94.       96.       98.       100. MHz    |    o    |    ║"
    clock_ascii[8] = "║                                                                    |         |    ║"
    clock_ascii[9] = "║                           -  ---     ---  ---                      |         |    ║"
    clock_ascii[10] = "║        [am]               |  | |  o    |  | |                      |         |    ║"
    clock_ascii[11] = "║                           |  | |     ---  ---                      |_________|    ║"
    clock_ascii[12] = "║        [  ]               |  | |  o  |    | |                                     ║"
    clock_ascii[13] = "║                           -  ---     ---  ---                                     ║"
    clock_ascii[14] = "╚═══════════════════════════════════════════════════════════════════════════════════╝"
    clock_ascii[15] = "    ╚══════╝                                                             ╚══════╝\n"

    return clock_ascii


def print_clock(clock_ascii, freq, freq_pairs):
    # place slider on the line
    freq_slider_string = clock_ascii[4][:freq_pairs[freq]] + '█' + clock_ascii[4][freq_pairs[freq]:]

    # print the lines above the slider line
    for i in range(0,4):
        print(clock_ascii[i])

    # print the slider line
    print(freq_slider_string)

    # print the lines below the slider line
    for i in range(5, 16):
        print(clock_ascii[i])


def story_intro(img_locked, img_alarm_clock, clock_ascii, freq_pairs):
    # introduce setting
    print("\nYou wake up in a room with concrete walls. The door to exit is locked. There is a window, but you can tell you are many stories up.\n")
    sleep(5)

    # show lock
    cv2.imshow('The door is locked.', img_locked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("You try a few combinations, but none seem to work.\n")
    sleep(3.5)

    # introduce clock
    print("As you look for the code within the room, you notice a faint hissing sound behind you.\n")
    sleep(4.5)

    # print clock, then show image to help player
    freq = 96.5
    print_clock(clock_ascii, freq, freq_pairs)

    # show clock
    cv2.imshow('An alarm clock sits on a worn wooden table near the window.', img_alarm_clock)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def puzzle_tutorial(player_name, clock_ascii, freq_pairs):
    # introduce clock puzzle
    print("After searching the room a few minutes longer, confused, you sit next to the clock and listen.\n")
    sleep(5)

    # print 96.5MHz string
    print("from radio: -===-=--n-=-=--=-==-=-=-=-i=--==--=-=-=-=-=-==---=-=-=-=-==---=-=-===v=-=-=-=--==-=-=--=-===-=--==-=-===-==--=n--=-=-=---\n")
    sleep(3)

    print("It's mostly noise. It would be nice to sleep to if you have to stay overnight...\n")
    sleep(5)

    # set starting freq = 96.5
    freq = 96.5
    print_clock(clock_ascii, freq, freq_pairs)
    sleep(3)

    print("You mess with the dial, setting the frequency to 97.0MHz.\n")
    sleep(3)

    # set new freq = 97.0
    freq = 97.0
    print_clock(clock_ascii, freq, freq_pairs)
    sleep(5)

    # print 97.0MHz string
    print("from radio: -=t-n=-on=-=-ere=-==a=mi-=i-=-p=rson-=-=th-=-ame=---=-=-=-=-=f==ou-hav-===y=-=-orm--==-=-p-eas===-nta==-Em=r=-nc----rvic=--\n")
    sleep(6)

    print("You rotate the dial to the right even more, setting the frequency to 97.5MHz. The signal seems to be improving in this direction.\n")
    sleep(7)

    # adjust clock to 10:29
    clock_ascii[12] = "║        [  ]               |  | |  o  |      |                                     ║"

    # set new freq = 97.5
    freq = 97.5
    print_clock(clock_ascii, freq, freq_pairs)
    sleep(6)

    print(f"from radio: Attention! There is a missing person by the name of {player_name}. If you have any information, please contact Emergency Services.\n")
    sleep(7)

    print("It sounds like there are people searching for you, but you doubt they'll be able to find you in this room.\n")
    sleep(6)

    print("There are lots of other frequencies. You might be able to gather some clues to escape this room.\n")
    sleep(6)

    print("Using the tuner you can set the alarm clock to frequencies between 90.0 and 100.0 in increments of 0.5.\n")
    sleep(5)


def puzzle_loop(allowed_freq, clock_ascii, freq_pairs, server_ip, server_port, client_socket):
    # create progress check to move to open the lock
    progress_check = [0, 0, 0]

    # adjust clock time
    clock_ascii[10] = "║        [am]               |  | |  o    |  | |                      |         |    ║"
    clock_ascii[11] = "║                           |  | |     ---  | |                      |_________|    ║"
    clock_ascii[12] = "║        [  ]               |  | |  o    |  | |                                     ║"

    # start puzzle loop, stopping when all clues have been found (91.0, 93.5, 99.0)
    while True:
        # error handling prior to sending frequency to server
        while True:
            # get new frequency from player
            new_freq = input("You listen to the radio for a moment after tuning it to: ")
            print("")

            # ensure entered frequency can become a float
            try:
                new_freq = float(new_freq)
            except ValueError:
                print("After thinking about it, you aren't sure the receiver will accept that frequency.\n")
                continue

            # ensure entered frequency is on the clock
            if new_freq not in allowed_freq:
                print("After thinking about it, you aren't sure the receiver will accept that frequency.\n")
                continue
            else:
                break

        # print clock with new frequency
        print_clock(clock_ascii, new_freq, freq_pairs)
        sleep(5)

        # convert frequency float to string
        new_freq = str(new_freq)

        # send frequency string to radio tower (server)
        client_socket.sendto(new_freq.encode(), (server_ip, server_port))

        # receive radio transmission
        radio_transmission, server_address = client_socket.recvfrom(2048)

        # print radio transmission
        print(radio_transmission.decode())
        sleep(1)

        # if 91.0MHz is heard, then the first number clue has been accessed
        if new_freq == "91.0":
            progress_check[0] = 1

        # if 91.0MHz is heard, then the first number clue has been accessed
        if new_freq == "93.5":
            progress_check[1] = 1

        # if 91.0MHz is heard, then the first number clue has been accessed
        if new_freq == "99.0":
            progress_check[2] = 1

        if sum(progress_check) == 3:
            sleep(1)
            return None


def conclude_story(img_locked, img_unlocked):
    # end clock puzzle and move to solve lock
    print("After thinking about what you heard on the radio, you stand up and walk over to the lock.\n")
    sleep(4)

    # show locked lock
    cv2.imshow('The door is still locked.', img_locked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # lists for checking player answers
    player_nums = [" ", " ", " "]
    correct_nums = ["22", "19", "3"]

    while True:
        # prompt player for lock sequence
        print("You try a new sequence of numbers on the lock.\n")
        sleep(1)

        player_nums[0] = input("First, you twist the lock to the right, stopping on the number: ")
        print("")

        player_nums[1] = input("Then, you twist the lock to the left, stopping on the number: ")
        print("")

        player_nums[2] = input("Finally, you twist the lock to the right, stopping on the number: ")
        print("")

        # check answers
        if player_nums == correct_nums:
            break
        else:
            print("That didn't work.\n")
            sleep(1)

    # show unlocked lock
    cv2.imshow('The lock opened.', img_unlocked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("You open the door and escape, never to return to this mysterious place.\n")
    sleep(3)


def main():
    ############################## 0 - prepping variables ##############################

    # get story images
    img_locked, img_alarm_clock, img_unlocked = load_images()

    # get frequency dictionary and list
    freq_pairs, allowed_freq = build_freq_dict_list()

    # get clock ascii art
    clock_ascii = build_clock()

    # get udp socket information
    server_ip, server_port, client_socket = connection_info()

    ############################## 1 - story intro ##############################

    # get player name for immersion
    player_name = input("Enter your name: ")

    # run story intro
    story_intro(img_locked, img_alarm_clock, clock_ascii, freq_pairs)

    ############################## 2 - start puzzle tutorial ##############################

    # run puzzle tutorial
    puzzle_tutorial(player_name, clock_ascii, freq_pairs)

    ############################## 3 - run puzzle loop ##############################

    # run puzzle loop with udp
    puzzle_loop(allowed_freq, clock_ascii, freq_pairs, server_ip, server_port, client_socket)

    # close udp connection when loop is broken
    client_socket.close()

    ############################## 4 - go to unlock ##############################

    # go to lock to solve puzzle
    conclude_story(img_locked, img_unlocked)


if __name__ == '__main__':
    main()
