# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/7 14:05
# 文件名称: python_repos.py
# 开发工具: PyCharm

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:java&sort=star'
r = requests.get(url)
print("Status code:", r.status_code)    # 状态码200表示请求成功

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# # 处理结果
# print(response_dict.keys())

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))

# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# # print("\nKeys:", len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# #     print(key)
#
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])    # 创建时间
# print('Updated:', repo_dict['updated_at'])    # 最后一次更新时间
# print('Description:', repo_dict['description'])

# print("\nSelected information about each repository:")
# # for repo_dict in repo_dicts:
# #     print('\nName:', repo_dict['name'])
# #     print('Owner:', repo_dict['owner']['login'])
# #     print('Stars:', repo_dict['stargazers_count'])
# #     print('Repository:', repo_dict['html_url'])
# #     print('Description:', repo_dict['description'])

# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

print("Number of time:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    if repo_dict['description']:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': 'None',
            'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend =False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15    # 将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.show_y_guides = False    # 以隐藏图表中的水平线
my_config.width = 1000    # 自定义宽度，让图表更充分地利用浏览器中的可用空间。

chart = pygal.Bar(my_config, style=my_style)    # 隐藏了图例:show_legend=False
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

# chart.add("", stars)
chart.add("lalalalalaalalal", plot_dicts)
chart.render_to_file("python_repos_java.svg")