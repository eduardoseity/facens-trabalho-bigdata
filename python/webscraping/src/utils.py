import json
import pandas as pd
import os

main_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

def load_categories_from_json() -> None:
    file = os.path.join(main_path,'assets/json/categories.json')
    with open(file, 'r') as f:
        json_string = f.read()
    json_obj = json.loads(json_string)

    items_list = []
    df = pd.DataFrame({'name':[], 'id':[]})

    def dict_iter(value):
        for k, v in value.items():
            if type(v) == list:
                list_iter(v)
            elif type(v) == dict:
                dict_iter(v)
            else:
                items_list.append(k+';'+v)

    def list_iter(value):
        for v in value:
            if type(v) == dict:
                dict_iter(v)
            elif type(v) == list:
                list_iter(v)
            else:
                print(v)

    for k, v in json_obj.items():
        if type(v) == list:
            list_iter(v)
        elif type(v) == dict:
            dict_iter(v)
        else:
            items_list.append(k+';'+v)

    for i in range(len(items_list)-1):
        current_item = items_list[i].split(';')
        next_item = items_list[i+1].split(';')
        if len(current_item) < 2 or len(next_item) < 2:
            continue
        else:
            if current_item[0] == 'id' and next_item[0] == 'name':
                current_df = pd.DataFrame({'name':[next_item[1]], 'id':[current_item[1]]})
                df = pd.concat([df, current_df])
    
    df.to_csv(os.path.join(main_path,'assets/datasets/categories.csv'), index=False)

if __name__ == '__main__':
    pass