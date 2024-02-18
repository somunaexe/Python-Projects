import urllib.request as urllib



def check_site_connection(url):
    print("Checking connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Enter the url of the website: ")

check_site_connection(input_url)
