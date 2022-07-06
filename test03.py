with open("data.csv", "r", encoding="UTF-8") as fp:
    data = fp.readlines()

for line in data[1:]:  #for迴圈將資料分段 #[1:]省略無用的第一行
    name, h, w = line.split(",")  #將資料拆開
    h = int(h)
    w = int(w.strip())  #.strip()將後面的換行符號\n去除
    bmi = round(w / ((h/100)**2), 2)  #round(x,2)即四捨五入，取到小數點後第二位
    print("{}的身高是{}公分，體重是{}公斤，BMI是{}".format(name, h, w, bmi))