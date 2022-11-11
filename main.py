# boxscore scraper

from datetime import datetime
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.acb.com/partido/estadisticas/id/103293?fbclid=IwAR1h_e2jmWXJAURcl5CO8DlisUf_mOu6cJ-CE3YY-Ek0GOKxOLY4pvKS8Ak'

driver = webdriver.Chrome(driver_path)
driver.get(website)

# stats for home team
df_home = pd.DataFrame(columns=['D', 'Nombre', 'Min', 'P', 'T2', 'T2%', 'T3', 'T3%', 'T1', 'T1%', 'REB T',
                            'REB D+O', 'A', 'BR', 'BP', 'C', 'TAP F', 'TAP C', 'TAP M', 'FP F', 'FP C', '+/-', 'V'])

t.sleep(1)
table_home = driver.find_element(by=By.XPATH, value="//section[@class='partido']")
home_team = table_home.find_element(by=By.TAG_NAME, value="h6")
tbody = table_home.find_element(by=By.TAG_NAME, value="tbody")
rows = tbody.find_elements(by=By.TAG_NAME, value="tr")

for row in rows:
    info = row.get_attribute('innerText')
    stats = row.find_elements(by=By.TAG_NAME, value="td")
    data = []
    for stat in stats:
        data.append(stat.get_attribute('innerText'))
    if len(data) == 23:
        df_home.loc[len(df_home)] = data
print(df_home)

# stats for away team
df_away = pd.DataFrame(columns=['D', 'Nombre', 'Min', 'P', 'T2', 'T2%', 'T3', 'T3%', 'T1', 'T1%', 'REB T',
                            'REB D+O', 'A', 'BR', 'BP', 'C', 'TAP F', 'TAP C', 'TAP M', 'FP F', 'FP C', '+/-', 'V'])

t.sleep(1)
table_away = driver.find_element(by=By.XPATH, value="//section[@class='partido visitante']")
away_team = table_away.find_element(by=By.TAG_NAME, value="h6")
tbody_away = table_away.find_element(by=By.TAG_NAME, value="tbody")
rows_away = tbody_away.find_elements(by=By.TAG_NAME, value="tr")

for row in rows_away:
    info = row.get_attribute('innerText')
    stats = row.find_elements(by=By.TAG_NAME, value="td")
    data = []
    for stat in stats:
        data.append(stat.get_attribute('innerText'))
    if len(data) == 23:
        df_away.loc[len(df_away)] = data

print(df_away)

# export data as csv
home_name = home_team.get_attribute('innerText')
away_name = away_team.get_attribute('innerText')
print(home_name, away_name)
df_home.to_csv(home_name+'stats.csv')
df_away.to_csv(away_name+'stats.csv')

driver.close()
