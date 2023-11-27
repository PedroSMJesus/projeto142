from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# URL dos Exoplanetas da NASA
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(URL)

soup = bs4(page.text, 'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')

# Webdriver
#browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
#browser.get(START_URL)

#time.sleep(10)



def scrape():

    for i in range(0,10):
        print(f'Coletando dados da página {i+1} ...' )

        ## ADICIONE O CÓDIGO AQUI ##
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            
            li_tags = ul_tag.find_all("li")
            
            temp_list = []
            
            for index, li_tags in enumerate(li_tags):
                
                if index == 0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0]) 
                    except:
                        temp_list.append("")       

        
# Chamando o método   
scrape()

planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Chame o método
for index, row in planet_df_1.iterrows():

    ## ADICIONE O CÓDIGO AQUI ##
    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])
     # Call scrape_more_data(<hyperlink>)

    print(f"Coleta de dados do hyperlink {index+1} concluída")
# Remova o caractere '\n' dos dados coletados
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## ADICIONE O CÓDIGO AQUI ##
    for el in row:
        el = el.replace("\n", "")
        replaced.append(el)
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

# Converta para CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
