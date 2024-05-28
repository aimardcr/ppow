from pow import Challenge, check

challenge = Challenge.generate(5000)
print(f"curl -sSfL https://pwn.red/pow | sh -s { challenge }\n\n")

sol = input("Solution: ")
if check(challenge, sol):
    print("Corrent!")
else:
    print("Incorrect!")