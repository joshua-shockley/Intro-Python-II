import time
commands = {"love": "love hard and love fiercely. Otherwise what's the point",
            "life": 'life is life dude.... just go live it!',
            "money": "I really don't know what to tell you about money.... \n I don't have any either. :(",
            "fashion": "It's all bullshit really... But, there are some poorly designed styles out there, so really think it through.",
            "game play": 'follow the directions as you go. \nIt gets much easier if you read what the display asks for or shows as an option. \nMost commands are explained in the request. \n\n For a full list of the commands; after entering "help" enter "all possible commands". \nThis will show all commands whether for game play or help menu.', }


def help(user):
    time.sleep(1)
    h_cmd = input(
        f"{user}, what do you need help with?...\n\n examples: \n game play  all possible commands\n ----> ").lower()
    if h_cmd is None:
        print('you have to type something for me to know how to help...')
        time.sleep(1)
        help(user)
    elif h_cmd == "":
        print('you have to type something for me to know how to help...')
        time.sleep(1)
        help(user)
    elif h_cmd == "life":
        print('')
        time.sleep(1)
        print(commands["life"])
    elif h_cmd == "love":
        print(commands.get("love"))
    elif h_cmd == "money":
        print(commands["money"])
    elif h_cmd == "fashion":
        print(commands.get("fashion"))
    elif h_cmd == "game play":
        print(commands.get("game play"))
    elif h_cmd == "all possible commands":
        # make  a list of commands that do something and that it looks like a list
        print('commands list from up top under imports')
        for key, value in commands.items():
            print(f"{key:20}{value}")
