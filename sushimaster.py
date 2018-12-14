import urllib.request
import requests

urls = ['https://sushi-master.ru/kaliningrad/menu/nabory/',
        'https://sushi-master.ru/kaliningrad/menu/aktsiya/',
        'https://sushi-master.ru/kaliningrad/menu/goryachie_blyuda/',
        'https://sushi-master.ru/kaliningrad/menu/salaty/',
        'https://sushi-master.ru/kaliningrad/menu/sup/',
        'https://sushi-master.ru/kaliningrad/menu/gotovye-voki/']

main_element_str = 'class="item-long item__el item__el-get  buySushi"'
name_class = '<span class="item__name">'
price_class = '<div class="item-long__cost">'


def parse_from_index(string, index):
    char = string[index]
    result = ''
    while char != '<':
        result += char
        index+=1
        char = string[index]

    return result

f = open('output.txt', 'w+')
for url in urls:

    r = requests.get(url)
    string = r.text

    res = 1
    last_name_ind = 0
    last_price_ind = 0
    names = []
    prices = []
    while res > 0:
        res = 1
        names.append(parse_from_index(string, string.find(name_class, last_name_ind) + len(name_class)))
        prices.append(parse_from_index(string, string.find(price_class, last_price_ind) + len(price_class)))
        try:
            last_name_ind = string.index(name_class, last_name_ind) + 2
            last_price_ind = string.index(price_class, last_price_ind) + 2
        except ValueError:
            print("End of page!")
            res = 0
            del names[len(names)-1]
            del prices[len(prices) - 1]

    for i in range(len(names)):
        f.write(names[i] + ';' + prices[i]) + f.write('\n')

f.close()
