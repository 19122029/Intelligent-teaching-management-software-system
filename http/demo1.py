import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','Charlie'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco','China']}
df = pd.DataFrame(data)

# 模糊查询包含 "Charlie" 子字符串的行
result = df[df['Name'].str.contains('Charlie', case=False)]

print(type(result))