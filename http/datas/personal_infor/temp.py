import pandas as pd
# 初始创建人员信息文件
file_dir = "datas/personal_infor/personal_infor.csv"
data = {

    '学号':['t111','s111','a111'],
    '密码':['','','']
    ''

}

df = pd.DataFrame(data)
df.to_csv(file_dir,index=False)

