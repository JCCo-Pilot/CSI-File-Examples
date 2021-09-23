import json
some_var = {
    "a key":"a value",
    "nested":{
        "another key":"another value",
        "something else":"some value"
    }, "array":[6,2,5,6]
}
print(json.dumps(some_var))#converts value of somevar to string
st = json.dumps(some_var)
p = json.loads(st)
print(json.loads(st))
print(p['nested']['another key'])
print(p['array'][3])
json_file = json.load(open('data.json','r',encoding = "utf-8"))

