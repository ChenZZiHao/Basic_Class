import xlwings as xw


def pre_data():
    path = "D:/emm.txt"
    f = open(path, 'r')
    out_list = []
    for i in f:
        f1 = i.strip().split('"')
        inside_list = []
        for j in f1:
            if j != '' and j != ',':
                k = j.split(',')
                if len(k) > 1:
                    for l in k:
                        if l != '':
                            inside_list.append(l)
                else:
                    inside_list.append(j.strip(','))
        out_list.append(inside_list)
    f.close()
    return out_list

def wx_insert(path, data):
    """
    按行增删excel，默认sheet表1
    param:
        path:文件路径
        data:要写入的数据
    """
    app = xw.App(visible=False)
    wb = app.books.open(path)
    sht = wb.sheets[0]
    try:
        for i in range(1, len(data) + 1):
            sht.range(f'A{i}').value = data[i-1]
    except:
        print("寄了")
    wb.save()
    wb.app.quit()

if __name__ == '__main__':
    # print(pre_data())
    wx_insert("D:/emm.xlsx", pre_data())