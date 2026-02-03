import time
import sys


# lines = [
#     "Don't you understand?"
#     "Don't you know the love that you want's all the love that you needed?"
#     "Gave me all you had"
#     "Gave me all the love that you want, all the love that you needed"
# ]

# for line in lines:
#     print(line)
#     time.sleep(10)  # delay in seconds



lines = [
    "Don't you understand?"
]

text = "Don't you understand?"

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.10)

# for i in range(5, 0, -1):
#     print(f"Starting in {i}...")
#     time.sleep(1)

# print(">>>>> Started!")
