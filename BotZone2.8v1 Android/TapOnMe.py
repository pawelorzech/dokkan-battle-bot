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
    print(Fore.CYAN + Style.BRIGHT + 'Choose a version')
    print('---------------------------------')
    print(' ')
    while True:
        print('Which version? (' + Fore.YELLOW + Style.BRIGHT + 'Jp: 1 ' + Style.RESET_ALL + 'or ' + Fore.YELLOW + Style.BRIGHT + 'Global: 2' + Style.RESET_ALL + ')',end='')
        client = input(" ")
        if client.lower() == '1':
            config.client = 'japan'
            while True:
                print(Fore.CYAN + Style.BRIGHT + 'Enter The BotZone ')
                print('---------------------------------')
                print("You're currently on JP")
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'New Account :' + Fore.YELLOW + Style.BRIGHT + ' 0')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Transfer Account :' + Fore.YELLOW + Style.BRIGHT + ' 1')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Load From Save :' + Fore.YELLOW + Style.BRIGHT + ' 2')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Daily Login :' + Fore.YELLOW + Style.BRIGHT + ' 3')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Update database:' + Fore.YELLOW + Style.BRIGHT + ' 4')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'BotZone Discord Link:' + Fore.YELLOW + Style.BRIGHT + ' 5')
                print('---------------------------------')
                print(' ')
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
                print(Fore.CYAN + Style.BRIGHT + 'Enter The BotZone ')
                print('---------------------------------')
                print("You're currently on GLB")
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'New Account :' + Fore.YELLOW + Style.BRIGHT + ' 0')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Transfer Account :' + Fore.YELLOW + Style.BRIGHT + ' 1')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Load From Save :' + Fore.YELLOW + Style.BRIGHT + ' 2')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'New Fresh Account :' + Fore.YELLOW + Style.BRIGHT + ' 3')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Load Fresh Account :' + Fore.YELLOW + Style.BRIGHT + ' 4')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Daily Login :' + Fore.YELLOW + Style.BRIGHT + ' 5')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'Update database:' + Fore.YELLOW + Style.BRIGHT + ' 6')
                print('---------------------------------')
                print(Fore.CYAN + Style.BRIGHT + 'BotZone Discord Link:' + Fore.YELLOW + Style.BRIGHT + ' 7')
                print('---------------------------------')
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
                elif command == '3':
                    print(' ')
                    config.identifier = commands.signup()
                    commands.fresh_save_account()
                    config.access_token, config.secret = commands.signin(config.identifier)
                    commands.tutorial()
                    commands.daily_login()
                    break
                elif command == '4':
                    print(' ')
                    commands.fresh_load_account()
                    commands.daily_login()
                    commands.accept_gifts()
                    commands.accept_missions()
                    break
                elif command == '5':
                    print('')
                    commands.bulk_daily_logins()
                    commands.fresh_bulk_daily_logins()
                elif command == '6':
                    print('')
                    commands.db_download()
                elif command == '7':
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
        else:
            print(Fore.RED + Style.BRIGHT + "Command not understood")
