import requests

def get_by_pincode(pinCode):
    url = "https://api.postalpincode.in/pincode/"
    response = requests.get(url+pinCode)
    data = response.json()
    display_post_offices(data[0]['PostOffice'])


def get_by_branch(branchName):
    url = "https://api.postalpincode.in/postoffice/"
    response = requests.get(url+branchName)
    data = response.json()
    display_post_offices(data[0]['PostOffice'])


def display_post_offices(PostOffices):
    print("No of Postoffices found : ",len(PostOffices))
    for post in PostOffices:
        print(post)


get_by_pincode("517112")
get_by_branch("New Delhi")