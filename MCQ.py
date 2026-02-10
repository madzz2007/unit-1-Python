score = 0

print("Welcome to the Python MCQ Quiz")
print("Answer by typing a, b, c, or d\n")

print("1. What is the output of print(2 + 3 * 4)?")
print("a) 20\nb) 14\nc) 24\nd) 10")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n2. Which keyword is used to define a function in Python?")
print("a) define\nb) func\nc) def\nd) function")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n3. What is the correct file extension for Python files?")
print("a) .pt\nb) .py\nc) .pyt\nd) .python")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n4. Which data type is immutable?")
print("a) list\nb) set\nc) dictionary\nd) tuple")
ans = input("Your answer: ")
if ans == "d":
    score += 1

print("\n5. What does len() do?")
print("a) adds elements\nb) deletes elements\nc) returns length\nd) stops program")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n6. Which symbol is used for comments in Python?")
print("a) //\nb) /*\nc) #\nd) <!--")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n7. What is the output of print(type(10))?")
print("a) int\nb) <class 'int'>\nc) integer\nd) number")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n8. Which loop is used when number of iterations is unknown?")
print("a) for\nb) while\nc) do-while\nd) repeat")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n9. What does input() function return?")
print("a) int\nb) float\nc) string\nd) boolean")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n10. Which operator is used for exponentiation?")
print("a) ^\nb) **\nc) //\nd) %")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n11. Which keyword is used for decision making?")
print("a) for\nb) while\nc) if\nd) switch")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n12. What is the output of bool(0)?")
print("a) True\nb) False\nc) 0\nd) Error")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n13. Which function converts string to integer?")
print("a) str()\nb) float()\nc) int()\nd) bool()")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n14. Which keyword is used to exit a loop?")
print("a) stop\nb) exit\nc) break\nd) return")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n15. What is the output of print(5 // 2)?")
print("a) 2.5\nb) 3\nc) 2\nd) 2.0")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n16. Which data type stores key-value pairs?")
print("a) list\nb) tuple\nc) dictionary\nd) set")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("\n17. What does range(3) return?")
print("a) 1,2,3\nb) 0,1,2\nc) 0,1,2,3\nd) 1,2")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\n18. Which operator is used for logical AND?")
print("a) &&\nb) AND\nc) &\nd) and")
ans = input("Your answer: ")
if ans == "d":
    score += 1

print("\n19. What is the output of print(type([]))?")
print("a) <class 'list'>\nb) list\nc) array\nd) <list>")
ans = input("Your answer: ")
if ans == "a":
    score += 1

print("\n20. Which statement is used to handle conditions?")
print("a) loop\nb) if-else\nc) function\nd) class")
ans = input("Your answer: ")
if ans == "b":
    score += 1

print("\nQuiz Completed")
print("Total Correct Answers:", score, "out of 20")
