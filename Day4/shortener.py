import sys,requests
def shorten_link(full_link, link_name):
    API_KEY="" #Get and enter your API from https://cutt.ly
    BASE_URL="https://cutt.ly/api/api.php"
    
    payload = {'key': API_KEY, 'short':full_link, "name":link_name}
    requestsa = requests.get(BASE_URL,payload)
    data = requestsa.json()
    
    print('')

    try:
        title = data['url']['title']
        short_link=data['url']['shortLink']
        
        print("Title:", title)
        print("Link:",short_link)
        with open("shorten_link_output.txt", "a") as file:
            file.write("Title: " + title + "\n")
            file.write("Link: " + short_link + "\n\n")
    except:
        status = data["url"]["status"]
        print("Error Status:", status)
        if(status==3):
            print("the preferred link name is already taken")
        elif(status==1):
            print("the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened")
        elif(status==2):
            print("the entered link is not a link")
        elif(status==3):
            print("the preferred link name is already taken")
        elif(status==4):
            print("Invalid API key")
        elif(status==5):
            print("the link has not passed the validation. Includes invalid characters")
        elif(status==6):
            print("The link provided is from a blocked domain")
        elif(status==8):
            print("You have reached your monthly link limit. You can upgrade your subscription plan to add more links.")
            
        


link=input("enter a link: ")
name=input("Give your link a  name: ")



shorten_link(link,name)

    