import requests

packages = ["theano", "scikit-learn", "uyyyt"]
for p in packages:
    r = requests.get(f"https://pypi.org/pypi/{p}/json")
    try:
        data = r.json()
    except:
        continue
    urls = data["info"]["project_urls"]
    try:
        doc = urls["Documentation"]
    except:
        doc = None
    if doc != None:
            print(doc)