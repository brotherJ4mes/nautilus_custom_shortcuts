#!/usr/bin/env python # -*- coding: utf-8 -*- #
# by Ricardo Lenz, 2016-jun
# riclc@hotmail.com
#

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

def ok():
    app = Gtk.Application.get_default()
    # HERE ARE THE ACTUAL REMAPPINGS
    # usage:  set_accels_for_action( detailed_action_name,  [desiredShortcut] )
    app.set_accels_for_action( "win.new-tab", ["<super>t"] )
    app.set_accels_for_action( "win.up", ["BackSpace"] )
    app.set_accels_for_action( "win.close-current-view", ["<super>w"] )
    app.set_accels_for_action( "win.tab-previous", ["<super>bracketleft"] )
    app.set_accels_for_action( "win.tab-next", ["<super>bracketright"] )
    app.set_accels_for_action( "view.copy", ["<super>c"] )
    app.set_accels_for_action( "view.paste", ["<super>v"] )
    app.set_accels_for_action( "app.show-hide-sidebar", ["<ctrl>b"] )
    #app.set_accels_for_action( "Terminal", ["F12"] ) # replaced with xdotool shift+f10 + e
    #app.set_accels_for_action( "open.folder.local", ["F12"] ) # replaced with xdotool shift+f10 + e

    # this section is to determine the gtk "detailed_action_name"
    # i.e. the first argument to the set_accels function above
    # you must know the default shortcuts (use xev to get the keysym)
    #print(app.get_actions_for_accel("<ctrl>t"))
    #print(app.get_actions_for_accel("<ctrl>w"))
    #print(app.get_actions_for_accel("<ctrl>Prior"))
    #print(app.get_actions_for_accel("<ctrl>Next"))
    #print(app.get_actions_for_accel("<ctrl>c"))
    #print(app.get_actions_for_accel("F9"))

class BackspaceBack(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass
    
    def get_widget(self, uri, window):
        ok()
        return None

