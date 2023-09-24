import pandas as pd
import warnings
warnings.filterwarnings('ignore')
filename=input("输入需要计算的成绩单文件名: ")
df=pd.read_excel(filename,usecols=["学年","学期","课程性质","学分","成绩","绩点"],index_col=False,dtype={"学期":str})
df["date"]=df["学年"] + " " + df["学期"]
optincalc=input("是否计算通识选修课程? (Y/N)")
def calc(dfparam):
    if optincalc=='N' or optincalc=='n':
        for i in range(0,len(dfparam.index)):
            if dfparam["课程性质"][i] == "通识教育选修课程":
                dfparam.drop(labels=i,inplace=True)
        dfparam.reset_index(drop=True,inplace=True)

    t1,t2=0,0
    for i in range(0,len(dfparam.index)):
        t1+=dfparam["学分"][i]*dfparam["成绩"][i]
        t2+=dfparam["学分"][i]*dfparam["绩点"][i]
    avgsco,avggpa=t1/sum(dfparam["学分"]),t2/sum(dfparam["学分"])
    return avgsco,avggpa

sheets=[]
dates=list(set(df["date"]))
dates.sort()
for i in dates:
    df2add=df[df["date"]==i]
    df2add.reset_index(drop=True,inplace=True)
    sheets.append(df2add)

print("\n每学期均分与绩点:")
x=-1
for i in sheets:
    res=calc(i)
    x+=1
    print(dates[x]+": ",end='')
    print("%.2f, %.2f"%(res[0],res[1]))

res=calc(df)
print("总均分和均绩点: "+"%.2f, %.2f"%(res[0],res[1]))