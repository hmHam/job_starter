import json
import random

global data 
with open('dummy_data.json') as f:
    data = json.load(f)
    for title_name, d in data.items():
        title_number = len(d['labels'])
        # データの配列
        records = d['data']
        for r in records:
            for j in range(1, title_number + 1):
                male_number = random.randrange(0, 333)
                female_number = random.randrange(0, 333)
                total = male_number + female_number
                r[j] = [male_number, female_number, total]
            
with open('dummy_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
