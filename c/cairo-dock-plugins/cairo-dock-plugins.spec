%define packagename cairo-dock
%define ver_major 3
%define ver_minor 0
%define ver_micro 0.0rc1

Summary: Plugins for cairo-dock
Name: cairo-dock-plugins
Version: %ver_major.%ver_minor
Release: alt%ver_micro.1
License: GPLv3+
Group: Graphical desktop/Other
Packager: Alexey Shabalin <shaba@altlinux.ru>
Url: https://launchpad.net/cairo-dock-plug-ins

Source: http://launchpad.net/cairo-dock-plug-ins/%version/%version.%ver_micro/+download/%name-%version.%ver_micro.tar
#.gz

Requires: cairo-dock >= %version

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: cmake-modules fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libX11-devel libXrender-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libdbus-glib-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-menus2 libgnutls-devel libgtk+3-devel libjavascriptcoregtk3-devel libpango-devel librsvg-devel libsoup-devel libstdc++-devel libxml2-devel mono mono-mscorlib ndesk-dbus pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email xorg-randrproto-devel xorg-renderproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: cairo-dock-devel cmake gcc-c++ libXrandr-devel libXxf86vm-devel libalsa-devel libetpan-devel libexif-devel libfftw3-devel libgnome-menus2-devel libgtk-sharp2 libical-devel libpulseaudio-devel libsensors3-devel libupower-devel libvte3-devel libwebkitgtk3-devel libxklavier-devel libzeitgeist-devel lsb-release mono-mcs ndesk-dbus-glib python-module-distribute ruby vala

BuildRequires: cairo-dock-devel >= %version
Requires: %packagename-common
Requires: %packagename-clock
Requires: %packagename-composite-manager
Requires: %packagename-dustbin
Requires: %packagename-logout
Requires: %packagename-rendering
Requires: %packagename-musicplayer
Requires: %packagename-scooby-do
Requires: %packagename-terminal
Requires: %packagename-powermanager
Requires: %packagename-shortcuts
Requires: %packagename-systray
Requires: %packagename-weather
Requires: %packagename-xgamma
Requires: %packagename-alsamixer
Requires: %packagename-cairo-penguin
Requires: %packagename-tomboy
Requires: %packagename-wifi
Requires: %packagename-netspeed
Requires: %packagename-switcher
Requires: %packagename-dbus
Requires: %packagename-showdesktop
Requires: %packagename-slider
Requires: %packagename-stack
Requires: %packagename-clipper
Requires: %packagename-gmenu
Requires: %packagename-animated-icons
Requires: %packagename-desklet-rendering
Requires: %packagename-dialog-rendering
Requires: %packagename-disks
Requires: %packagename-drop_indicator
Requires: %packagename-icon-effect
Requires: %packagename-illusion
Requires: %packagename-impulse
Requires: %packagename-motion_blur
Requires: %packagename-quick-browser
Requires: %packagename-recent-events
Requires: %packagename-show_mouse
Requires: %packagename-toons
Requires: %packagename-keyboard-indicator
Requires: %packagename-weblets
Requires: %packagename-network-monitor
Requires: %packagename-system-monitor
Requires: %packagename-mail
Requires: %packagename-dnd2share
Requires: %packagename-rssreader
Requires: %packagename-folders

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package contains various plugins for cairo-dock.

%files

#---------------------------------------------------------------------
%package -n %packagename-common
Summary: That common package provides lang files
Group: Graphical desktop/Other
Requires: %packagename = %version

%description -n %packagename-common
This plug-in provides many different animations for your icons.

%files -n %packagename-common -f %name.lang
%dir %_datadir/%packagename/plug-ins
%_datadir/%packagename/plug-ins/shared-files
%dir %_libdir/%packagename

#---------------------------------------------------------------------
%package -n %packagename-animated-icons
Summary: That package provides plugin "Animated icons"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-animated-icons
This plug-in provides many different animations for your icons.

%files -n %packagename-animated-icons
%_datadir/%packagename/plug-ins/Animated-icons
%_libdir/%packagename/libcd-Animated-icons.so

