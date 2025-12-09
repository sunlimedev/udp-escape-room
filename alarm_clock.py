clock_ascii = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

clock_ascii[0]= "╔═══════════════════════════════════════════════════════════════════════════════════╗"
clock_ascii[1]= "║     CASIO    Alarm Clock w/ FM Receiver                                           ║"
clock_ascii[2]= "╠═══════════════════════════════════════════════════════════════════════════════════╣"
clock_ascii[3]= "║                                                                                   ║"
clock_ascii[4]= "║                                                                                  ║"
clock_ascii[5]= "║       | -  -  - | -  -  - | -  -  - | -  -  - | -  -  - |         TUNE (.5 MHz)   ║"
clock_ascii[6]= "║                                                                     _________     ║"
clock_ascii[7]= "║  FM  90.       92.       94.       96.       98.       100. MHz    |    O    |    ║"
clock_ascii[8]= "║                                                                    |         |    ║"
clock_ascii[9]= "║                           -  ---     ---  ---                      |         |    ║"
clock_ascii[10]="║        [am]               |  | |  o    |  | |                      |         |    ║"
clock_ascii[11]="║                           |  | |     ---  ---                      |_________|    ║"
clock_ascii[12]="║        [  ]               |  | |  o  |    | |                                     ║"
clock_ascii[13]="║                           -  ---     ---  ---                                     ║"
clock_ascii[14]="╚═══════════════════════════════════════════════════════════════════════════════════╝"

freq = 91.5

freq_pairs = {
    90.0 : 8,  #
    90.5 : 10,
    91.0 : 13,
    91.5 : 16,
    92.0 : 18,  #
    92.5 : 20,
    93.0 : 23,
    93.5 : 26,
    94.0 : 28,  #
    94.5 : 30,
    95.0 : 33,
    95.5 : 36,
    96.0 : 38,  #
    96.5 : 40,
    97.0 : 43,
    97.5 : 46,
    98.0 : 48,  #
    98.5 : 50,
    99.0 : 53,
    99.5 : 56,
    100.0 : 58
}

clock_ascii[4] = clock_ascii[4][:freq_pairs[freq]] + 'o' + clock_ascii[4][freq_pairs[freq]:]

for i in range(len(clock_ascii)):
    print(clock_ascii[i])