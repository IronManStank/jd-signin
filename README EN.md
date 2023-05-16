# JingDong_AutoSignin
Auto Sign in JD and daily check in. 
# Features
- [x] Auto sign in 
- [x] Use wx_push_services to push the sign-in results and view directly in Enterprise WeChat (optional, not required). For wx_push_services configuration, please refer to ![wx_push_services](https://github.com/IronManStank/WX-Push-Services)
- [x] Use GitHub Action to run on schedule, no server required, no configuration required, ready to use. 
- [x] If you use a local server, you can directly use the wx_push_services command line push method to push messages.
- [x] Use the JD_COOKIE parsing engine (Reslove_JD_Cookie) to automatically parse JD_COOKIE without manually finding pt_key and pt_pin. 
## About Reslove_JD_Cookie:
It provides three ways to get JD_COOKIE:
1. Environment variable: First try to get from the JD_COOKIE environment variable. If it exists, return it. We highly recommend using this method to add COOKIE. 
2. Local file: If the environment variable does not exist, try to get from the cookies.txt file in the current directory.
3. Manual input: If the first two methods fail, prompt the user to manually enter JD_COOKIE.
## Usage
1. Run on a local server:
- Install dependencies: 
pip install -r requirements.txt
- Run: 
python Auto_SignIn.py
2. Run on GitHub Action:
1. Fork this repository to your GitHub account
2. Open your forked repository and click "Actions" 
3. Click "Run workflow" to run GitHub Action
## Communication Feedback
If you have any questions or suggestions during use, please submit an issue to communicate with me. 
I will actively answer your questions and continue to optimize and update the scripts. Thank you for your use and support!
## Finally 
If there is a problem, please reconfigure JD_COOKIE or submit an issue to communicate with me. 
This JD sign-in solution implements truly automated sign-in through cookie management, automatic script updates, push notifications and a series of designs. It allows us to easily complete all JD sign-in activities without having to manually sign in every day. 
I hope it can bring convenience and allow us to rediscover the simple pleasures of life!