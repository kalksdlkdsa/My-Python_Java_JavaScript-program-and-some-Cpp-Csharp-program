path='D:\QLSV.txt'
def save(line):
    try:
        f = open(path, 'a', encoding="utf8")
        f.writelines(line)
        f.writelines("\n")
        f.close()  # Kết thúc hàm save(line)
    except:
        pass
def read():
    sv=[]
    try:
        f = open(path, 'r', encoding="utf8")
        for i in f:
            data = i.strip()
            arr = data.split('-')
            sv.append(arr)
        f.close()
    except:
        pass
    return sv #Kết thúc hàm read()
