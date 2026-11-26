import re
import subprocess

tools = [
    "python3",
    "sqlmap",
    "gopherus",
    "nmap",
    "tool_not_exist"
]

class toolresult:
    def __init__(self,name,version,status,wronginfo):
        self.name=name
        self.version=version
        self.status=status
        self.wronginfo=wronginfo
    def __str__(self):
        return f"工具：{self.name} 版本：{self.version} 状态：{self.status} 错误信息：{self.wronginfo}"

for tool in tools:
    try:
        result=subprocess.run(
            [tool,"--version"],
            capture_output=True,
            text=True
            )
        output=result.stdout.strip() or result.stderr.strip()
        if result.returncode==0:#正常
            status="正常"
            version=re.findall(r"\d+.*\d+",output)[0]
            wronginfo=""
        else:
            status="异常"
            version="未知"
            wronginfo=output
    except FileNotFoundError:
        status="执行失败"
        version="未知"
        wronginfo="找不到该文件"
    except PermissionError:
        status="执行失败"
        version="未知"
        wronginfo="权限不足"

    it=toolresult(tool,version,status,wronginfo)


    print("#######################")
    print(it.name,it.status,it.version,it.wronginfo)



        
