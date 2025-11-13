#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单的 Telegram Bot 示例
用于回复 /start 和其他基本指令
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 启用日志记录
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 处理 /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """当用户发送 /start 时的响应"""
    user = update.effective_user
    await update.message.reply_text(
        f'你好 {user.first_name}！👋\n\n'
        f'欢迎使用这个简单的 Bot！\n\n'
        f'可用指令：\n'
        f'/start - 显示欢迎信息\n'
        f'/help - 显示帮助信息\n'
        f'/about - 关于这个 Bot\n'
        f'/echo <消息> - 复读你的消息'
    )

# 处理 /help 指令
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """发送帮助信息"""
    help_text = (
        "📚 *帮助信息*\n\n"
        "这是一个简单的 Telegram Bot 示例。\n\n"
        "*可用指令：*\n"
        "/start - 开始使用 Bot\n"
        "/help - 显示此帮助信息\n"
        "/about - 关于这个 Bot\n"
        "/echo <消息> - Bot 会复读你的消息\n\n"
        "你也可以直接发送文本消息，Bot 会回复你！"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

# 处理 /about 指令
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """显示关于信息"""
    await update.message.reply_text(
        '🤖 *关于这个 Bot*\n\n'
        '这是一个使用 python-telegram-bot 库创建的简单示例 Bot。\n'
        '版本：1.0\n'
        '作者：Your Name',
        parse_mode='Markdown'
    )

# 处理 /echo 指令
async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """复读用户的消息"""
    if context.args:
        message = ' '.join(context.args)
        await update.message.reply_text(f'🔊 {message}')
    else:
        await update.message.reply_text('请在 /echo 后面输入要复读的内容，例如：/echo 你好')

# 处理普通文本消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """回复用户的普通消息"""
    user_message = update.message.text
    await update.message.reply_text(
        f'你发送了："{user_message}"\n\n'
        f'我收到了你的消息！😊\n'
        f'使用 /help 查看可用指令。'
    )

# 错误处理
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """记录错误"""
    logger.error(f'Update {update} caused error {context.error}')

def main() -> None:
    """启动 Bot"""
    # 在这里替换成你的 Bot Token
    TOKEN = '8434664041:AAGTRxDMSbZSI2oaWrnys2zkeOfnMadxBT4'
    
    # 创建 Application
    application = Application.builder().token(TOKEN).build()
    
    # 注册指令处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("echo", echo_command))
    
    # 注册消息处理器（处理非指令的普通文本消息）
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # 注册错误处理器
    application.add_error_handler(error_handler)
    
    # 启动 Bot
    logger.info('Bot 正在启动...')
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
