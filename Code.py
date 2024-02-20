from bs4 import BeautifulSoup
import requests
import pandas as pd
#
html = requests.get('https://pbu.mayoga.sch.id/data-pendaftar-pbu-2024/')
soup = BeautifulSoup(html.text, 'html.parser')
#
table = soup.find_all('th')
header = [title.text.strip() for title in table]
df = pd.DataFrame(columns = header)

#
max_student = soup.find_all('tr')[-1].find_all('td')[0].text
#When do iteration use this formula
#while i <= max_student: Loop \ i++

num = soup.find('tbody')
raw = num.find_all('tr')

for raw_data in raw: 
    cek = raw_data.find('td')
    
    for data in cek:
        data1 = data.find(class_='numdata integer column-no sorting_1').text()
        print(data1)
    
    """
    result = {
        "No": Student_data[0],
        "ID": Student_data[1],
        "Nama": Student_data[2],
        "Date": Student_data[3],
        "Choose to Boarding": Student_data[4],
        "Verif Result": Student_data[5],
        "Test Date": Student_data[6]
    }
    """

#length = len(df)
#df.loc[length] = result


#Student_data = [data.text.strip() for data in cek]

"""
for raw in num:
    raw_data = raw.find('td')
    Regis_num = raw.find('td', class_='expand column-kode-pendaftaran sorting_1').text
    data1 = [data.text.strip() for data in raw_data][0:6]

    print(raw_data)
    """