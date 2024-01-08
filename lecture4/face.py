import sys
from sayings import say_goodbye, say_hello

if len(sys.argv) == 2:
    say_goodbye(sys.argv[1])