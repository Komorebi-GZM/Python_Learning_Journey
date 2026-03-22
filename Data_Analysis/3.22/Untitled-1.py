#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NumPy和Pandas基础测试
用于回顾和测试NumPy与Pandas的基本知识点
"""

import numpy as np
import pandas as pd

# =======================================
# NumPy 测试部分
# =======================================
print("=== NumPy 测试 ===")

# 1. 创建数组
print("\n1. 创建数组:")
# 从列表创建
arr1 = np.array([1, 2, 3, 4, 5])
print(f"从列表创建: {arr1}")

# 创建全0数组
zeros_arr = np.zeros((2, 3))
print(f"全0数组:\n{zeros_arr}")

# 创建等差数列
range_arr = np.arange(0, 10, 2)
print(f"等差数列: {range_arr}")

# 2. 数组属性
print("\n2. 数组属性:")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"形状: {arr2.shape}")
print(f"维度: {arr2.ndim}")
print(f"数据类型: {arr2.dtype}")

# 3. 数组运算
print("\n3. 数组运算:")
arr3 = np.array([1, 2, 3])
print(f"原数组: {arr3}")
print(f"数组 + 2: {arr3 + 2}")
print(f"数组 * 2: {arr3 * 2}")
print(f"数组 ** 2: {arr3 ** 2}")

# 4. 索引和切片
print("\n4. 索引和切片:")
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"原数组:\n{arr4}")
print(f"索引 arr4[1, 2]: {arr4[1, 2]}")
print(f"切片 arr4[:2, 1:]:\n{arr4[:2, 1:]}")

# 5. 布尔索引
print("\n5. 布尔索引:")
arr5 = np.random.randn(5, 3)
print(f"原数组:\n{arr5}")
print(f"大于0的元素:\n{arr5[arr5 > 0]}")

# 6. 统计函数
print("\n6. 统计函数:")
arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"原数组:\n{arr6}")
print(f"均值: {arr6.mean()}")
print(f"每行均值: {arr6.mean(axis=1)}")
print(f"每列求和: {arr6.sum(axis=0)}")
print(f"最大值: {arr6.max()}")
print(f"最小值: {arr6.min()}")

# 7. 数组转置
print("\n7. 数组转置:")
arr7 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"原数组:\n{arr7}")
print(f"转置后:\n{arr7.T}")

# =======================================
# Pandas 测试部分
# =======================================
print("\n=== Pandas 测试 ===")

# 1. 创建Series
print("\n1. 创建Series:")
# 从列表创建
s1 = pd.Series([1, 2, 3, 4, 5])
print(f"从列表创建:\n{s1}")

# 带索引的Series
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(f"带索引的Series:\n{s2}")

# 2. Series操作
print("\n2. Series操作:")
print(f"索引访问 s2['c']: {s2['c']}")
print(f"布尔过滤 s2[s2 > 2]:\n{s2[s2 > 2]}")
print(f"Series + 2:\n{s2 + 2}")

# 3. 创建DataFrame
print("\n3. 创建DataFrame:")
# 从字典创建
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'score': [85, 90, 88, 92]
}
df1 = pd.DataFrame(data)
print(f"从字典创建:\n{df1}")

# 4. DataFrame操作
print("\n4. DataFrame操作:")
print(f"查看前2行:\n{df1.head(2)}")
print(f"查看列名: {df1.columns}")
print(f"查看age列:\n{df1['age']}")
print(f"查看行索引为1的行:\n{df1.loc[1]}")

# 5. DataFrame过滤
print("\n5. DataFrame过滤:")
print(f"年龄大于30的行:\n{df1[df1['age'] > 30]}")
print(f"分数大于88的行:\n{df1[df1['score'] > 88]}")

# 6. DataFrame统计
print("\n6. DataFrame统计:")
print(f"各列均值:\n{df1.mean()}")
print(f"各列最大值:\n{df1.max()}")
print(f"数据描述:\n{df1.describe()}")

# 7. DataFrame修改
print("\n7. DataFrame修改:")
# 添加新列
df1['grade'] = ['A', 'A+', 'A', 'A+']
print(f"添加grade列后:\n{df1}")

# 修改值
df1.loc[0, 'score'] = 87
print(f"修改score后:\n{df1}")

print("\n=== 测试完成 ===")
print("回顾了NumPy和Pandas的基本操作")
