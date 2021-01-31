
# 使用方法：在link.txt里面放入所有link，第一行写js或者css（也就是要套的模板类型），一行一个链接，然后结果在out.txt里面

import os

f = open("./link.txt",'r')
f_out = open('./out.txt','w')
lines = f.readlines()
type = lines[0].replace("\n", "")

if type == "js":
    for line in lines:
        line = line.replace("\n", "")
        if line == "js":
            continue
        template = "<script type='text/javascript' src='"+ line +"'></script>\n"
        f_out.write(template)
        print("Success-Js!")

else:
    if type == "css":
        for line in lines:
            line = line.replace("\n", "")
            if line == "css":
                continue
            template = "<link rel='stylesheet' type='text/css' href='"+ line +"'>\n"
            f_out.write(template)
            print("Success-css! ")

    else:
        f_out.write("fail")
        print("Fail!检查是否在文件第一行输入链接类型？")
f.close()