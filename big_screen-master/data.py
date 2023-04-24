class SourceDataDemo:

    def __init__(self):
        self.title = '城市公交服务不可靠性社会成本评价系统'
        self.counter = {'name': '浪费总时间', 'value': 12581189}
        self.counter2 = {'name': '相当于寿命/年', 'value': 3912410}
        self.echart1_data = {
            'title': '时间时间',
            'data': [
                {"name": "1", "value": 47},
                {"name": "2", "value": 52},
                {"name": "3", "value": 90},
                {"name": "4", "value": 84},
                {"name": "5", "value": 99},
                {"name": "6", "value": 37},
                {"name": "7", "value": 2},
            ]
        }
        self.echart2_data = {
            'title': '省份分布',
            'data': [
                {"name": "浙江", "value": 47},
                {"name": "上海", "value": 52},
                {"name": "江苏", "value": 90},
                {"name": "广东", "value": 84},
                {"name": "北京", "value": 99},
                {"name": "深圳", "value": 37},
                {"name": "安徽", "value": 150},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车", "value": 4},
                {"name": "旅游", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '省份',
            'data': [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ]
        }
        self.echart6_data = {
            'title': '一线城市',
            'data': [
                {"name": "浙江", "value": 80, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "上海", "value": 70, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "广东", "value": 65, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "北京", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "深圳", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '海门', 'value': 239},
                {'name': '鄂尔多斯', 'value': 231},
                {'name': '招远', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '北京市公交服务不可靠性社会成本评价系统'
        self.counter = {'name': '浪费总时间/小时', 'value': 604715}
        self.counter2 = {'name': '相当于寿命/年', 'value': 69}
        self.echart1_data = {
            'title': '有约时间',
            'data': [
                {"name": "1号线", "value": 537},
                {"name": "2号线", "value": 248},
                {"name": "3号线", "value": 82},
                {"name": "4号线", "value": 189},
                {"name": "5号线", "value": 165},
                {"name": "6号线", "value": 140},
                {"name": "7号线", "value": 133},
                {"name": "8号线", "value": 262},
                {"name": "9号线", "value": 149}
            ]
        }
        self.echart2_data = {
            'title': '无约时间',
            'data': [
                {"name": "1号线", "value": 4480},
                {"name": "2号线", "value": 1458},
                {"name": "3号线", "value": 903},
                {"name": "4号线", "value": 1517},
                {"name": "5号线", "value": 1309},
                {"name": "6号线", "value": 939},
                {"name": "7号线", "value": 1284},
                {"name": "8号线", "value": 1686},
                {"name": "9号线", "value": 1090}
            ]
        }
        self.echarts3_1_data = {
            'title': '东大桥-弘燕',
            'data': [
                {"name": "起点", "value": 236},
                {"name": "中间", "value": 220},
                {"name": "末端", "value": 237}
            ]
        }
        self.echarts3_2_data = {
            'title': '东直门-金家村',
            'data': [
                {"name": "起点", "value": 57},
                {"name": "中间", "value": 80},
                {"name": "末端", "value": 60}
            ]
        }
        self.echarts3_3_data = {
            'title': '二里庄-动物园',
            'data': [
                {"name": "起点", "value": 68},
                {"name": "中间", "value": 89},
                {"name": "末端", "value": 70}
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "有约", "value": [537, 248, 82, 189, 165, 140, 133, 262, 149, 151, 99, 130,
                                           131, 140, 126, 54, 43, 191, 50, 129, 134, 119, 107]},
                {"name": "无约", "value": [4480, 1458, 903, 1517, 1309, 939, 1284, 1686, 1090, 1186, 980, 1075,
                                           1223, 1223, 1024, 640, 666, 1644, 734, 1076, 908, 987, 1006]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12',
                      '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '东直门-金家村',
            'data': [
                {"name": "无约高峰期", "value": 132},
                {"name": "无约非高峰期", "value": 87},
                {"name": "有约高峰期", "value": 1241},
                {"name": "有约非高峰期", "value": 896}
            ]
        }
        self.echart6_data = {
            'title': '无约：有约',
            'data': [
                {"name": "月坛南街北-公主坟西", "value": 269, "value2": 2014, "color": "01", "radius": ['59%', '70%']},
                {"name": "西安门-六里桥东", "value": 281, "value2": 2015, "color": "02", "radius": ['49%', '60%']},
                {"name": "安华桥北-北京西", "value": 224, "value2": 2942, "color": "03", "radius": ['39%', '50%']},
                {"name": "金台路口西-金家村桥东", "value": 312, "value2": 3056, "color": "04", "radius": ['29%', '40%']}
            ]
        }
