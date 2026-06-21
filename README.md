# Password Strength Analyzer

## What is this project?

This is a simple Python project I built while learning cybersecurity. 
It checks how strong a password is by scanning for different character types.

I built this because in my cybersecurity class, my sir explained that 
most attacks happen because of weak passwords. So I wanted to build 
a tool that actually checks password strength.

## What it checks

- Does the password have capital letters?
- Does it have small letters?
- Does it have numbers?
- Does it have special characters like @, #, $?
- Is it at least 8 characters long?

Each check gives 1 point. Total score is out of 5.

## How to run this

You need Python installed on your computer.

Open terminal and type:
python password_checker_analyser.py

Then enter your password when it asks.

## Output example
Score    : 4 out of 5

[PASS] Contains uppercase letter

[PASS] Contains lowercase letter

[PASS] Contains number

[FAIL] No special character found

[PASS] Length is 8 or more characters
RESULT   : GOOD - Almost there, one more improvement!

## What I used

- Python 3
- re module (Regular Expressions)

## What I learned from this

Before building this I didn't know what Regular Expressions were.
After this project I understand how to use re.search() to find 
patterns inside a string. I also understood why security tools 
check passwords the way they do.

## What I want to add next

- Check if the password is in a list of common passwords
- Show how long it would take a hacker to crack this password
- Build a simple GUI for this

## About me

I am Dharshini S R, a 3rd year Cybersecurity student.
This is one of my first Python projects in cybersecurity.
