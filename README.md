# LineBot
Linebot (AWS API Gateway + Lambda)

Please get LINE developers account and AWS account.
It is necessaly that AWS API Gateway and Lambda.

Lambda setting:
 runtime : python3.6
 handler : main.callback
 environment variable:
   CHANNEL_SECRET
   CHANNEL_ACCESS_TOKEN
   ※Check for the LINE developers site.

This program use the LINE SDK of Python.
This is already installed by pip those.
Please compress this program and upload it.

2017/09/09
 This LINE bot is very simple now. It returns the same reply as the sent message.
