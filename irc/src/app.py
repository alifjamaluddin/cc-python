import socket
import threading

HOST = "irc.freenode.net"
PORT = 6667


channels = []

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Welcome to IRC Client")
nickname = input("Choose your nickname: ")
realname = input("What is your realname? ")

# registration
nick_reg = f"NICK {nickname} \r\n"
name_reg = f"USER guest 0 * :{realname} \r\n"
client.send(nick_reg.encode())
client.send(name_reg.encode())

def receive():
    while True:
        try:
            stream = client.recv(1024).decode("utf-8")
            messages = stream.split('\r\n')
            for message in messages:
                if len(message) > 0:
                    if "PING" in message: handle_ping(message + "\r\n") 
                    elif nickname in message: handle_server_message(message)
                    elif "NOTICE" in message: handle_server_message(message)
                    elif "PRIVMSG" in message: handle_private_message(message)
                    elif "Closing link" in message: exit(1)
                    else: parse_message(message)
        except Exception:
            client.close()
            break

def handle_server_message(message):
    clean_message = message.split(':')
    if len(clean_message) > 0:
        print(f"{clean_message[-1]}")

def handle_private_message(message):
    info = message.split(':')[1].split(" ")

    content = "".join(message.split(':')[2:])
    channel_name = info[2]
    user = info[0]
    print(f"[{channel_name}] ({user}) : {content}")

def handle_ping(message):
    pong_msg = f"PONG{message[4:]}"
    client.send(pong_msg.encode()) 

def parse_message(message):
    print(f"{message}")


def write():
    while True:
        message = input()
        if message[:4] == "JOIN":
            client.send(f"{message} \r\n".encode())
            channels.append(message[4:].strip())
        elif message[:4] == "PART":
            client.send(f"{message} \r\n".encode())
            channels.remove(message[4:].strip())
        elif "CHANNELS" in message:
            print(channels)
        elif "NICK" in message:
            client.send(f"{message} \r\n".encode())
            nickname = message.split(" ")[-1].strip()
        elif "QUIT" in message:
            client.send(f"{message} :bye\r\n".encode())
            print("bye2")
            break
        else:        
            print(f"WRONG COMMAND: JOIN | PART | CHANNELS | NICK | QUIT")



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


