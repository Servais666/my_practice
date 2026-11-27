import re
data = """
[INFO] 192.168.1.10 GET /login 200
[WARN] 192.168.1.11 POST /admin 403
[INFO] 192.168.1.10 GET /index 200
[ERROR] 10.0.0.8 GET /flag 500
[INFO] 192.168.1.12 POST /login 302
BROKEN LINE
[WARN] 192.168.1.11 GET /robots.txt 404
"""

pattern = r"\[(\w+)\]\s+(\d+\.\d+\.\d+\.\d+)\s+[A-Z]+\s+\S+\s+(\d{3})"#\S指的是非空格的任意单位，最后的d{3}是指限制长度为3的数字组合
def analyze(data):
    data=data.splitlines()
    ip={}
    status={}
    specialrequest=[]
    for line in data:
        line=line.strip()
        if not line:
            continue
        result=re.fullmatch(pattern,line)
        if result:#格式正确
            pass
        else:
            print("格式错误"+line)
            continue
        this_ip=result.group(2)
        this_statuscode=result.group(3)
        ip[this_ip]=ip.get(this_ip,0)+1
        status[this_statuscode]=status.get(this_statuscode,0)+1
        if int(this_statuscode)>=400:
            specialrequest.append(line)
    return ip,status,specialrequest

ip_result,status_result,specialrequest_result=analyze(data)
print("ip及其访问次数：")
for ip in ip_result:
    print(ip,ip_result[ip])
print("所有访问类型如下：")
for status in status_result:
    print(status,status_result[status])
print("异常访问记录如下：")
for request in specialrequest_result:
    print(request)


        


            

