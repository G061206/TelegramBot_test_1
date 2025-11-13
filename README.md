# Telegram Bot 项目

一个简单的 Telegram Bot，支持基本指令响应。

## 功能特性

- ✅ /start - 欢迎消息
- ✅ /help - 帮助信息
- ✅ /about - 关于信息
- ✅ 文本消息响应

## 快速部署到 Ubuntu 服务器

### 1. SSH 连接到服务器

```bash
ssh your_username@your_server_ip
```

### 2. 运行一键部署脚本

```bash
# 下载并运行部署脚本
curl -O https://raw.githubusercontent.com/G061206/TelegramBot_test_1/main/deploy.sh
chmod +x deploy.sh

# 编辑脚本，填入你的 Bot Token
nano deploy.sh
# 修改这一行：BOT_TOKEN="YOUR_BOT_TOKEN_HERE"

# 执行部署
./deploy.sh
```

### 3. 启动 Bot

部署完成后，Bot 会自动启动。你可以使用以下命令管理：

```bash
# 查看状态
sudo systemctl status telegram-bot

# 启动服务
sudo systemctl start telegram-bot

# 停止服务
sudo systemctl stop telegram-bot

# 重启服务
sudo systemctl restart telegram-bot

# 查看实时日志
sudo journalctl -u telegram-bot -f
```

## 手动部署步骤

如果你想手动部署，可以按以下步骤操作：

### 1. 安装依赖

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

### 2. 克隆仓库

```bash
git clone https://github.com/G061206/TelegramBot_test_1.git
cd TelegramBot_test_1
```

### 3. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 5. 配置环境变量

```bash
echo "BOT_TOKEN=你的Bot_Token" > .env
```

### 6. 运行 Bot

```bash
python bot.py
```

## 设置为系统服务（开机自启）

### 1. 编辑服务配置文件

```bash
sudo nano telegram-bot.service
```

将 `YOUR_USERNAME` 替换为你的实际用户名。

### 2. 安装服务

```bash
sudo cp telegram-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

### 3. 验证运行状态

```bash
sudo systemctl status telegram-bot
```

## 获取 Bot Token

1. 在 Telegram 中搜索 [@BotFather](https://t.me/botfather)
2. 发送 `/newbot` 命令
3. 按提示设置 Bot 名称和用户名
4. 获取 API Token（格式类似：`1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`）

## 更新代码

```bash
cd ~/TelegramBot_test_1
git pull
sudo systemctl restart telegram-bot
```

## 故障排查

### 查看日志
```bash
sudo journalctl -u telegram-bot -f
```

### 测试 Bot 是否正常
```bash
cd ~/TelegramBot_test_1
source venv/bin/activate
python bot.py
```

### 检查 Token 配置
```bash
cat .env
```

## 项目结构

```
TelegramBot_test_1/
├── bot.py                    # Bot 主程序
├── requirements.txt          # Python 依赖
├── .env                      # 环境变量（不提交到 Git）
├── .gitignore               # Git 忽略文件
├── deploy.sh                # 一键部署脚本
├── telegram-bot.service     # systemd 服务配置
└── README.md                # 项目说明
```

## 许可证

MIT License
