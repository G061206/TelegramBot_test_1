#!/bin/bash
# Telegram Bot 一键部署脚本
# 适用于 Ubuntu 服务器

set -e  # 遇到错误时退出

# ===== 配置区域 =====
BOT_TOKEN="YOUR_BOT_TOKEN_HERE"  # 🔴 请替换为你的 Bot Token
REPO_URL="https://github.com/G061206/TelegramBot_test_1.git"
DEPLOY_DIR="$HOME/TelegramBot_test_1"
SERVICE_NAME="telegram-bot"
# ===================

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Telegram Bot 自动部署脚本 v1.0     ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# 检查是否配置了 Token
if [ "$BOT_TOKEN" == "YOUR_BOT_TOKEN_HERE" ]; then
    echo -e "${RED}❌ 错误：请先编辑脚本并配置你的 BOT_TOKEN${NC}"
    echo -e "${YELLOW}使用命令：nano deploy.sh${NC}"
    exit 1
fi

echo -e "${YELLOW}[1/6] 更新系统并安装依赖...${NC}"
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git

echo -e "${GREEN}✓ 依赖安装完成${NC}"
echo ""

echo -e "${YELLOW}[2/6] 克隆或更新代码仓库...${NC}"
if [ -d "$DEPLOY_DIR" ]; then
    echo "目录已存在，拉取最新代码..."
    cd "$DEPLOY_DIR"
    git pull
else
    echo "克隆仓库..."
    git clone "$REPO_URL" "$DEPLOY_DIR"
    cd "$DEPLOY_DIR"
fi

echo -e "${GREEN}✓ 代码获取完成${NC}"
echo ""

echo -e "${YELLOW}[3/6] 配置 Python 虚拟环境...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${GREEN}✓ 虚拟环境配置完成${NC}"
echo ""

echo -e "${YELLOW}[4/6] 创建环境变量文件...${NC}"
cat > .env << EOF
BOT_TOKEN=$BOT_TOKEN
EOF

echo -e "${GREEN}✓ 环境变量配置完成${NC}"
echo ""

echo -e "${YELLOW}[5/6] 配置 systemd 服务...${NC}"

# 创建服务文件
sudo tee /etc/systemd/system/$SERVICE_NAME.service > /dev/null << EOF
[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$DEPLOY_DIR
Environment="PATH=$DEPLOY_DIR/venv/bin"
ExecStart=$DEPLOY_DIR/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 重载 systemd
sudo systemctl daemon-reload

echo -e "${GREEN}✓ 服务配置完成${NC}"
echo ""

echo -e "${YELLOW}[6/6] 启动 Bot 服务...${NC}"

# 启动并启用服务
sudo systemctl enable $SERVICE_NAME
sudo systemctl restart $SERVICE_NAME

# 等待服务启动
sleep 2

# 检查状态
if sudo systemctl is-active --quiet $SERVICE_NAME; then
    echo -e "${GREEN}✓ Bot 启动成功！${NC}"
else
    echo -e "${RED}❌ Bot 启动失败，请查看日志${NC}"
    sudo systemctl status $SERVICE_NAME
    exit 1
fi

echo ""
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         🎉 部署完成！                 ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}📍 Bot 已在后台运行并设置为开机自启${NC}"
echo ""
echo -e "${YELLOW}常用管理命令：${NC}"
echo -e "  查看状态：sudo systemctl status $SERVICE_NAME"
echo -e "  查看日志：sudo journalctl -u $SERVICE_NAME -f"
echo -e "  重启服务：sudo systemctl restart $SERVICE_NAME"
echo -e "  停止服务：sudo systemctl stop $SERVICE_NAME"
echo ""
echo -e "${BLUE}现在你可以在 Telegram 中测试你的 Bot 了！${NC}"