#---------------------------------------------------------------------
%package -n %packagename-clock
Summary: That package provides plugin "clock"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-clock
Display rime and date in your dock with the clock applet!
2 view are available: numeric and analogic.
It can derach itself to be the perfect clone of CairoClock.
It can warn you with alarms, can display a calendar, and
allow you to setup time and date.

%files -n %packagename-clock
%_datadir/%packagename/plug-ins/clock
%_libdir/%packagename/libcd-clock.so

#---------------------------------------------------------------------
%package -n %packagename-composite-manager
Summary: That package provides plugin "Composite-Manager"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-composite-manager
This applet allows you to toggle the composite ON/OFF.
The composite is what allows transparency on the desktop, but it can slow down
your PC, especially during games.
The applet also lets you acces to some actions of the Window-Manager.

%files -n %packagename-composite-manager
%_datadir/%packagename/plug-ins/Composite-Manager
%_libdir/%packagename/libcd-Composite-Manager.so

#---------------------------------------------------------------------
%package -n %packagename-desklet-rendering
Summary: That package provides plugin "desklet-rendering"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-desklet-rendering
This module provides different views for your desklets.

%files -n %packagename-desklet-rendering
%_datadir/%packagename/plug-ins/desklet-rendering
%_libdir/%packagename/libcd-desklet-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-dialog-rendering
Summary: That package provides plugin "dialog-rendering"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-dialog-rendering
This plug-in provides some dialog decorators for dialog bubbles.

%files -n %packagename-dialog-rendering
%_datadir/%packagename/plug-ins/dialog-rendering
%_libdir/%packagename/libcd-dialog-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-disks
Summary: That package provides plugin "Disks"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-disks
Monitors disks speed and space.
This applet show your disks informations. You can activate both options at
once, but they're better separated in 2 or more instances of the applet.

%files -n %packagename-disks
%_datadir/%packagename/plug-ins/Disks
%_libdir/%packagename/libcd-disks.so

#---------------------------------------------------------------------
%package -n %packagename-drop_indicator
Summary: That package provides plugin "drop_indicator"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-drop_indicator
This plug-in displays an animated indicator when you drop something in the dock.

%files -n %packagename-drop_indicator
%_datadir/%packagename/plug-ins/drop-indicator
%_libdir/%packagename/libcd-drop_indicator.so

#---------------------------------------------------------------------
%package -n %packagename-dustbin
Summary: That package provides plugin "dustbin"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-dustbin
Manage your disks space with this trash applet!
It can handle several trash directories,
threw files or unmount diisks with drag'n'drop,
warn you if you use too much space,
and display usefull info about your dustbins.

%files -n %packagename-dustbin
%_datadir/%packagename/plug-ins/dustbin
%_libdir/%packagename/libcd-dustbin.so

#---------------------------------------------------------------------
%package -n %packagename-icon-effect
Summary: That package provides plugin "icon-effect"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-icon-effect
This plug-in adds many special effects to your icons.

%files -n %packagename-icon-effect
%_datadir/%packagename/plug-ins/icon-effect
%_libdir/%packagename/libcd-icon-effect.so

#---------------------------------------------------------------------
%package -n %packagename-illusion
Summary: That package provides plugin "illusion"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-illusion
This plug-in provides animations for appearance & disappearance of icons.

%files -n %packagename-illusion
%_datadir/%packagename/plug-ins/illusion
%_libdir/%packagename/libcd-illusion.so

#---------------------------------------------------------------------
%package -n %packagename-impulse
Summary: That package provides plugin "Impulse"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-impulse
Did you know that your dock can dance? :)
If you click on this icon, the dock will dance!
In fact, you will have a graphical equalizer into the dock
It will analyse the signal given by PulseAudio.

%files -n %packagename-impulse
%_datadir/%packagename/plug-ins/Impulse
%_libdir/%packagename/libcd-Impulse.so

#---------------------------------------------------------------------
%package -n %packagename-logout
Summary: That package provides plugin "logout"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-logout
A very simple applet that adds an icon to log out
from your session.

