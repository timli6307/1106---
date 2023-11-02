student = {}
student['sid'] = input("請輸入您的學號：")
student['sname'] = input("請輸入您的姓名：")
student['china'] = float(input("請輸入您的國文成績："))
student['math'] = float(input("請輸入您的數學成績："))
student['info'] = float(input("請輸入您的電腦成績："))

total_score = round(student['fchina'] + student['fmath'] + student['finfo'], 2)
average_score = round(total_score / 3, 2)

pass_status = "合格" if total_score >= 180 else "不及格"

print("-" * 30)
print(f"{student['sname']}({student['sid']})同學您好：")
print("以下是您的各科成積與分數評定")
print(f"國文：{student['china']} / 數學：{student['math']} / 電腦：{student['info']}")
print(f"總分：{total_score} / 平均：{average_score}")
print("-" * 30)
print(f"成績判定：{pass_status}")
