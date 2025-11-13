import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("❌ 未找到 BOT_TOKEN，请检查 .env 文件")

# /start 命令处理
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 欢迎使用 Telegram Bot！\n\n"
        "可用命令：\n"
        "/start - 显示欢迎消息\n"
        "/help - 获取帮助\n"
        "/about - 关于本 Bot"
    )

# /help 命令处理
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 帮助信息\n\n"
        "这是一个简单的 Telegram Bot。\n"
        "您可以发送任何消息，我会回复您！\n\n"
        "命令列表：\n"
        "/start - 开始使用\n"
        "/help - 查看此帮助\n"
        "/about - 关于信息"
    )

# /about 命令处理
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ 关于\n\n"
        "这是一个使用 python-telegram-bot 库开发的 Telegram Bot。\n"
        "项目地址: https://github.com/G061206/TelegramBot_test_1"
    )

# 处理普通文本消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"您说：{user_message}\n\n我收到了您的消息！👍")

# 主函数
def main():
    print("🚀 Bot 正在启动...")
    
    # 创建应用
    application = Application.builder().token(BOT_TOKEN).build()
    
    # 注册命令处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    
    # 注册消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ Bot 启动成功！")
    
    # 启动 Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
