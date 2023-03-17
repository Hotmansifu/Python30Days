import whois

# Get the domain name from user input
domain_name = input("Enter a domain name: ")

# Retrieve information about the domain using whois
info = whois.whois(domain_name)

# Print the information
print("Domain Name:", info.domain_name)
print("Creation Date:", info.creation_date)
print("Expiration Date:", info.expiration_date)
print("Last Updated Date:", info.updated_date)
print("Registrar:", info.registrar)
print("Registrant Name:", info.name)
print("Registrant Email:", info.email)
