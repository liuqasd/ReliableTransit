import pandas as pd
import plotly.graph_objects as go

# import plotly.express as px
# import plotly.offline as py


cd_metro = pd.read_excel(r"D:\SRTP\网站和代码\房价汇总带经纬度.xls")
# print(type(cd_metro))
token = 'pk.eyJ1IjoiZm94eGpqIiwiYSI6ImNraDJ1OXNhbzBhYzEydXA2Ymt6N2R0NHAifQ.VkK9tHG3fwSnVr2k2Zxleg'

order_route = cd_metro['线路']
print(order_route)
len_route = cd_metro['无约.2']
# len_route = cd_metro['有约.2']

# 获取最大值最小值
max_route = max(len_route)
print("max_route = ", max_route)
min_route = min(len_route)
print("min_route = ", min_route)
# print(len_route)

zipped_lines = list(set(zip(order_route, len_route)))  # 使用set去重得到线路条数
# print(zipped_lines)
# print(type(zipped_lines))


lines = cd_metro['线路'].unique()
# print(lines)

colors = ['rgb(0,0,255)',  # 1蓝
          'rgb(30,131,235)',  # 2
          'rgb(0,200,255)',  # 3
          'rgb(135,245,255)',  # 4
          'rgb(0,255,255)',  # 5青
          'rgb(71,210,205)',  # 6
          'rgb(144,231,145)',  # 7
          'rgb(50,208,60)',  # 8
          'rgb(0,128,0)',  # 9绿
          'rgb(139,249,0)',  # 10
          'rgb(140,228,46)',  # 11
          'rgb(155,255,24)',  # 12
          'rgb(255,255,0)',  # 13黄
          'rgb(250,128,0)',  # 14
          'rgb(248,143,0)',  # 15
          'rgb(242,78,0)',  # 16
          'rgb(255,0,0)',  # 17红
          ]
# step = int((max_route-min_route)/len(colors)) + 1  # 无约29+1=30
step = int(max_route / len(colors)) + 1  # 无约31+1=32
print("区间大小 = ", step)
colorindex = []
for zipped_line in zipped_lines:
    # index = int((zipped_line[1] - min_route)/step)
    index = int(zipped_line[1] / step)
    colorindex.append(index)

for i, val in enumerate(zipped_lines):
    zipped_lines[i] = (val[0], val[1], colorindex[i])
print(zipped_lines)


fig = go.Figure([go.Scattermapbox(mode='markers + lines',
                                  # 取对应每一条线路的经纬度信息
                                  lon=cd_metro.loc[lambda x: x['线路'] == line[0]]['经度'],
                                  lat=cd_metro.loc[lambda x: x['线路'] == line[0]]['纬度'],
                                  marker={'color': colors[line[2]],
                                          'size': 5},
                                  hovertext=cd_metro.loc[lambda x: x['线路'] == line[0]]['站名'],
                                  showlegend=True,
                                  name=('线路' + str(line[0]) + '|无约:' + str(line[1]))
                                  ) for line in zipped_lines])


fig.update_layout(mapbox={'accesstoken': token,
                          'center': {'lon': 116.4247,
                                     'lat': 39.9056},
                          'zoom': 11.8},
                  margin={'l': 0, 'r': 0, 't': 0, 'b': 0}
                  )

fig.write_html(r'D:\SRTP\网站和代码\cd_metro_38有约.html')
