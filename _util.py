def dic_iqual(dic):
    v = int(dic_values(dic)[0])
    for i in dic:
        if v != dic[i]:
            return False
    return True

def dic_minValue(dic):
    _max = int(dic_values(dic)[0])
    key = int(dic_key(dic)[0])
    for i in dic:
        if dic[i] < _max:
            _max = dic[i]
            key = i
    return [key,_max]

def dic_key(dic):
    return str(dic.keys()).replace("dict_keys","").replace("(","").replace(")","").replace("[","").replace("]","").strip("").split(",")
def dic_values(dic):
    return str(dic.values()).replace("dict_values","").replace("(","").replace(")","").replace("[","").replace("]","").strip("").split(",")