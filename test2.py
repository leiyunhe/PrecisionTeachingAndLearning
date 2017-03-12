import requests
url = "https://github.com/leiyunhe/Py103"
r = requests.get(url)
# r.json() 返回所有的 contributors
for person in r.json():
    # person 类型为 dict, keys有 "author", "total", "weeks"
    # "author"的 value 又是一个 dict, "login" 对应的是作者的名字
    print(person["author"]["login"] + ":" + str(person["total"]))