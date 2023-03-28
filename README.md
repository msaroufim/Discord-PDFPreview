# Arxiv PDF Previewer in Discord

![image](https://user-images.githubusercontent.com/3282513/228138823-c8a2d981-953d-401b-baaf-6b322c5489a5.png)


## Installation

Get a token from https://discord.com/developers/applications and run `export DISCORD_BOT_TOKEN="YOUR_TOKEN_HERE"`

```
pip install -r requirements.txt
python main.py
```

Then add the bot to your Discord group


## Bot invitation

Just invite PDF Preview # 2277 to your channel. This bot is running on a cheap Heroku instance, depending on traffic I might scale it.


## Usage

1. `@PDF Preview https://arxiv.org/pdf/2012.03837.pdf` -> will render the first page of the PDF
2. `@PDF Preview https://arxiv.org/pdf/2012.03837.pdf#page=3` -> will render the third page of the PDF
2. `@PDF Preview https://arxiv.org/abs/2012.03837` -> Will find the corresponding pdf and render it


## Known issues
1. Some pdfs online don't have a `.pdf` extension, this won't quite work for those websites but it will work for arxiv
2. I'm not sure why but if you try to preview the same link multiple times in a row it won't render, I suspect it's some caching or anti-spam feature Discord has
3. The heroku deployment is still somewhat flaky
4. We need better logs in general, debugging things has been a pain
