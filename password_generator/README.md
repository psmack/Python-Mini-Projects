# password_generator
A simple password generator script.

## Usage
Password minimum length must be between 1 and 40.
```
python3 password_generator.py [-h] [-n] [-s] length
```

### Examples:
Generate password with minimum length of 20 characters.
```
python3 password_generator.py 20
Password is: ciQouTAfanapmSYQoEzm
```

Generate password with minimum length of 20 characters and include numbers.
```
python3 password_generator.py -n 20
Password is: Z2O6oM9g6oBiUbY4C5Gl
```

Generate password with minimum length of 20 characters and include special characters.
```
python3 password_generator.py -s 20
Password is: cERl`$/>*>!I@Co!S()m
```

Generate password with minimum length of 20 characters and include both numbers and special characters.
```
python3 password_generator.py -ns 20
Password is: TP#-![K*$!{"|aRtON=!G=^x7
```