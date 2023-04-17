*Nautilus Custom Shortcuts*
-----------------------
Brings back the ability to add basic custom shortcuts to Nautilus (Gnome "Files")

Custom keyboard shortcuts (a.k.a. "accels") were previously a feature in Nautilus but this was discontinued in 3.15.4:
[(release notes)](https://gitlab.gnome.org/GNOME/nautilus/-/blob/master/NEWS)

This is accomplished with nautilus-python via a single python file.   TBH, I don't really understand how it works, github user [riclc](https://github.com/riclc) wrote the original "nautilus_backspace" repo which is setup for a single, specific shortcut and I just used that as a template and added print statements so I could figure out the other shortcuts.

(As a former mac user, I prefer super based shortcuts so, by default,  this is configured to open and navigate tabs with super+t, super+], etc. though it can be changed to suit any needs as long as the shortcut already exists in nautilus.)


Installation
-----------------------
1) Install [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython) (`apt-get install python-nautilus` in Debian-based distributions)
 
2) Download `accels.py` and put it here: `.local/share/nautilus-python/extensions/`
(you might have to create this directory first)

3) Restart Nautilus (`killall nautilus; nautilus &`)


Configuration
----------------------------
note: you only need edit the `ok` method for configuration

1) View `accels.py` and uncomment/edit any `print` statements with get_actions_for_acce

2) Launch nautilus from command line so you can view output

3) Do any simple navigation (e.g. click a folder) and check terminal for printed output.
   This will provide you with the "detailed_action_name" needed for the actual remapping.
   
4) Use the action name from 3 to edit `accels.py` within the  `app.set_accels_for_action` function.  Restart nautilus to confirm it worked.
