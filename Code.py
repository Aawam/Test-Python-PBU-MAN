from bs4 import BeautifulSoup
import requests
import pandas as pd

#
html = requests.get("https://pbu.mayoga.sch.id/data-pendaftar-pbu-2024/")
soup = BeautifulSoup(html.text, "html.parser")
#
table = soup.find_all("th")
header = [title.text.strip() for title in table]
df = pd.DataFrame(columns=header)

#
max_student = soup.find_all("tr")[-1].find_all("td")[0].text
# When do iteration use this formula
# while i <= max_student: Loop \ i++

table = soup.find("tbody")
datas = table.find_all("tr")
output = []
for i in datas:
    i = [x.text for x in i.find_all("td")]
    i: BeautifulSoup = i

    result = {
        "ID": i[0],
        "Reg_Code": i[1],
        "Name": i[2],
        "Date": i[3],
        "isBoarded": True if i[4] == "YA" else False,
        "Verif": True if i[5] == "LOLOS" else False,
        "Interview_Date": i[6],
    }
    output.append(result)

for i in output:
    print(i)

df = pd.DataFrame(data=output)
df.to_csv("output.csv", index=False)
# length = len(df)
# df.loc[length] = result


# Student_data = [data.text.strip() for data in cek]

"""
for raw in num:
    raw_data = raw.find('td')
    Regis_num = raw.find('td', class_='expand column-kode-pendaftaran sorting_1').text
    data1 = [data.text.strip() for data in raw_data][0:6]

    print(raw_data)
    """
