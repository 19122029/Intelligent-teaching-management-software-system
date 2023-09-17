import pandas as pd
import copy
# 创建一个示例 DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
df1 = copy.deepcopy(df)
# 创建一个切片，选择要修改的行和列
# 在这个示例中，我们将修改第一行的 'A' 列的值为 99
row_index = 0  # 行索引
column_name = 'A'  # 列名
new_value = 99  # 新的值

# 使用 .loc 方法来修改原始 DataFrame 中的数据
df1.iloc[row_index].loc[column_name] = new_value

# 打印修改后的 DataFrame
print(df)
print(df1)
