import sys
from bigcardorbit import check_bigcardorbit

RED = "\033[1;31m"
BLUE = "\033[1;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

sys.stdout.write(RED)


def main() -> None:
    print("\nStarting to check BigOrbitCards... \n")
    check_bigcardorbit()


if __name__ == "__main__":
    main()
