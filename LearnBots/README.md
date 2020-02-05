# Botkit template

This project implements a Botkit + Webex Teams adapter bot, based on the [generator-botkit](https://www.npmjs.com/package/generator-botkit) Yoeman template, providing a few extra good-practice features, plus several interesting samples:

- A 'health check' URL: check bot availability, uptime and metadata by browsing to the bot's public URL

- Quality-of-life features: fallback/catch-all module, welcome message when user joins a space

- 'Help' command auto-generation framework

- Redis/MongoDB storage support for persistent/scalable storage of conversation state

- checkAddMention() function to automatically format bot commands for 1:1 or group space usage

## How to run (local machine)

Assuming you plan to expose your bot via [ngrok](https://ngrok.com), you can run this template in a jiffy:

1. Clone this repo:

    git clone https://github.com/CiscoDevNet/botkit-template.git

2. Install the Node.js dependencies:

    npm install

3. Create a Webex Teams bot account at ['Webex for Developers'](https://developer.webex.com/my-apps/new/bot), and note/save your bot's access token

4. Launch ngrok to expose port 3000 of your local machine to the internet:

    ngrok http 3000
    Note/Save the 'Forwarding' HTTPS (not HTTP) address that ngrok generates

5. Edit the `.env` file and configure the settings and info for your bot.

    >Note: you can also specify any of these settings via environment variables (which will take precedent over any settings configured in the `.env` file)...often preferred in production environments

    To successfully run, you'll need to specify at minimum a `PUBLIC_URL` (ngrok HTTPS forwarding URL), and a `WEBEX_ACCESS_TOKEN` (Webex Teams bot access token)

    Additional values in the `.env` file (like `OWNER` and `CODE`) are used to populate the healthcheck URL metadata.

    Be sure to save the `.env` file!

6. You're ready to run your bot:

    node bot.js
