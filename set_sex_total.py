
import json
import random

global data 

with open('dummy_data.json') as f:
    data = json.load(f)
    total_record = ['合計']
    for title_name, d in data.items():
        title_number = len(d['labels'])
        records = d['data']

        for i, r in enumerate(records):
            department_name = r[0]
            counts = r[1:]
            for j, count in enumerate(counts):
                if i == 0:
                    # 0 -> male, 1 -> female, 2 -> total
                    total_record.append([count[0], count[1], count[2]])
                else:
                    total_record[j + 1][0] += count[0]
                    total_record[j + 1][1] += count[1]
                    total_record[j + 1][2] += count[2]
        data[title_name]['data'].append(total_record)
        total_record = total_record[:1]

with open('dummy_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
