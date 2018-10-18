#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for rank in points:
    sum+=points[rank]
print(int(sum))

