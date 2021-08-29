"""
                                    control flow --  Loops

while loop
"""
i = 34
while i < 40:
    print(i)
    i += 1         # this increments the loop variable after each loop


print("\n")
"""
for loop
for i in range(stop),   for i in range(start, stop),    for i in range(start, stop, step)
in for loop, the loop variable is incremented automatically
"""

for i in range(10):        # NB:start at 0 and ends at stop-1 i.e 9
    print(i)

for b in range(12, 16):
    print(b)

# simple program

text = input("enter text: ")

for index in range(len(text)):                             # using indexing
    if text[index] == 'i' or text[index] == 'u':
        print("there is an i or u")

for char in text:                                       # NB: this iterates over every element in text
    if char == 'i' or char == 'u':
        print("there is an i or u")