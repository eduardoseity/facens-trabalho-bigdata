import requests
import json
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import argparse
import utils
import os

main_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')


def __get_best_seller(name:str, id:str, timestamp=None) -> pd.DataFrame:
    headers = {
        'Host': 'www.mercadolivre.com.br',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Alt-Used': 'www.mercadolivre.com.br',
        'Connection': 'keep-alive',
        'Cookie': '_d2id=4647b427-8c4e-4c5c-9e73-ef1658d883a7; c_ui-navigation=6.2.1; _ml_ga=GA1.3.219935527.1690772536; _gac_UA-46090222-1=1.1690772553.CjwKCAjwlJimBhAsEiwA1hrp5vVJ8KekT55BjJmagm0edVwo8QsEsIKHwvlEfYp9x-Lx2JQRznOc1hoCumUQAvD_BwE; _gcl_aw=GCL.1690772553.CjwKCAjwlJimBhAsEiwA1hrp5vVJ8KekT55BjJmagm0edVwo8QsEsIKHwvlEfYp9x-Lx2JQRznOc1hoCumUQAvD_BwE; _gcl_au=1.1.28663430.1690772536; _ga_NDJFKMJ2PD=GS1.1.1691449811.3.1.1691450372.60.0.0; _ga=GA1.1.219935527.1690772536; _pin_unauth=dWlkPU16YzNNV1U0WkRFdE0ySTROeTAwWldNNExUazFNelV0TVRNME1EbGlOek5tWmpoaA; _hjSessionUser_580848=eyJpZCI6IjJkZDBkM2NjLWIwZmQtNWQ0Ni1hZmZhLTFlY2UxNDUwM2FhMiIsImNyZWF0ZWQiOjE2OTA3NzI1MzcxNDEsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.2.1690772537167.1841917425; _tt_enable_cookie=1; _ttp=MCsNb-1Urivn84Dw1ufFnaopgIc; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22NqDsmGgbMpOJaIDaJBhL%22%7D; cto_bundle=B063pV9abHZhRnFnN0F1dFNheUJhR1JPQXVLdFFUVWMyOVM2MiUyQnNrYU9aakduT0EwODdYSU9QY2tMOVVyenhMODU1JTJCTjN6bzBuR2ttVG02NnhURkZLZjVBa1BRJTJGNFpEV3FKZnZZMG9zUVU3MnFBVGd0OW5MSjRqcTJ4d25ibXdYeG9ZSFNoNzV0OUV0ZDN1VDBrTGslMkZFRW9LcTBjalMya3hBWDJtb3Fua1J0enB1dyUzRA; _csrf=iRQSdh0rQ56tSir9WIKudX9m; _ml_ci=219935527.1690772536; _hjSessionUser_720738=eyJpZCI6ImYxYjQwZWU0LTVlZGItNWUyMS1hZTUxLTRmNWE3ZjVjZjIwYyIsImNyZWF0ZWQiOjE2OTEyNzM0MTQ5OTEsImV4aXN0aW5nIjpmYWxzZX0=; _ml_ga_gid=GA1.3.325818735.1691449811; navigation_items=MLB3402637333%7C07082023231931%7CMLB19035706%7CMLB6408981; _uetsid=8f0c6160357711eeabac5d6fa4dd17db; _uetvid=a7e9b5602f4e11ee82136f3671e6eac3; _mldataSessionId=b2467f41-f755-49f3-b439-426c33d22c0c',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }
    timestamp = timestamp if timestamp != None else datetime.now()
    re = requests.get(f'https://www.mercadolivre.com.br/mais-vendidos/{id}', headers=headers)
    trim = re.text.split('window.__PRELOADED_STATE__ =')[1]
    trim = trim.split('},props:{"on":"load","type":"function","preload":false}},{s:function(){')[0]
    json_txt = trim[0:-11]
    json_obj = json.loads(json_txt)
    items = json_obj['initialState']['results'][0]['trends_categories']['recommendations']
    items_dict = {
        'timestamp':[],
        'best_seller_category_name':[],
        'best_seller_category_id':[],
        'id':[],
        'category_id':[],
        'title':[],
        'url':[],
        'price':[],
        'image':[],
        'image2x':[],
        'product_id':[],
        'available_quantity':[],
        'free_shipping':[],
        'installments':[],
        'free_installments':[],
        'discount':[]
    }
    for i in items:
        items_dict['timestamp'].append(timestamp)
        items_dict['best_seller_category_name'].append(name)
        items_dict['best_seller_category_id'].append(id)
        items_dict['id'].append(i['id'])
        items_dict['category_id'].append(i['category_id'])
        items_dict['title'].append(i['title'])
        items_dict['url'].append(i['url'])
        items_dict['price'].append(i['sale_price']['amount'])
        items_dict['image'].append(i['image']['src'])
        items_dict['image2x'].append(i['image']['src2x'])
        
        try:
            items_dict['product_id'].append(i['product_id'])
        except KeyError:
            items_dict['product_id'].append(None)

        items_dict['available_quantity'].append(i['available_quantity'])
        
        try:
            items_dict['free_shipping'].append(i['shipping']['freeShipping'])
        except KeyError:
            items_dict['free_shipping'].append(False)
        
        try:
            installments = str(i['installments']['quantity'])+'x'+i['installments']['fraction']+','
            try:
                installments += i['installments']['cents']
            except KeyError:
                installments += '00'
            items_dict['installments'].append(installments)
            items_dict['free_installments'].append(i['installments']['freeInstallments'])
        except KeyError:
            items_dict['installments'].append(None)
            items_dict['free_installments'].append(None)
        
        try:
            items_dict['discount'].append(i['discount']['text'])
        except KeyError:
            items_dict['discount'].append(None)

    df = pd.DataFrame(items_dict)
    return df

def get_best_sellers():
    print('Iniciando raspagem dos itens mais vendidos...')
    timestamp = datetime.now()
    categories_csv = os.path.join(main_path,'assets/datasets/categories.csv')
    best_sellers_csv = os.path.join(main_path,'assets/datasets/best_sellers.csv')
    try:
        categories_df = pd.read_csv(os.path.join(main_path, categories_csv))
    except:
        raise Exception(f'Erro ao abrir o arquivo {categories_csv}')
    
    df = None
    
    for c in tqdm(categories_df.itertuples()):
        name = c.name
        id = c.id
        if type(df) == type(None):
            df = __get_best_seller(name, id, timestamp)
        else:
            df = pd.concat([df, __get_best_seller(name, id, timestamp)], ignore_index=True)
    
    try:
        best_sellers_df = pd.read_csv(best_sellers_csv)
        pd.concat([best_sellers_df, df]).to_csv(best_sellers_csv, index=False)
    except:
        df.to_csv(best_sellers_csv, index=False)
    
    print('Processo finalizado!')
    print(f'Arquivo {best_sellers_csv} atualizado')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bestsellers', help='Baixar os itens mais vendidos', action="store_true")
    parser.add_argument('--updatecategories', help='Atualizar dataset de categorias a partir do arquivo categories.json', action="store_true")
    args = parser.parse_args()

    if args.bestsellers:
        get_best_sellers()
    elif args.updatecategories:
        utils.load_categories_from_json()