%files -n %packagename-logout
%_datadir/%packagename/plug-ins/logout
%_libdir/%packagename/libcd-logout.so

#---------------------------------------------------------------------
%package -n %packagename-motion_blur
Summary: That package provides plugin "motion_blur"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-motion_blur
This plug-in adds a motion blur effect on docks.

%files -n %packagename-motion_blur
%_datadir/%packagename/plug-ins/motion-blur
%_libdir/%packagename/libcd-motion_blur.so

#---------------------------------------------------------------------
%package -n %packagename-quick-browser
Summary: That package provides plugin "quick-browser"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-quick-browser
This applet lets you browse a folder and its sub-folders very quickly.
You can set up a shortkey to pop up the menu. Midlle-click will open
the main folder.
This applet can be instanciated several times, if you want to browse
different folders.

%files -n %packagename-quick-browser
%_datadir/%packagename/plug-ins/quick_browser
%_libdir/%packagename/libcd-quick-browser.so

#---------------------------------------------------------------------
%package -n %packagename-recent-events
Summary: That package provides plugin "Recent-Events"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common
Requires: zeitgeist

%description -n %packagename-recent-events
This applet remembers you last actions to help you working faster.
It also adds related actions on other icons' menu.

%files -n %packagename-recent-events
%_datadir/%packagename/plug-ins/Recent-Events
%_libdir/%packagename/libcd-Recent-Events.so

#---------------------------------------------------------------------
%package -n %packagename-rendering
Summary: That package provides plugin "rendering"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-rendering
This module adds different views to your dock.
Any dock or sub-dock can be displayed with the
view of your choice. Currently, 3D-plane, Caroussel,
Parabolic and Rainbow views are provided

%files -n %packagename-rendering
%_datadir/%packagename/plug-ins/rendering
%_libdir/%packagename/libcd-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-musicplayer
Summary: That package provides plugin "musicPlayer"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-musicplayer
Control your Rhythmbox player directly in the dock!
Play/pause with left click, next song with middle click.

%files -n %packagename-musicplayer
%_datadir/%packagename/plug-ins/musicPlayer
%_libdir/%packagename/libcd-musicPlayer.so

#---------------------------------------------------------------------
%package -n %packagename-scooby-do
Summary: That package provides plugin "Scooby-Do"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-scooby-do
This plug-in allows you to make different actions directly from the keyboard.
It is triggered by a keyboard shortcut (by default: CTRL + Enter):
It lets you find and launch applications, files, recent files, firefox
bookmarks, commands, and even calculations.
Type what you want to search, the results will be displayed in real time.
The first results of each category are displayed in the main listing.
Use the up/down arrows to navigate inside the list,
and use the left/right arrows to enter into a category, or to display more
actions (when a little arrow is drawn next to text).
Once inside a category, you can filter the results by typing some letters.
Press Enter to validate, maintain SHIFT or ALT to keep the list of results opened.
Escape or the same shortkey will cancel.

%files -n %packagename-scooby-do
%_datadir/%packagename/plug-ins/Scooby-Do
%_libdir/%packagename/libcd-scooby-do.so

#---------------------------------------------------------------------
%package -n %packagename-terminal
Summary: That package provides plugin "terminal"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-terminal
Add a terminal to your dock!
You can drag'n'drop files or text into it
and select an action

%files -n %packagename-terminal
%_datadir/%packagename/plug-ins/terminal
%_libdir/%packagename/libcd-terminal.so

#---------------------------------------------------------------------
%package -n %packagename-powermanager
Summary: That package provides a powermanager plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-powermanager
A power manager for laptop's battery
It works with ACPI and DBus.

%files -n %packagename-powermanager
%_datadir/%packagename/plug-ins/powermanager
%_libdir/%packagename/libcd-powermanager.so

#---------------------------------------------------------------------
%package -n %packagename-shortcuts
Summary: That package provides a shortcuts plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-shortcuts
An applets thatlet you acces quickly to all of your shortcuts.
It can manage disks, network points, and Nautilus bookmarks.
You can add or remove bookmarks bye drag'n'drop, even if you
don't have Nautilus. Middle-click to acces your desktop easily

