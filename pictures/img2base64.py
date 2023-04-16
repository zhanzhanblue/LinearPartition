import base64
f=open('0.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
with open('out.txt', 'w') as f:
    f.write('data:image/png;base64,' + str(ls_f)[2:-1])