import json

if __name__ == '__main__':
    with open('classdata.json','r', encoding='utf8') as file:
        dic = file.read()
    dic = json.loads(dic)
    print(dic['classes']['54846'])