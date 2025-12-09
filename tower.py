from socket import *

server_port = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', server_port))

print('The radio tower is transmitting on several frequencies.')

transmission_pairs = {
    90.0 : "from radio: -=s-=-o-==-h=--y=-i-=-da-==Ju=-==o=-==-=-=-o-=-a-l=--==-f-=-=a=bu=-=-e-=-=t--\n",
    90.5 : "from radio: -=sh=-o-=a-h=-py=-ir=hda-==Ju=-==o=-yo-=-=ro-=-ayl=---wif-=-=a=bu=-=Re-=-=t-s\n",
    91.0 : "from radio: wish you a happy birthday! Just for you, from Taylor Swift's album, Red, it's\n",
    91.5 : "from radio: -=sh=-o-=a-h=-py=-ir=hda-==Ju=-==o=-yo-=-=ro-=-ayl=---wif-=-=a=bu=-=Re-=-=t-s\n",
    92.0 : "from radio: -=s-=-o-==-h=--y=-i-=-da-==Ju=-==o=-==-=-=-o-=-a-l=--==-f-=-=a\n",
    92.5 : "from radio: nos=a=ogo=-ha-=y--i-=pds=ngJuf-1==o-==--=-=o==-\n",
    93.0 : "from radio: no=-a--go-==a--th--=-p=s-ng-=f=1-\n",
    93.5 : "from radio: not as good as the top song of 19\n",
    94.0 : "from radio: no=-a--go-==a--th--=-p=s-ng-=f=1-\n",
    94.5 : "from radio: -o-=a===-==--==th--=-=-s-=g--==1==-=-\n",
    95.0 : "from radio: -=-=a===-==--==th--=-=-=-=g--==-==-==-==-\n",
    95.5 : "from radio: -=-=-===-==--==-h--=-=-=-==--==-==-==-==-==--\n",
    96.0 : "from radio: -=-=-===-==--==-=--=-=-=-==--==-==-==-==-==-==--\n",
    96.5 : "from radio: -=-=-===-==--==-=--=-=-=-==--==-==-==-==-==-==-==--\n",
    97.0 : "from radio: -=-=-===-==--==-=--=-=-=-==--==-==-==-==-==-==-==-==-\n",
    97.5 : "from radio: -==-=--=-===-D=-=-=-=-=-=--====---=-=-==-==-=-=x=-==--\n\nThe emergency transmission stopped playing on this frequency. Nobody is looking for you anymore.\n",
    98.0 : "from radio: -==-=--t-=-=-D-=--=-==-=-=-=h-=-a==-=-==---=--=xt-=-=--\n",
    98.5 : "from radio: an=-=hat-=-s-De=--=Sou-=-=-Th-=-=gic=-u-be-=--=xt-=-=i-\n",
    99.0 : "from radio: and that was De La Soul's, The Magic Number. Next up is\n",
    99.5 : "from radio: an=-=hat-=-s-De=--=Sou-=-=-Th-=-=gic=-u-be-=--=xt-=-=i-\n",
    100.0: "from radio: -==-=--t-=-=-=-=--=-==-=-=-=h-=-a==-=-==---=--=-=-=-=--\n"
}

while True:
    freq, client_address = server_socket.recvfrom(2048)
    radio_transmission = transmission_pairs[float(freq.decode())]
    server_socket.sendto(radio_transmission.encode(), client_address)
