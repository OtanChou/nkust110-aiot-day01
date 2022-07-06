import json
with open("gender_lname.json", "r", encoding="utf-8") as fp:
    jsondata = fp.read()
data = json.loads(jsondata)
data = data["responseData"]
for item in data[:10]:
    print(item["family_name"], item["gender"], item["people_total"])