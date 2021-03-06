# django-custom-users

There are two ways to extend users in Django: the "profile" method and a custom user. We've already used the profile method for our first project, so now we'll cover the custom user.

This project is simply about implementing a custom user from the ground up so that you can use it in the next assignment.

#### **Your Task**

Implement your own login and signup page (don't use the defaults) for the server that leads to a locked-down "homepage". The homepage should show:

*   the username <span>of the person who is logged in</span>
*   the display name of the person who is logged in
*   the output the value of `settings.AUTH_USER_MODEL`

NOTE: DO NOT name any part of your app "user" -- it will have conflict with the built-in user model and give you all sorts of errors that are really difficult to debug if you don't know what you're looking for. Use "custom_user", "myuser", "dudewheresmyuser"... literally anything but "user" will work.
