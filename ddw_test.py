from dw import Interval
from os import remove, system

FILE="testo.tsv"
LINES=6

system(f"touch {FILE}")


x = Interval("deep", 12, "test")

print("Printing and instance of interval")
print(x)

for i in range(6):
    x.write(f"{FILE}")

print("Cat the file:")
system(f"cat {FILE}")

print("Number of lines is:")
system(f"wc -l {FILE}")
print(f"And it must be {LINES}")

remove(f"{FILE}")