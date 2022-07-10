# AutoTemp beta

**请注意，任何人有自由选择填写真实或虚假体温的权利，并非不使用本工具就无法填写虚假体温，望周知**

### 更新计划

本工具处于Beta阶段，目前并不易于使用

- 添加GUI
- 自动为用户下载适配的Chrome版本
- 增加登录方式

### 更新日志

2022.7.10 将填写行数决定方式由固定数字换为按时间自动分辨

### 自行运行/编译

若您不打算自行编译或在Python解释器环境下运行本程序，则您可以跳过该章节

确认你拥有较高版本的Python 3环境（推荐3.10.4）

在项目根目录下的命令行中运行`pip install -r requirements.txt`

这将自动安装所有依赖库

这时运行`python main.py`即可在命令行中运行本程序

或先运行`python -m pyinstaller main.py -F`对本程序进行编译

编译后的可执行文件将存放在dist目录下

自行编译后依旧不可直接使用，请参考使用章节

### 直接下载

直接在releases下下载可执行文件main.exe

接下来请参考使用章节

### 使用

1.  请确保您安装了Google Chrome
2. 请访问[谷歌官方仓库](http://chromedriver.storage.googleapis.com/index.html)下载**与您的Google Chrome版本相同的**Chrome Driver
3. 将其放置在Google Chrome安装路径下，一般为`C:\Program Files\Google\Chrome\Application`（即与chrome.exe同目录）
4. 首次运行程序，这将在运行目录下生成setting.json（以下称配置文件）
4. 在电脑上启动PC版QQ（这是因为本程序目前只支持点击自动登录图片登录QQ账号）
5. 适当配置该文件后再次启动本程序（配置方法参考配置章节）

### 使用

如果您并不完全清楚JSON语法或无法理解参数的意义，在修改设置文件时请小心，读取了错误的配置文件将导致本程序闪退、陷入死循环或其他问题。

若您自认无法还原正确的语法，请将配置文件移出本目录后再次运行以再次取得默认配置文件

- sheet_url 本参数应为电子表格的URL
- driver_path 本参数应为chromedriver.exe的路径
- user_name 本参数应为被填写温度人的名字
- temp_set 本参数由三个子参数组成，填写的随机温度将为x(x=min+step*n&n∈Z&x<=max)。请注意子参数为字符串格式而非浮点数格式
- login_wait 本参数控制程序等待自动登录所花费的时间（秒）
- wait_max 本参数控制程序等待页面元素加载的最长时间（加载时间超过该时间将导致程序直接退出）（秒）
- keyboard_wait 本参数控制程序等待页面响应部分模拟键盘操作所花费的时间（秒）
- start_time 本参数应为填写的开始日期，前两个数字分别为填写开始日期的月和日，最后一个数字为0（上午）/1（中午）/2（下午）
- day_div 本参数控制了程序如何分辨上午、中午与下午，第一个数字为上午与中午午分割的时间，第二个数字为中午与下午的
- save_wait 本参数控制程序填写完成后等待页面提交更改所花费的时间（秒）
- is_headless 本参数控制程序是否在隐藏浏览器界面模式下运行
