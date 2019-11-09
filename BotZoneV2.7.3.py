from colorama import init, Fore, Back, Style
import commands
import config
import sys
import os
import webbrowser


# Coloroma autoreset
init(autoreset=True)
if not os.path.isdir("Saves"):
    try:
        os.mkdir('Saves')
        os.mkdir('Saves/ios')
        os.mkdir('Saves/android')
        os.mkdir('Saves/Jp')
        os.mkdir('Saves/Jp/ios')
        os.mkdir('Saves/Jp/android')
        os.mkdir('Saves/fresh')
        os.mkdir('Saves/fresh/ios')
        os.mkdir('Saves/fresh/android')
    except:
        print(Fore.RED + Style.BRIGHT + 'Unable to create saves file')

while True:

    # Decide which client to use.
    print(' ')
    print("   ___       __ ____     ")   
    print("  / _ )___  / //_  / ___  ___  ___ ")
    print(" / _  / _ \/ __// /_/ _ \/ _ \/ -_)")
    print("/____/\___/\__//___/\___/_//_/\__/")
                                   
    print('Choose a version')
    print('---------------------------------')
    print(' ')
    while True:
        print('Which version? (' + 'Jp: 1 ' + 'or ' 'Global: 2' ')',end='')
        client = input(" ")
        if client.lower() == '1':
            config.client = 'japan'
            while True:
                print("   ___       __ ____     ")   
                print("  / _ )___  / //_  / ___  ___  ___ ")
                print(" / _  / _ \/ __// /_/ _ \/ _ \/ -_)")
                print("/____/\___/\__//___/\___/_//_/\__/") 
                print("-----------------------------------") 
                print("Possible by SomeNi")               
                print(" ")
                print("[ Status ] -> You're curently on JP")
                print(" ")
                print("[ 0 ] -> New Account")
                print("[ 1 ] -> Transfer Account")
                print("[ 2 ] -> Load From Save")
                print("[ 3 ] -> Daily Logins")
                print("[ 4 ] -> Update Both DataBase")
                print("[ 5 ] -> BotZone Discord Link")
                print("[ 6 ] -> Update Glb DataBase")
                print("[ 7 ] -> Update JP DataBase")
                print(" ")

                command = input('Enter your choice: ')
                if command == '0':
                    print(' ')
                    config.identifier = commands.signup()
                    commands.Jp_save_account()
                    config.access_token, config.secret = commands.signin(config.identifier)
                    commands.tutorial()
                    commands.daily_login()
                    break
                elif command == '1':
                    print(' ')
                    commands.Jp_transfer_account()
                    commands.daily_login()
                    break
                elif command == '2':
                    print(' ')
                    commands.Jp_load_account()
                    commands.daily_login()
                    commands.accept_gifts()
                    commands.accept_missions()
                    break
                elif command == '3':
                    print('')
                    commands.Jp_bulk_daily_logins()
                    break
                elif command == '4':
                    print('')
                    commands.db_download()
                elif command == '6':
                	commamds.glb_db_dowmload()
                elif command == '7':
                	commands.jp_db_download()
                elif command == '5':
                    webbrowser.open(commands.discordurl, new=0, autoraise=True)
                elif command == 'exit':
                    exit()
                else:
                    print(Fore.RED + Style.BRIGHT + "Command not understood")

                # User commands.
            while True:
                print('---------------------------------')
                print(
                        Fore.CYAN + Style.BRIGHT + "Type" + Fore.YELLOW + Style.BRIGHT + " 'help'" + Fore.CYAN + Style.BRIGHT + " to view all commands.")

                # Set up comma separated chain commands. Handled via stdin
                try:
                    command = input()
                except:
                    sys.stdin = sys.__stdin__
                    command = input()

                if command == 'exit':
                    break
                # Pass command to command executor and handle keyboard interrupts.
                try:
                    commands.user_command_executor(command)
                except KeyboardInterrupt:
                    print(Fore.CYAN + Style.BRIGHT + 'User interrupted process.')
                except Exception as e:
                    print(Fore.RED + Style.BRIGHT + repr(e))
            break
        elif client.lower() == '2':
            config.client = 'global'
            print(' ')
            while True:
                print("   ___       __ ____     ")   
                print("  / _ )___  / //_  / ___  ___  ___ ")
                print(" / _  / _ \/ __// /_/ _ \/ _ \/ -_)")
                print("/____/\___/\__//___/\___/_//_/\__/") 
                print("-----------------------------------") 
                              
                print(" ")
                print("[ Status ] -> You're curently on Global")
                print(" ")
                print("[ 0 ] -> New Account")
                print("[ 1 ] -> Transfer Account")
                print("[ 2 ] -> Load From Save")
                print("[ 3 ] -> Load Fresh Account")
                print("[ 4 ] -> New Fresh Account")
                print("[ 5 ] -> Update Both DataBase")
                print("[ 6 ] -> BotZone Discord Link")
                print("[ 7 ] -> Update Glb DataBase")
                print("[ 8 ] -> Update JP DataBase")
                print(" ")

                command = input('Enter your choice: ')
                if command == '0':
                    print(' ')
                    config.identifier = commands.signup()
                    commands.save_account()
                    config.access_token, config.secret = commands.signin(config.identifier)
                    commands.tutorial()
                    commands.daily_login()
                    break
                elif command == '1':
                    print(' ')
                    commands.transfer_account()
                    commands.daily_login()
                    break
                elif command == '2':
                    print(' ')
                    commands.load_account()
                    commands.daily_login()
                    commands.accept_gifts()
                    commands.accept_missions()
                    break
                elif command == '4':
                    print(' ')
                    config.identifier = commands.signup()
                    commands.fresh_save_account()
                    config.access_token, config.secret = commands.signin(config.identifier)
                    commands.tutorial()
                    commands.daily_login()
                    break
                elif command == '3':
                    print(' ')
                    commands.fresh_load_account()
                    commands.daily_login()
                    commands.accept_gifts()
                    commands.accept_missions()
                    break
                elif command == '5':
                    print(' ')
                    commands.db_download()
                elif command == '7':
                	commands.glb_db_download()
                elif command == '8':
                	commands.jp_db_download()
                elif command == '6':
                    webbrowser.open(commands.discordurl, new=0, autoraise=True)
                elif command == 'exit':
                    exit()
                else:
                    print(Fore.RED + Style.BRIGHT + "Command not understood")

            # User commands.
            while True:
                print('---------------------------------')
                print(
                             "Type" + " 'help'" + " to view all commands.")

                # Set up comma separated chain commands. Handled via stdin
                try:
                    command = input()
                except:
                    sys.stdin = sys.__stdin__
                    command = input()

                if command == 'exit':
                    break
                # Pass command to command executor and handle keyboard interrupts.
                try:
                    commands.user_command_executor(command)
                except KeyboardInterrupt:
                    print(Fore.CYAN + Style.BRIGHT + 'User interrupted process.')
                except Exception as e:
                    print(Fore.RED + Style.BRIGHT + repr(e))

            break
        else:
            print(Fore.RED + Style.BRIGHT + "Command not understood")
