from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


url = 'https://calscape.org/loc-34.4136,-119.8497%20(93106)/cat-All-Plants/ord-popular?srchcr=sc63f5693746598'
driver = webdriver.Chrome()
common_names_list = []
species_names_list = []
all_names = []

# Scrapes common and scientific names from 93106 page

driver.get(url)

common_names = driver.find_elements(By.CLASS_NAME, "common_name")
for name in common_names:
    if len(name.text) != 0:
        common_names_list.append(name.text)
    
species_names = driver.find_elements(By.CLASS_NAME, "species")
for name in species_names:
    if len(name.text) != 0:
        species_names_list.append(name.text)
    
for index in range(0, len(common_names_list)):
    all_names.append(f"{common_names_list[index]} ({species_names_list[index]})")

# scrapes other info from each plant (goes to seperate plant url)
'Marah-fabacea-(Wild-Cucumber)'
plant_urls_base = 'https://calscape.org/loc-34.4136,-119.8497%20(93106)/Marah-fabacea-(Wild-Cucumber)?srchcr=sc63f5693746598'
common_name_url = []
species_url = []
plant_url = []
all_plant_info = []

for name in common_names_list:
    new_name = str(name).replace(" ", "-")
    common_name_url.append(new_name)

for name in species_names_list:
    new_species = str(name).replace(" ", "-")
    species_url.append(new_species)

for index in range(0, len(common_names_list)):
    plant_url.append(f"{species_url[index]}-({common_name_url[index]})")

for index in range(0, len(plant_url)):
    url = f'https://calscape.org/loc-34.4136,-119.8497%20(93106)/{plant_url[index]}?srchcr=sc63f5693746598'
    driver.get(url)
    plant_info = []

    info = driver.find_elements(By.CLASS_NAME, "info")

    for item in info:
        plant_info.append(item.text)

    all_plant_info.append(plant_info)



# adds all info and names to a dataframe

df = pd.DataFrame(all_plant_info)
df.insert(0, "Plant Name", all_names)

df.to_csv('plantinfo.csv', index=False, encoding='utf-8')

