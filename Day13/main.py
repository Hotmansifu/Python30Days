def email_slicer(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    print("Username:", username)
    print("Domain:", domain)

    message = f"Hello host,\n\nI am contacting you regarding your website at {domain}. I noticed that my username for the site is {username}. Is there any way to change it to my preferred username?\n\nThank you,\n{username}"
    print("\nMessage:\n", message)

email_slicer("john.doe@example.com")
