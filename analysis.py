import os
import sys

def test():
    """A simple test function to show Ruff everything is used."""
    print(f"Running on platform: {sys.platform}")
    print(f"Current directory: {os.getcwd()}")
    print("This is finally fixed!")

if __name__ == "__main__":
    test()
