from win10toast import ToastNotifier
import socket
import time
import re


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'test_boot'
token = 'oauth:ll7ux5exfrddog2qu0q2x83kzh6m3o'
channel = '#notepidemic'

sock = socket.socket()

sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

connected = False
run = True

while run:
    response = sock.recv(2048).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        print('Pong')
    else:
        username = re.search(r"\w+", response).group(0)
        CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

        message = CHAT_MSG.sub("", response).rstrip('\n')

        if 'End of /NAMES list' in message:
            connected = True
            print('Listening to ', 'CHAN')

        if connected == True:
            if 'End of /NAMES list' in message:
                pass
            else:
                print(username.title() + ':', message)

            if 'test' in message:
                print("Hello World!")
                messageTemp = "PRIVMSG #" + channel + " :" + 'Hello Chat!'
                sock.send((messageTemp + "\r\n").encode("utf-8"))
            if 'join' in message:
                messageTemp = "JOIN #" + channel
                sock.send((messageTemp + "\r\n").encode("utf-8"))
                print("Joined")
            if 'part' in message:
                messageTemp = "PART #" + channel
                sock.send((messageTemp + "\r\n").encode("utf-8"))
                print("Parted")

        time.sleep(1 / 10)
