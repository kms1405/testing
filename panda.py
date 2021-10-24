import csv

j= open("/home/meenakshisundaram/Downloads/allurls.csv")

s=j.read().split(" ")

for i in s:
    if "/" in i:
        print(i)