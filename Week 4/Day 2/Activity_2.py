import re

text = "Hello, World!"
pattern = r"Hello"
result = re.match(pattern, text)
if result:
    print("Pattern matched!")
