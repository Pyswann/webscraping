import requests
api = "https://api.ipify.org?format=json"
r = requests.get(api)
if r.status_code == 200:
    ip = r.json()
    data = ip.get("ip")

myip = f"https://ipapi.co/{data}/json/"
# print(myip)
res = requests.get(myip)
if res.status_code == 200:
    my_loc = res.json()
    ip = my_loc.get("ip")
    network = my_loc.get("network")
    city = my_loc.get("city")
    country = my_loc.get("country_name")
    capital = my_loc.get("country_capital")
    post_code = my_loc.get("postal")
    sen = f"Dear sir! We have got the suspect! He is using {network} and currently is in {city}, {country}, and postal code is {post_code}. His ip address is {ip}, and all the ip details are in this link {myip}"
    print(sen)









