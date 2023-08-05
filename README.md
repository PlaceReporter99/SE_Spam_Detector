# SE Spam Detector
Searches for spam in Stack Exchange.
## How does it work?
Lots of spam posts contain phone numbers in their title. This scans question URLs for phone numbers using a RegEx expression.
## Where is the spam list?
It's in the spam_posts.md file.
## A non-spam post constantly appears. Why?
It's [this post](https://stackapps.com/questions/10264/spam-detector-detect-spam-posts-section-just-to-test-it-736-555-007-3), and I intentionally included a fake phone number in the title to test this spam detector. It's just a control test, essentially.
