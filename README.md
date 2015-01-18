# dj-discuss
[NOT READY!] Django project for public discussion on the web.

The last live vesion is [https://trial-filipkral.c9.io](https://trial-filipkral.c9.io)

# How to use
Exact settings and steps depend on how you have your django project set up so the steps below may not always work.

1) Add download the app and add it to django apps.

2) Add the discuss app to settings.py under INSTALLED_APPS.

3) Makse sure settings.py defines static root, e.g. `STATIC_ROOT = '/var/www/discuss-static'`

4) Add the discuss app to your project's urls.py, e.g. `url(r'^$', include('discuss.urls', namespace="discuss"))`. The namespace has to be `discuss`!

5) Run `python manage.py migrate`

6) Run `python manage.py collectstatic`

7) Run the server and direct your web browser to the discuss home url.

Done.
