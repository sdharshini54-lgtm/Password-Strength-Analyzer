import re

password = input("Enter your password: ")

score = 0
feedback = []


if re.search(r'[A-Z]', password):
    score += 1
    feedback.append("[PASS] Contains uppercase letter")
else:
    feedback.append("[FAIL] No uppercase letter found")


if re.search(r'[a-z]', password):
    score += 1
    feedback.append("[PASS] Contains lowercase letter")
else:
    feedback.append("[FAIL] No lowercase letter found")


if re.search(r'[0-9]', password):
    score += 1
    feedback.append("[PASS] Contains number")
else:
    feedback.append("[FAIL] No number found")


if re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password):
    score += 1
    feedback.append("[PASS] Contains special character")
else:
    feedback.append("[FAIL] No special character found")


if len(password) >= 8:
    score += 1
    feedback.append("[PASS] Length is 8 or more characters")
else:
    feedback.append("[FAIL] Password too short - minimum 8 characters needed")


print("")
print("========================================")
print("       PASSWORD STRENGTH ANALYZER       ")
print("========================================")
print("Password : " + ("*" * len(password)))
print("Score    : " + str(score) + " out of 5")
print("----------------------------------------")

for item in feedback:
    print("  " + item)

print("----------------------------------------")

if score == 5:
    print("RESULT   : STRONG - Your password is secure!")
elif score == 4:
    print("RESULT   : GOOD - Almost there, one more improvement!")
elif score == 3:
    print("RESULT   : MEDIUM - Please strengthen your password!")
elif score == 2:
    print("RESULT   : WEAK - Your password needs improvement!")
else:
    print("RESULT   : VERY WEAK - Please change your password!")

print("========================================")      