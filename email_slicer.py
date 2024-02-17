def sliceEmail():
    email = input("Enter your email address: ")
    if "@" in email:
        (username, domain) = email.split("@")

        if "." in domain:
            (domain, extension) = domain.split(".")
        else:
            extension = "none"
    else:
        if "." in email:
            (domain, extension) = email.split(".")
            username = "none"
        else:
            username = email
            domain = "none"
            extension = "none"

    
    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)

sliceEmail()