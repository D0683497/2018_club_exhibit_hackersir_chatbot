# -*- coding: utf-8 -*-
FB_TOKEN = ''
LINE_TOKEN = []

DEFAULT_BUTTON=["黑客社介紹","新生茶會","社課","我要領獎品","粉絲專頁","Linux指令"]
CLASS_BUTTON = ["python","iot","資安","金融科技與資料科學活動","回目錄"]
WORD = {
    "help":{
            "text":'輸入\n"黑客社介紹"\n"新生茶會"\n"社課"\n"我要領獎品"\n"粉絲專頁"\n"Linux指令"\n試試看'
        },
    "回目錄":{
            "text":"還想知道甚麼呢"
        },
    "Linux指令":{
            "text":"這是模擬Linux系統的快來玩，直接輸入指令，試試看底下指令(還有其他指令可以玩喔)",
            "button":["ping 1.1.1.1 -c 1","ls"]
        },
    "新生茶會":{
        "text":"新生茶會時間為:9/18\n晚上 18:30準時開始\n地點為:IOT Lab(科航八樓)",
        "button":["科航八樓在哪?"]
        },
    "科航八樓在哪?":{
        "text":"從資電館往南走\n在商學院右邊\n請從科航館左邊門進入電梯\n搭往8樓\n地圖:https://goo.gl/maps/6uNUywmbjU32",
        "pic":["https://i.imgur.com/D8kttzl.jpg","https://i.imgur.com/D8kttzlm.jpg"]
        },
    "黑客社介紹":{
        "text":"黑客社社課在幫助社員了解電腦的運作\n從硬體設備知識的累積到各種軟體網頁開發維護都在我們社課的範圍內\n不論你只是純粹喜歡打遊戲、希望能自己寫外掛\n或是你立志成為板手工具人、+遍逢甲妹子的賴(?\n都歡迎上進的你加入我們，一起解決更多的bugs"
        },
    "社課":{
        "text":"我們有三路社課和講座，\n想了解甚麼呢？",
        "button":CLASS_BUTTON
        },
    "歡迎":{
            "text":"嗨！我是小黑，很開心成為你的好友！\n有關黑客社的事情可以問我喔！\n輸入help了解可用指令\n(所有對話紀錄並不會由真人查看\n有需要請密粉絲專頁)",
            "button":DEFAULT_BUTTON
        },
    "python":{
        "text":"「python」社課時間為:\n每週星期二 晚上18:30~21:00\n主要內容為python基礎及爬蟲教學\n來茶會了解更多!",
        "button":CLASS_BUTTON
        },
    "資安":{
        "text":"「資汛安全」社課時間為:\n每週星期三 晚上18:30~21:00\n主要內容為駭客教學^^\n來茶會了解更多!",
        "button":CLASS_BUTTON
        },
    "iot":{
        "text":"「Internet Of Thing」社課時間為:\n每週星期一 晚上18:30~21:00\n主要內容為arduino基礎\n來茶會了解更多!",
        "button":CLASS_BUTTON
        },
    "金融科技與資料科學活動":{
        "text":"「金融科技與資料科學活動」\n是我們與「財富管理社」所舉辦的系列演講\n第一堂題目為：資料科學簡介\n時間為:9月28日(五) 18:30 ~ 21:00\n報名網址:https://act.hackersir.org/",
        "button":CLASS_BUTTON
        },
    "我要領獎品":{
        "text":"我們有三個遊戲可以玩\n第一個:快問快答\n第二個:RPG小遊戲(無獎品)\n第三個:LINE的聊天室尋寶(難)\n要玩哪個呢?",
        "button":["快問快答","RPG小遊戲","LINE聊天室尋寶"]
        },
    "快問快答":{
        "text":"在有限的時間內，回答題目\n得分大於等於7，即可來攤位兌換L夾\n(獎品有限要玩要快)\n網址:https://goo.gl/cYTCT4"
        },
    "RPG小遊戲":{
        "text":"跟著劇情回答問題，踏入駭客的領域\n(難度:簡單，無獎品)\n網址:https://goo.gl/j8ExnC"
        },
    "LINE聊天室尋寶":{
                "text":"有沒有注意到\n這個聊天室可以輸入指令\n因為他連到我們伺服器內部\n使用指令找到隱藏的文字\n來攤位兌換神秘禮物(難度:難，獎品僅有三個!)",
                 "button":["ls /"]
        },
    "粉絲專頁":{
        "text":"粉絲專頁網址:https://www.facebook.com/HackerSir.tw/\n我們各種最新資訊會在這裡發佈!!"
    },
}
