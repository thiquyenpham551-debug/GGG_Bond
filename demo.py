import pandas as pd
from datetime import datetime

def calculate_age_from_id(id_number):

    if len(id_number) == 18:
        birth_year = int(id_number[6:10])  # 提取出生年份 [[6]]
        current_year = datetime.now().year  # 获取当前年份 [[6]]
        age = current_year - birth_year
        return age
    else:
        # 如果身份证号不是18位，返回None或进行其他错误处理
        return None  # 或者 raise ValueError("身份证号长度不正确")

# 读取输入的Excel文件
# 请将 'input.xlsx' 替换为你的输入文件名
input_file = '模拟身份证数据.xlsx'
df = pd.read_excel(input_file, dtype={"身份证号": str})


# 假设列名为 '姓名' 和 '身份证号'，如果不是，请修改下面的列名
name_column = '姓名'
id_column = '身份证号'

# 计算年龄并创建新列
df['年龄'] = df[id_column].apply(calculate_age_from_id)  # 应用函数计算年龄 [[1]]

# 选择需要输出的列：姓名、身份证号、年龄
output_df = df[[name_column, id_column, '年龄']]

# 将结果写入新的Excel文件
# 请将 'output.xlsx' 替换为你想要的输出文件名
output_file = 'output.xlsx'
output_df.to_excel(output_file, index=False)  # 使用pandas写入Excel [[1]]

print(f"处理完成，结果已保存到 {output_file}")