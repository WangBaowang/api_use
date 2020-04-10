# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/10 16:41
# 文件名称: bar_descriptions.py
# 开发工具: PyCharm

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value':16101, 'label': 'Description of httpie'},
    {'value':15262, 'label': 'Description of django'},
    {'value':14501, 'label': 'Description of flask'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')