# LineBot
Linebot (AWS API Gateway + Lambda)

Please get LINE developers account and AWS account.<br>
It is necessaly that AWS API Gateway and Lambda.<br>

**Lambda setting:**<br>
 runtime : python3.6<br>
 handler : main.callback<br>
 environment variable: <br>
 　　　CHANNEL_SECRET<br>
 　　　CHANNEL_ACCESS_TOKEN<br>
 　　　※Check for the LINE developers site. <br>

This program use the LINE SDK of Python.<br>
This is already installed by pip those.<br>
Please compress this program and upload it.<br>

2017/09/09<br>
 This LINE bot is very simple now. It returns the same reply as the sent message.<br>
test