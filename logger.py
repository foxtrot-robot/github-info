try:
    from colorama import Fore, Back, Style
except ImportError as e:
    print(f"Error catched {e}")
    print("Dependency's error please execute following line in your terminal")
    print("pip3 install -r requirements.txt")
class logger:
    def log(text):
        print(f"{Fore.CYAN}[LOG] {Fore.GREEN} {text}")
    def error(text):
        print(f"{Fore.RED}[ERROR] {Fore.GREEN} {text}")
    def find(text):
        print(f"{Fore.GREEN}[FOUND] {Fore.CYAN} {text}")