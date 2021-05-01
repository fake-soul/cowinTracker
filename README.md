# cowinTracker

For Paid Cowin SLots

First of all, create a bot using Telegram BotFather. To create a BotFather follow the below steps –

    Open the telegram app and search for @BotFather.
    Click on the start button or send “/start”.
    Then send “/newbot” message to set up a name and a username.
    After setting name and username BotFather will give you an API token which is your bot token.
The second step is go get the chat_id:

    Visit https://api.telegram.org/bot<YourBOTToken>/getUpdates and get the chat_id under the key message['chat']['id'].

Replace Token ,chatID, date, pincode.
better to run for currentDate

update the sleep and scriptEndTime according to you

Cowin API's gives Not 200 response sometimes


