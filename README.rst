collective.addtohomescreen
==========================

Overview
--------

Collective.mobile.addtohomescreen is a Plone integration of  Matteo Spinelli's Add to Home screen product, developed by Quintagroup.

The script places a floating balloon inviting the user to add your website to the home screen. 

The code is compatible with Plone 4.x on iPhone/iPod touch and iPhone 4. On older devices the "add" icon is a "+" while on iOS 4.2 it has been replaced with "arrow". The script detects the OS version and displays the appropriate icon.

Autostart
---------

The script automatically starts on page load. But the message shows up to returning visitors only. The first time a user accesses your site the message is not shown. The message appears after 2 seconds from page load, and is destroyed after 15 seconds. The balloon enters and exits the screen with a quick animation: drop from top.

The balloon can be dismissed any time by tapping the small "x" icon. If the user intentionally closes the balloon, it will not show up again for 12 hours. This feature overrides all your configurations, even if you set the balloon to show up every single time, if the user taps the close button the message will not be shown until 12 hours have passed.

Localization
------------

The script  checks the user's locale and shows the message in an appropriate language. The Supported  languages are:

- Catalan
- Chinese (Traditional and Simplified)
- Danish
- Dutch
- English
- Finnish
- French
- German
- Greek
- Hebrew
- Hungarian
- Italian
- Japanese
- Korean
- Norwegian
- Polish
- Portuguese
- Russian
- Spanish
- Swedish
- Thai
- Turkish

Installation
------------

You can install collective.mobile.addtohomescreen on Plone 4.x websites. 

- Add the following to your buildout.cfg:

        eggs = 
            ...
            collective.mobile.addtohomescreen

        zcml =
            ...
            collective.mobile.addtohomescreen

- Rerun buildout, e.g. with:

        $ ./bin/buildout

- Restart the Zope server, e.g with the following command in the terminal:

        $ ./bin/instance restart

Configuration
-------------

You can define the website sections where the balloon should appear via *Site Setup -> Configuration registry*. After navigating to *Allowed url paths* enter the needed URLs and click *Save*. By default the script places the floating balloon on the home page. 

Authors
-------

- Taras Poburynnyi
- Roman Kozlovskyi
- The original concept and code was created by Matteo Spinelli  http://cubiq.org/
