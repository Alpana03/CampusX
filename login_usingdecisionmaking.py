# Login using decision making:
# Take email and password from user, and take static email and password to check with user input
# Check, if "@" is present in the email, if not then print "@ is missing in email address."
# Check, if email and password is correct then print "Welcome"
# Check, if email is correct but password is wrong then print "Incorrect Password" and ask for password again
# Check if email and password is wrong then print "Login failed"
# Check if email is correct and password is wrong again then print "Again wrong password.Login failed."

Email = input("Please enter Email: ")
if "@" not in Email:
		print("@ is missing in email address.")
Email = input("Please enter Email again: ")
Password = (input("Please enter Password: "))
if Email == "campusx@gmail.com" and Password == "1234":
	print("Welcome")
elif Email == "campusx@gmail.com" and Password != "1234":
    print("Incorrect Password")
    Password = input("Enter Password again: ")
    if Password == "1234":
        print("Now, password is correct. Welcome")
    else:
        print("Again wrong password. Login failed.")
else:
    print("Login failed")