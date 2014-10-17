import gdata.youtube
import gdata.youtube.service
import os

yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
yt_service.ssl = True

# A complete client login request
yt_service.email = os.environ.get('email')
yt_service.password = os.environ.get('password')
yt_service.source = os.environ.get('source')
yt_service.developer_key = os.environ.get('dev_key')
yt_service.ProgrammaticLogin()

def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  print 'Video published on: %s' % entry.published.text
  print 'Video description: %s' % entry.media.description.text
  print 'Video category: %s' % entry.media.category[0].text
  print 'Video tags: %s' % entry.media.keywords.text
  print 'Video watch page: %s' % entry.media.player.url
  print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds

  # non entry.media attributes
  print 'Video view count: %s' % entry.statistics.view_count

  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url)

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url

def PrintVideoFeed(feed):
  for entry in feed.entry:
    PrintEntryDetails(entry)

def GetAndPrintUserUploads(username):
  yt_service = gdata.youtube.service.YouTubeService()
  uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
  PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))

GetAndPrintUserUploads(os.environ.get('user_id'))
