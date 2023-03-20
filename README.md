# Arxiv PDF Previewer in Discord

## Installation

Get a token from https://discord.com/developers/applications and run `export DISCORD_BOT_TOKEN`

```
pip install -r requirements.txt
python main.py
```

Then add the bot to your Discord group


## Bot invitation

Just invite Arxiv Preview # 2277 to your channel. This bot is running on a cheap Heroku instance, depending on traffic I might scale it.

![Capture.JPG](Capture.JPG)

## Usage

1. `@PDF Preview https://arxiv.org/pdf/2012.03837.pdf` -> will render the first page of the PDF
2. `@PDF Preview https://arxiv.org/pdf/2012.03837.pdf#page=3` -> will render the third page of the PDF
2. `@PDF Preview https://arxiv.org/abs/2012.03837` -> Will find the corresponding pdf and render it


## Known issues
1. Some pdfs online don't have a `.pdf` extension, this won't quite work for those websites but it will work for arxiv
2. I'm not sure why but if you try to preview the same link multiple times in a row it won't render, I suspect it's some caching or anti-spam feature Discord has