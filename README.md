Python-YouTube-Example
=======================

This repo contains simple examples of interacting with YouTube using python.

It requires the google API pythin library found here:

https://code.google.com/p/gdata-python-client/

Useful info on the library can be found here:

https://developers.google.com/youtube/1.0/developers_guide_python

All of the scripts in this repo login to YouTube using this library and require the following environment variables to be set:

email (YouTube email used to sign in),
password (YouTube password used to sign in),
source (YouTube channel name),
dev_key (YouTube developer key for the Product you have registered.)


##### youtube_printuploads.py

The youtube_printuploads.py script logins to youtube and it requires an additional environment variable:

user_id (User id for YouTube channel you want to get the uploads info from).

Once you have set this additional environment variables, then run the script as follows:

<pre>
python youtube_printuploads.py
</pre>

It should print out details of all of the uploaded videos for the specifed user.
