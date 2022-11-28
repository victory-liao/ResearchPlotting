# -*- coding:utf-8 -*-

# 导入所需要的包
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from matplotlib.font_manager import FontProperties  # 字体管理器
import random


def plot_confusion_matrix(true_label, pred_label):
	# 设置汉字格式
	font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
	
	sns.set()
	f, ax = plt.subplots()
	C2 = confusion_matrix(true_label, pred_label, labels=[0, 1])
	sns.heatmap(C2, annot=True, ax=ax)  # 画热力图
	
	plt.title("混淆矩阵", fontproperties=font)  # 设置标题
	plt.xlabel('预测值', fontproperties=font)  # 设置x轴标题
	plt.ylabel('真实值', fontproperties=font)  # 设置y轴标签
	
	# 保存绘图
	plt.savefig("./confusion_matrix.png")
	
	# 绘图
	plt.show()


if __name__ == "__main__":
	true_label = [random.randint(0, 1) for i in range(0, 100)]
	pred_label = [random.randint(0, 1) for i in range(0, 100)]
	plot_confusion_matrix(true_label, pred_label)
