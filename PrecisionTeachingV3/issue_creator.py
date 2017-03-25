#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
def issue_creator():
    url = 'https://github.com/leiyunhe/PrecisionTeachingAndLearning/issues'
    s = requests.session()
    r = s.get(url)
    print(r)
    print(type(r))
    print(r.text)
    result = json.loads(r.text)
    print(result[0])
issue_creator()