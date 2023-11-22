import json

def mean_age(json_string):
    my_json = json.loads(json_string)
    sum = 0
    k = 0
    for i in range(len(my_json)):
        for key, value in my_json[i].items():
            if key == "age":
                k += 1
                sum += value
    mage = sum / k
    return json.dumps({"mean_age": mage})