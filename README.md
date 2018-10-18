# django news

This is a fork of monokrome/django-news by Brandon R. Stoner <monokrome@monokro.me>.

## Original description:

A django application for posting news. This is a fairly decent *news or blogging* application, and easily provides features like comments, and RSS and ATOM feeds at no cost. However it makes no assumptions regarding your design, and therefore doesn't include any WYSIWYG/WYSIWYM editors or anything like that. You can easily add your own by simply applying it to <textarea> elements with a 'text-edit' class. This application also ties into the django user authentication system to allow multiple users to post, edit, and delete news articles on the web site.

## Tweaks by:

* Byron Ruth <b@devel.io>
* Kevin Murphy <murphyke@email.chop.edu>
* Jeremy Leipzig <leipzig@gmail.com>

## Release Notes

0.7.0 - Differences from the monokrome version:

* Remove defaulting the summary to a slice of the body
* Add prefix to slug, clean update formatting
* Ensure the created datetime has been set
* Rename created_on to created, add modified, remove fixtures
* Include date in slug to prevent unique clashes

0.7.1 - Updated for Haystack 2.X

0.8.0 - Changes to deal with deprecation of markup.templatetags

0.8.1 - 2to3