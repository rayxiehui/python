#!/usr/bin/env/python
# utf-8
# numpy 练习

import numpy as np

nparr = np.arange(100)  

t = nparr*2
# 平均数
mean = np.mean(nparr)

max = np.max(nparr)
min = np.min(nparr)

# 加权平均数
average = np.average(t,weights=nparr)

sum = np.sum(t)
ptp = np.ptp(t)
