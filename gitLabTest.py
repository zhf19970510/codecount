# encoding: utf-8
import gitlab

url = "https://git.jczh56.com"
private_token = "65cx2shbYxsJgWpQcpCN"
# 登录
gl = gitlab.Gitlab(url, private_token)
gl.auth()
# 获取所有的project
projects = gl.projects.list(all=True)
print(projects)
# 获取所有project的name,id
for p in gl.projects.list(all=True, as_list=False):
    print(p.name, p.id)
