from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL da NASA Exoplanet
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/zodte/Byjus/aula141/msedgedriver.exe")
browser.get(URL)

time.sleep(10)

planets_data = []

# Defina o método de coleta de dados dos exoplanetas
def scrape():

    for i in range(0,10):
        print(f'Coletando dados da página {i+1} ...' )

        ## ADICIONE O CÓDIGO AQUI ##
        soup = BeautifulSoup(browser.page_source, "html.passer")
        
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
            
            planets_data.append(temp_list)
            print(planets_data[1])
    
    browser.find_element(by = By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        
# Chamando o método   
scrape()

# Defina o cabeçalho
headers = []

# Defina o dataframe do pandas   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Converta para CSV
planet_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
    