%files -n %packagename-shortcuts
%_datadir/%packagename/plug-ins/shortcuts
%_libdir/%packagename/libcd-shortcuts.so

#---------------------------------------------------------------------
%package -n %packagename-show_mouse
Summary: That package provides plugin "show_mouse"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-show_mouse
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %packagename-show_mouse
%_datadir/%packagename/plug-ins/show_mouse
%_libdir/%packagename/libcd-show_mouse.so

#---------------------------------------------------------------------
%package -n %packagename-systray
Summary: That package provides a systray plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-systray
Add a systray to your dock!

%files -n %packagename-systray
%_datadir/%packagename/plug-ins/systray
%_libdir/%packagename/libcd-systray.so

#---------------------------------------------------------------------
%package -n %packagename-toons
Summary: That package provides plugin "toons"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-toons
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %packagename-toons
%_datadir/%packagename/plug-ins/Toons
%_libdir/%packagename/libcd-Toons.so

#---------------------------------------------------------------------
%package -n %packagename-weather
Summary: That package provides a weather plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-weather
This applet displyas weather into your dock.
It can detach itself to be a ttally eye-candy 3D Desklet.
You can have many valuable info by (middle) clicking on
the icons. Data are provided by www.weather.com

%files -n %packagename-weather
%_datadir/%packagename/plug-ins/weather
%_libdir/%packagename/libcd-weather.so

#---------------------------------------------------------------------
%package -n %packagename-xgamma
Summary: That package provides a Xgamma plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-xgamma
Setup the gama of your screen directly from the dock.
It is a simple port of xgamma. Quickly setup gamma with
left click, or more accurately with middle click.

%files -n %packagename-xgamma
%_datadir/%packagename/plug-ins/Xgamma
%_libdir/%packagename/libcd-Xgamma.so

#---------------------------------------------------------------------
%package -n %packagename-alsamixer
Summary: That package provides a alsaMixer plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-alsamixer
This applet let you set up the sound volume from the dock.
Click on icon to show/hide volume comtrol (You can bin a
keyboard shortcut for it.)
Middle-click to set or unset mute. This applet works with
the Alsa sound drivers.

%files -n %packagename-alsamixer
%_datadir/%packagename/plug-ins/AlsaMixer
%_libdir/%packagename/libcd-AlsaMixer.so

#---------------------------------------------------------------------
%package -n %packagename-cairo-penguin
Summary: That package provides a Cairo-Penguin plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-cairo-penguin
Add a lively Penguin in your dock! Left click to change animation,
right click to disturb him ^_^.
Images are from Pingus, Inspiration is from xpenguins.

%files -n %packagename-cairo-penguin
%_datadir/%packagename/plug-ins/Cairo-Penguin
%_libdir/%packagename/libcd-Cairo-Penguin.so

#---------------------------------------------------------------------
%package -n %packagename-slider
Summary: That package provides a slider plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-slider
The slider applet is a basic image slider.

%files -n %packagename-slider
%_datadir/%packagename/plug-ins/slider
%_libdir/%packagename/libcd-slider.so

#---------------------------------------------------------------------
%package -n %packagename-stack
Summary: That package provides a stack plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-stack
This applet allows you to build a stack of items, just like the Stack
applet of MacOS X. Items can be files, folders, URL, or even pieces of
text.

%files -n %packagename-stack
%_datadir/%packagename/plug-ins/stack
%_libdir/%packagename/libcd-stack.so

#---------------------------------------------------------------------
%package -n %packagename-wifi
Summary: That package provides a wifi plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-wifi
The wifi applet show you the signal strenght of
the first active connection.

%files -n %packagename-wifi
%_datadir/%packagename/plug-ins/wifi
%_libdir/%packagename/libcd-wifi.so


#---------------------------------------------------------------------
%package -n %packagename-tomboy
Summary: That package provides a tomboy plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-tomboy
Control your TomBoy's notes directly in the dock!

%files -n %packagename-tomboy
%_datadir/%packagename/plug-ins/tomboy
%_libdir/%packagename/libcd-tomboy.so

