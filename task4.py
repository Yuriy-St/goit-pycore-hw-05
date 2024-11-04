import re
from typing import Callable
from colorama import Fore


# Regular exception to test phone numbers (first approach, just for testing)
PHONE_REGEXP = r"\d{4,10}$"


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return log_error("Enter the all arguments")
        except KeyError:
            return log_error("Contact not found")
        except IndexError:
            return log_error("Enter correct data")
        except Exception as e:
            return e

    return inner


def log_info(msg: str) -> str:
    return f"{Fore.BLUE}{msg}{Fore.RESET}"


def log_error(msg: str) -> str:
    return f"{Fore.RED}{msg}{Fore.RESET}"


def validate_phone(phone: str):
    match = re.match(PHONE_REGEXP, phone)

    if not bool(match):
        raise Exception(log_error("The phone number must consist of only 4-10 digits"))


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    validate_phone(phone)

    if any(name == key for key in contacts.keys()):
        raise Exception(log_error("Name already in the list"))

    contacts[name] = phone

    return log_info("Contact added")


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args

    validate_phone(phone)

    if name not in contacts.keys():
        raise KeyError

    contacts[name] = phone
    return "Contact changed"


@input_error
def show_phone(args: list, contacts: dict) -> str:
    name, *rest = args

    return contacts[name]


@input_error
def show_all(contacts: dict):
    if len(contacts) == 0:
        print(log_error("The list is empty"))

    for user in contacts.keys():
        print(f"{Fore.GREEN}{user}: {Fore.GREEN}{contacts[user]}")


def main():
    contacts = {}
    print(f"{Fore.MAGENTA}Welcome to the assistant bot!")
    while True:
        user_input = (
            input(f"{Fore.YELLOW}Enter a command: {Fore.GREEN}").strip().lower()
        )
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print(f"{Fore.RED}Invalid command")


if __name__ == "__main__":
    main()
