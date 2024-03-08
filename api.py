import requests
from bs4 import BeautifulSoup
import os

hijau_nyala = "\033[1;92m"
reset = "\033[0m"


os.system("clear")
print(f"Dev : {hijau_nyala}FebryEnsz{reset}")
print(" ")
host = input("Masukan Hostname : ")
url = f"https://dev-ical-webstore.pantheonsite.io/sub.php?host={host}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    result = soup.get_text()
    print(result)
    
    save_to_file = input("Simpan Result : (y/n): ")
    if save_to_file.lower() == "y":
        file_name = input("Masukkan nama file: ")
        file_path = f"/sdcard/{file_name}.txt"
        with open(file_path, "w") as file:
            file.write(result)
        print(f"{file_name} telah disimpan di {file_path}")
else:
    print("Api Error Atau Hosting Suspend Thanks")