#---------------------------------------------------------------------
%package -n %packagename-netspeed
Summary: That package provides a netspeed plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-netspeed
the netspeed applet show you the bit rate of your internet connection
and make some stats on it.

%files -n %packagename-netspeed
%_datadir/%packagename/plug-ins/netspeed
%_libdir/%packagename/libcd-netspeed.so

#---------------------------------------------------------------------
%package -n %packagename-switcher
Summary: That package provides a switcher plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-switcher
The new and soon wonderful switcher applet

%files -n %packagename-switcher
%_datadir/%packagename/plug-ins/switcher
%_libdir/%packagename/libcd-switcher.so

#---------------------------------------------------------------------
%package -n %packagename-dbus
Summary: That package provides a Dbus plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-dbus
This plug-in lets extern pllication interact on the dock.
The communication between both sides is based on Dbus.

%files -n %packagename-dbus
%_datadir/%packagename/plug-ins/Dbus
%_libdir/%packagename/libcd-Dbus.so

#---------------------------------------------------------------------
%package -n %packagename-showdesktop
Summary: That package provides a showDesktop plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-showdesktop
This applet let you acces quickly to your desktop.

%files -n %packagename-showdesktop
%_datadir/%packagename/plug-ins/showDesktop
%_libdir/%packagename/libcd-showDesktop.so

#---------------------------------------------------------------------
%package -n %packagename-gnome-integration
Summary: That package provides a gnome-integration plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-gnome-integration
This applet provides functions for a better integration into GNOME.

%files -n %packagename-gnome-integration
%_datadir/%packagename/plug-ins/gnome-integration
%_libdir/%packagename/libcd_gnome-integration.so

#---------------------------------------------------------------------
%package -n %packagename-kde-integration
Summary: That package provides a kde-integration plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-kde-integration
This applet provides functions for a better integration into KDE.

%files -n %packagename-kde-integration
%_datadir/%packagename/plug-ins/kde-integration
%_libdir/%packagename/libcd_kde-integration.so

#---------------------------------------------------------------------
%package -n %packagename-xfce-integration
Summary: That package provides a xfce-integration plugins
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-xfce-integration
This applet provides functions for a better integration into XFCE.

%files -n %packagename-xfce-integration
%_datadir/%packagename/plug-ins/xfce-integration
%_libdir/%packagename/libcd_xfce-integration.so

#---------------------------------------------------------------------
%package -n %packagename-clipper
Summary: That package provides plugin "clipper"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-clipper
This applet keeps a trace of the clipboard and mouse selection, so that
you can recall them quickly. It's a clone of the well-know Klipper.

%files -n %packagename-clipper
%_datadir/%packagename/plug-ins/Clipper
%_libdir/%packagename/libcd-Clipper.so

#---------------------------------------------------------------------
%package -n %packagename-gmenu
Summary: That package provides plugin "gmenu"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-gmenu
The new and soon wonderful GMenu applet

%files -n %packagename-gmenu
%_datadir/%packagename/plug-ins/GMenu
%_libdir/%packagename/libcd-GMenu.so

#---------------------------------------------------------------------
%package -n %packagename-keyboard-indicator
Summary: That package provides plugin "keyboard-indicator"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-keyboard-indicator
This applet lets you control the keyboard layout.

%files -n %packagename-keyboard-indicator
%_datadir/%packagename/plug-ins/keyboard-indicator
%_libdir/%packagename/libcd-keyboard-indicator.so

#---------------------------------------------------------------------
%package -n %packagename-weblets
Summary: That package provides plugin "weblets"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-weblets
The weblets applet allows you to show an interactive web page on your desktop.

%files -n %packagename-weblets
%_datadir/%packagename/plug-ins/weblets
%_libdir/%packagename/libcd-weblets.so

#---------------------------------------------------------------------

%package -n %packagename-network-monitor
Summary: That package provides plugin "Network-Monitor"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-network-monitor
This applet shows you a monitor of your active connections.

%files -n %packagename-network-monitor
%_datadir/%packagename/plug-ins/Network-Monitor
%_libdir/%packagename/libcd-network-monitor.so

