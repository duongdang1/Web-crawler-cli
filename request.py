import requests
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable, ALL
import click
from json.decoder import JSONDecodeError


cookies = {
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1619575001259%2Cregion:%27VN%27}',
    '_ga': 'GA1.3.1721776623.1619575033',
    '_gid': 'GA1.3.1280940627.1619963592',
    'XSRF-TOKEN': 'eyJpdiI6IjFGVzJaZ1wvTWdkb0FRSTlxdTgyNkJnPT0iLCJ2YWx1ZSI6IjdMeTN4MEo5azE4QnJUbGp4MmIrNnd4SkxcLzJIQWwrd25WMnV2SFFCR0FQdHFoM3YzUHIyMDkzZGw1anVuNWpBIiwibWFjIjoiOTJkZDRjNGNhMWFlNGM0Njk3MzY2M2VjYmJjMTU5MTljNjQ0Yjg4MGNhMWU4YTVkZmZkOGNmOGNiNTRmMzUwOSJ9',
    'exploit_database_session': 'eyJpdiI6InZvY2FidUpjTllLZXBudVF3MkNDdUE9PSIsInZhbHVlIjoiY2VFRzJwTTltbmRFejYzMEVnQ2NOM2Ztb1prSmdGaFRKZUNZVXlZZjRSOFwvR0djMjNTSGM1UjhhSlVOczZmV1IiLCJtYWMiOiJjNmFmMDY5ODlkZjA1ZjhlNjIxNTYyNTE3ZmJlNTRiNzcyYjU1ODI2NDk4ODk5OGYyYTA0MmJmZDE0YjRjOGNiIn0%3D',
    '_gat': '1',
}

headers = {
    'authority': 'www.exploit-db.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.exploit-db.com/',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
}


start = 0
limit = 15
page_number = 1
EXP_DATA = {}
EBD_ID_list = []
while start <= 30:
    EXP_DATA[page_number] = {}
    url = f'https://www.exploit-db.com/?draw=3&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start={start}&length={limit}&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1620284336350'
    response = requests.get(url, headers=headers, cookies=cookies)

    
    for exp_counter in range(15):
        
        
        exp_id = response.json()['data'][exp_counter]['id']
        EBD_ID_list.append(exp_id)
        
        exploit_r = requests.get(f'https://www.exploit-db.com/exploits/{exp_id}', headers=headers, cookies=cookies).text

        soup = BeautifulSoup(exploit_r, 'lxml')

        exp_list = []
        #      0   |   1  | 2 |  3   | 4  |   5    | 6  |
        #title|vuln|ebd_id|cve|author|type|platform|data|
        title = soup.find(class_="card-title text-secondary text-center").text
        
        exp_list.append(title)
        list_l = soup.find_all(class_="stats-title")
        for stats in list_l: 
            
            stats_text = stats.text
        
            exp_list.append(stats_text)

        data = 'data'
        detail = 'detail'

        
        EXP_DATA[page_number][exp_id]  = {data: exp_list, detail : soup.find('pre').text}
        
    # print(f"done with page {page_number}")
    
            
    page_number += 1 
    start += 15




# print(EXP_DATA[1]['49840']['data'][4])
# first_row = EXP_DATA[1]['49840']['data']

page_dict = {}
start = 0 
limit = 15
for i in range(len(EXP_DATA)):
    page_dict[i+1] = {}
    x = PrettyTable()
    x.field_names = ["EBD_ID", "Product", "Vuln", "CVE", "Platform"]
    x._max_width = {"EBD_ID" : 10, "Product" : 45, "Vuln": 45, "CVE": 10, "Platform": 20}
    x.hrules=ALL
    # x.add_row([first_row[1].strip(), first_row[0].strip(), first_row[0].strip(), first_row[2].strip(), first_row[5].strip()])
    page = EXP_DATA[i+1]
    
    for j in range(start, limit):

        x.add_row([EBD_ID_list[j].strip(), page[EBD_ID_list[j]]['data'][0].strip(), page[EBD_ID_list[j]]['data'][0].strip(), page[EBD_ID_list[j]]['data'][2].strip(), page[EBD_ID_list[j]]['data'][5].strip()])
    page_dict[i+1] = x
    start += 15
    limit += 15

# print(page_dict[1])

# print('----------------------------------------------------------------------------')
# print('----------------------------------------------------------------------------')
# print('----------------------------------------------------------------- this is page 2 -----------------------------------------------------')


# print(page_dict[2])

# print('----------------------------------------------------------------------------')
# print('----------------------------------------------------------------------------')
# print('----------------------------------------------------------------- this is page 3 -----------------------------------------------------')

# print(page_dict[3])
@click.group()
@click.version_option(version='0.01', prog_name='request')
def main():
    """simple exploit-db crawler
    welcome to exploit-db CLI interface
    WELCOME PAGE
    Recently visited page:
    Recently visited ID:"""
    # with open('db.txt', 'r') as readfile: 
    #     data = json.load(readfile)
    # # page_num = 1
    # if data is None: 
    #     click.echo('nothing yet')
    # else: 
    #     click.echo(f'recently visited page:{data["page"]}')
    #     click.echo(f'\n recently visited page:{data["exp_id"]}')
    

@main.command()

@click.option('--page_num', '-fn', prompt=True)
# @click.option('--favorite', '-fn', prompt=True)
# @click.option('--help', '-fn', prompt=True)



def get_page(page_num):
    page = int(page_num)
    print(page_dict[page])


@main.command()
@click.option('--page', '-pg', prompt= True)
@click.option('--exploit_id', '-    ', prompt=True)

def get_exp(page, exploit_id):
    page_num = int(page)
    exp_id = str(exploit_id)
    print(EXP_DATA[page_num][exp_id]['detail'])
    


    with open('db.txt', 'r') as infile, open('db.txt', 'w') as outfile:
        
        old_data = json.load(infile)
        if old_data is None:
            
            save_data = {
                'page':[page_num],
                'exp_id':[exp_id]
            }
            
        
            json_object = json.dumps(save_data)
            outfile.write(json_object)

            

                
        else: 
            print(len(old_data['page']))
            if len(old_data['page']) < 3:
                old_data['page'].append(page_num)
                
                outfile.write(old_data)
            

            else:
                old_data['page'].remove(data['page'][0])
                old_data['page'].append(page_num)
                outfile.write(old_data)
            
    
    
    

    infile.close()
    outfile.close()

if __name__ == "__main__": 

    print('just a moment . . .   ')
    main()