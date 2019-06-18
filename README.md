# PDF Previer in Discord

## What works
* You can render the first page of a pdf in Discord
* Bot is totally OK to use locally and I've been using with fren

Just make sure to put in an app token and you should be good to go

![Capture.JPG](Capture.JPG)

## What still needs to be done
* Right now files are saved, which will cause naming issues and unecessary storage on the server
* Doesn't work for pdf links that aren't stored on a site only remote which is ideal for things like arxiv, but this could be done easily
* URL matching needs to be more robust than .pdf, because it'll break if you type .pdf right now if there isn't a url
* Need graceful error handling
* Right now only shows first page but could either make it a param to navigate to second, third etc pages or allow navigation directly in discord (which would be amazing but not clear how if Discord supports slideshows right now)
* Support some options to resize the preview