#---------------------------------------------------------------------

%package -n %packagename-system-monitor
Summary: That package provides plugin "System-monitor"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-system-monitor
This applet shows you the CPU load, RAM usage, graphic card temperature, etc.

%files -n %packagename-system-monitor
%_datadir/%packagename/plug-ins/System-monitor
%_libdir/%packagename/libcd-system-monitor.so

#---------------------------------------------------------------------

%package -n %packagename-mail
Summary: That package provides plugin "mail"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-mail
This applet is very useful to warn you when you get new e-mails.
It can check in any kind of mailbox (yahoo, gmail, etc).

%files -n %packagename-mail
%_datadir/%packagename/plug-ins/mail
%_libdir/%packagename/libcd-mail.so

#---------------------------------------------------------------------

%package -n %packagename-dnd2share
Summary: That package provides plugin "dnd2share"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common
Requires: curl wget

%description -n %packagename-dnd2share
This applet lets you share files easily :
Drag-and-drop a file on the icon to upload it to one of the available hosting sites.
It supports many sites, like DropBox, Imageshack, pastebin, etc
You can upload text, image, video, and files.

%files -n %packagename-dnd2share
%_datadir/%packagename/plug-ins/dnd2share
%_libdir/%packagename/libcd-dnd2share.so

#---------------------------------------------------------------------

%package -n %packagename-rssreader
Summary: That package provides plugin "RSSreader"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-rssreader
This applet is an RSS/Atom feed reader

%files -n %packagename-rssreader
%_datadir/%packagename/plug-ins/RSSreader
%_libdir/%packagename/libcd-rssreader.so

#---------------------------------------------------------------------

%package -n %packagename-folders
Summary: That package provides plugin "Folders"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-folders
This applet imports folders inside the Dock

%files -n %packagename-folders
%_datadir/%packagename/plug-ins/Folders
%_libdir/%packagename/libcd-Folders.so

#---------------------------------------------------------------------

%package -n %packagename-remote-control
Summary: That package provides plugin "Remote-Control"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-remote-control
This plug-in lets you control your dock from the keyboard or even a remote controller.

%files -n %packagename-remote-control
%_datadir/%packagename/plug-ins/Remote-Control
%_libdir/%packagename/libcd-Remote-Control.so


#---------------------------------------------------------------------

%package -n %packagename-doncky
Summary: That package provides plugin "Doncky"
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-common

%description -n %packagename-doncky
This applet allows you to write texts and monitor your system with a "text style desklet".

%files -n %packagename-doncky
%_datadir/%packagename/plug-ins/Doncky
%_libdir/%packagename/libcd-doncky.so

#---------------------------------------------------------------------

%prep
%setup -q -n %name-%version.%ver_micro

%build
# Need dbusmenu-* for extra plugins
%cmake \
	-Denable-disks=yes \
	-Denable-doncky=yes \
	-Denable-network-monitor=yes \
	-Denable-old-gnome-integration=no \
	-Denable-scooby-do=yes \

%make_build -C BUILD

%install
%make_install DESTDIR=%buildroot install -C BUILD

%find_lang %name

%changelog
* Thu Apr 12 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.0-alt0.0rc1.1
- removed:
  - compiz-icon
  - showdesklets
- added
  + Composite-Manager
  + disks
  + Impulse
  + Recent-Events
  + scooby-do

* Thu May 05 2011 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2.1
- 2.3.0~2

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt4.2
- realy rebuild with new libwebkitgtk

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt4.1
- rebuild with new libwebkitgtk

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt4
- 2.2.0-4
- add Folders, Remote-Control, Doncky plugins

* Sun Apr 11 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt8
- 2.1.3-8

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt7
- 2.1.3-7

* Fri Feb 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt1
- 2.1.3-1
- no more exist showdesklets
- add rssreader

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt4
- 2.1.2-4

* Thu Nov 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt2.2
- rebuild with libxklavier.so.15

* Sat Oct 31 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt2
- 2.1.1-2

* Mon Oct 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- initial build, mandriva spec based
