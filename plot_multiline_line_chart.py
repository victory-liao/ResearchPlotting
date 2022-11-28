import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['font.size'] = 12  # 设置字体大小


def plot(label_name, metric_name, lists, language="english"):
	plt.plot(lists[0], marker="o", label="A", ls="solid")
	plt.plot(lists[1], marker="o", label="B", ls="dotted")
	plt.plot(lists[2], marker="o", label="C", ls="dashdot")
	plt.plot(lists[3], marker="o", label="D", ls="dashed")
	
	if language == "chinese":
		plt.xlabel("月份")
		plt.ylabel("收入")
		plt.title("四个公司每月的收入")
	elif language == "english":
		plt.xlabel("month")
		plt.ylabel("income")
		plt.title("Monthly income of four companies")
	else:
		print("不支持该语言！程序已退出！")
		exit()
	
	plt.grid(color='lightpink', linestyle='--', linewidth=0.5)
	plt.legend()
	plt.show()


if __name__ == "__main__":
	A_income = [1.2, 1.5, 1.1, 1.4, 1.6, 1.8, 2.0, 1.3, 1.9, 3.0, 1.0, 2.0]

	B_income = [0.8, 1.2, 1.5, 2.3, 1.8, 1.6, 0.5, 1.3, 2.0, 2.8, 2.0, 2.3]
	
	C_income = [0.5, 0.6, 0.8, 1.0, 1.2, 1.0, 1.5, 1.3, 1.4, 1.8, 1.6, 0.8]
	
	D_income = [1.3, 1.6, 1.5, 2.4, 2.5, 2.8, 3.0, 2.8, 1.2, 1.8, 1.5, 1.4]
	
	plot("valence", "acc", [A_income, B_income, C_income, D_income], language="chinese")