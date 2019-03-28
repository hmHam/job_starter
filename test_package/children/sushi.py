import sys
import os

def hi():
    print(__file__)
    print(os.path.abspath(__file__))
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print("Hi I'm Sushi")
    print(os.pardir)
    sys.path.append(os.path.join(current_dir, os.pardir, os.pardir))
    from .. import main
    main.hi()