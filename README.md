# About
This is generates a string of text using a randomly selected work from a Vocabulary file and uses this string to create a post on atproto. This Source Code is used to create posts on the [godspeakbot.bsky.social](godspeakbot.bsky.social) account on the Bluesky Social Network.
The .env file used in this project is not included in this Repository.

This Project was inspired by [TempleOS](https://templeos.org/)

Why did I make this? I think it's because I thought it'd be funny/amusing.
Is it Accurate? I'm not sure, I think it's not and if I can find the time to improve that I might, a lot of sources online have been convincing me this isn't accurate to the output of Terry A. Davis's GodSpeak Script that ran as a bash script (I've honestly never seen it), however I think his original script might have an output too verbose for Microblogging Social Networks like Bluesky to accept the output of (limited character counts and what not), so this is an unfortunate compromise to get the Word of God out on Social Media.

I ask that you not take this too seriously as a project, again I just find doing this amusing and I hope others do too.
# Dependencies
- [atproto](https://pypi.org/project/atproto/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) 
- [keyboard](https://pypi.org/project/keyboard/) 
- [Vocab.DD](https://github.com/cia-foundation/TempleOS/blob/archive/Adam/God/Vocab.DD) (This file can also be found within TempleOS itself, this is just a more convenient repository to obtain this file from)