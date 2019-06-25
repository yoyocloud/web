

# 数据:账号  密码   预期结果
url="http://120.78.128.25:8765/Index/login.html"

user_info_success={'username':'18684720553','pwd':'python','expected':'退出'}


#错误提示出现在按钮下方
user_down_error=[
    {'username':'','pwd':'','expected':'请输入手机号'},
    {'username':'123','pwd':'','expected':'请输入正确的手机号'},
    {'username':'18684720553','pwd':'','expected':'请输入密码'},

]
#错误提示出现在页面中间
user_mid_authorize = [
    {'username': '18211111111', 'pwd': 'python', 'expected': '此账号没有经过授权，请联系管理员!'},
    {'username': '18684720553', 'pwd': 'python777', 'expected': '帐号或密码错误!'}
]