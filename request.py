import requests
import json
from bs4 import BeautifulSoup
cookies = {
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1619575001259%2Cregion:%27VN%27}',
    '_ga': 'GA1.3.1721776623.1619575033',
    '_gid': 'GA1.3.1280940627.1619963592',
    'XSRF-TOKEN': 'eyJpdiI6Iktkc0dGdEExcTBoVUd0c3FKcVRncWc9PSIsInZhbHVlIjoiaFc2XC9PdldjckhrXC9TbmFMdGN1MlRTcnBYV2JWU1RVbUNqUTFyQUthZzU5eUYyREV6WVloZGk0T2U5dU1yQ2VTIiwibWFjIjoiYmI4MmE0M2JlNWFhMmZjZWRlNjQ3OWI0YTY1MDZlMDFiMzVmMDBkYjViNTEyYzhlMjU0MzlmMWE0ZDU4ZWM1YSJ9',
    'exploit_database_session': 'eyJpdiI6Ilo0dzhvSzhxTlpXYk9tRis3TWV1aWc9PSIsInZhbHVlIjoiaDNsSzNqNU5PWHJqMVZIUE5YTU9GV2hJWnZiVHNUejlTSnlLOFRicUc5R283ekd6XC9XMnRPZkU1XC9uTnA1RWExIiwibWFjIjoiMTI5MzFhZDVjNjMyYTBjNmNiNzgxMTI4MjAzMzIyNzJjN2I0OTc0Y2ZmNzZlNmQ1MGIzZDVlYmFhYThjNzc0YSJ9',
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


counter = 2
while counter <= 2933:
    page_number = 1
    EXP_DATA = {}
    EXP_DATA[page_number] = {}
    response = requests.get(f'https://www.exploit-db.com/?draw={counter}&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1620118525455', headers=headers, cookies=cookies)

    for exp_counter in range(14):
        
        
        exp_id = response.json()['data'][exp_counter]['id']
        # print(response.text)

        cookies = {
            'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1619575001259%2Cregion:%27VN%27}',
            '_ga': 'GA1.3.1721776623.1619575033',
            '_gid': 'GA1.3.1280940627.1619963592',
            'XSRF-TOKEN': 'eyJpdiI6ImpESUdtSFhYWlprXC96XC9FdW1STGlaUT09IiwidmFsdWUiOiJDS01DRWxVZmg1QlladEdlZ1BtQnQxSTVuSSttQkRDUUNKcVVKVWdVZlhVdUVtUXVzMTFGMys5a25Bb2lyOTdrIiwibWFjIjoiM2JkZmNiNzc2YmU0ZTcyMTIzOGEyNjg2YmFkZmRlOTBlMzYwY2Y5MTM2OTdiNzIzZDJhMjZlYTk0NmRhODFlZCJ9',
            'exploit_database_session': 'eyJpdiI6InlVWkxsTFRjZUE4QkZvM3E4V0ZPUEE9PSIsInZhbHVlIjoiQ0ROcmtyeUlLNmdzbFB5ZHd2c0ZZNkxhUEt5XC9BejRhVFVSQlwvbk5lU2tPMVBRMXJJbEViZUIzOG4zWEdsWjY5IiwibWFjIjoiZjBkMzFjMTU3MDRiNzZhOGEwMDJiY2Q0MGYxNjYyODljMWI1YTZiZmQ1ZTU3NWFiOGI5MjM4YTU4NGJlZTQ3YSJ9',
        }

        headers = {
            'authority': 'www.exploit-db.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.exploit-db.com/',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        }

        exploit_r = requests.get(f'https://www.exploit-db.com/exploits/{exp_id}', headers=headers, cookies=cookies).text

        soup = BeautifulSoup(exploit_r, 'lxml')

        exp_list = []
        title = soup.find(class_="card-title text-secondary text-center").text.split('-')
        for i in title: 
            exp_list.append(i)
        list_l = soup.find_all(class_="stats-title")
        for stats in list_l: 
            
            stats_text = stats.text
        
            exp_list.append(stats_text)

        data = 'data'
        detail = 'detail'

        if exp_id not in EXP_DATA[page_number]: 
            EXP_DATA[page_number][exp_id]  = {data: exp_list, detail : soup.find('pre').text}
    page_number += 1 
    counter += 1 
    



