import http.client

conn = http.client.HTTPSConnection("instagramdimashirokovv1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com",
    'x-rapidapi-key': "c0521f0f3dmsh8993f042a8099ffp10d5cdjsn4c4323e33c3f"
    }

conn.request("GET", "/tag/virtualstarsgymnastics/optional", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))