"""Sample app that imports and uses the custom MyModule."""

import sys
from pathlib import Path

# Add project root to sys.path so that MyModule can be imported
sys.path.append(str(Path(__file__).resolve().parents[2]))

from MyModule import say_hello


def main():
    message = say_hello("World")
    print(message)


if __name__ == "__main__":
    main()
