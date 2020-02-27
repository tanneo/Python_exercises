#while loops
#will keep executing code block under it as long as the Boolean expression is true
#use while loops sparingly. Usually for loops are better. While loops can sometimes keep running forever if condition never changes to false
#when in doubt print test variable at top and bottom of while loop to see what it is doing



while i < num:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)