from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

cities = ['Carpentiera', 'Summerland', 'Santa-Barbara', 'Montecito', 'Goleta', 'Isla-Vista', 'Cuyama', 'New-Cuyama', 'Casmalia', 
          'Guadalupe', 'Lompoc', 'Los-Alamos', 'Los-Olivos', 'Santa-Maria', 'Orcutt', 'Santa-Ynez', 'Ballard', 'Solvang']
driver = webdriver.Chrome()
common_names_list = []
species_names_list = []
all_names = []

for city in cities:
    urls = [f'https://calscape.org/loc-34.3989,-119.5185%20({city})/cat-All-Plants/ord-popular?srchcr=sc642e0babcdbd9', 
            f'https://calscape.org/loc-34.4133,-119.861%20({city})/cat-All-Plants/ord-popular/page-2/np-0?srchcr=sc642e0da4adc4b']

    # Scrapes common and scientific names from 93106 page
    for url in urls:

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

    plant_urls_base = f'https://calscape.org/loc-34.4133,-119.861%20({city})/Quercus-agrifolia-(Coast-Live-Oak)'
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
        url = f'https://calscape.org/loc-34.4136,-119.8497%20({city})/{plant_url[index]}?srchcr=sc63f5693746598'
        driver.get(url)
        plant_info = []

        info = driver.find_elements(By.CLASS_NAME, "info")

        if len(info) < 7:
            continue
        else:
            for i in range(0, 8):
                plant_info.append(info[i].text)

        all_plant_info.append(plant_info)



    # adds all info and names to a dataframe

    df = pd.DataFrame(all_plant_info)

    df.insert(0, "Plant Name", all_names)

    df.to_csv(f'plantinfo{city}.csv', index=False, encoding='utf-8')

