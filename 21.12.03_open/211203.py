import pandas as pd
import numpy as np

data2={"names" : ["kilho","chaeho","hyeonho","gaho","junho"]
      ,"year":["1994","1993","1994","1992","1993"]
      ,"points":[1.5, 1.7, 3.6, 2.4, 2.9]}
df3=pd.DataFrame(data2, columns=["year", "names", "points", "penalty"]
                ,index=["one", "two", "three", "four", "five"])
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
df3['debt']=val
df3['net_points']=df3['points']-df3['penalty']
df3['hight_points']=df3['net_points']>2.0
df3.loc['six',:] = [2013,"mino",4.0,0.1,5,0.8,0,0] #기존의 columns에 해당하는 모든 값을 얺어주어야함