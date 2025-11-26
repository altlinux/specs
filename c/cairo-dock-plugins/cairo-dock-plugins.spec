#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define packagename cairo-dock
%define sover 1

Name: %packagename-plugins
Version: 3.6.0
Release: alt1

Summary: Plugins for cairo-dock
Summary(ru_RU.UTF-8): Плагины для cairo-dock

License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later
Group: Graphical desktop/Other

URL: https://github.com/Cairo-Dock/cairo-dock-plug-ins
VCS: https://github.com/Cairo-Dock/cairo-dock-plug-ins

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: cairo-dock-devel = %version
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(ayatana-indicator3-0.4)
BuildRequires: pkgconfig(libayatana-ido3-0.4)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(libgnome-menu-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(libetpan)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: libsensors3-devel

Requires: %packagename-common = %EVR
Requires: %packagename-animated-icons = %EVR
Requires: %packagename-cairo-penguin = %EVR
Requires: %packagename-clipper = %EVR
Requires: %packagename-composite-manager = %EVR
Requires: %packagename-dbus = %EVR
Requires: %packagename-disks = %EVR
Requires: %packagename-folders = %EVR
Requires: %packagename-impulse = %EVR
Requires: %packagename-network-monitor = %EVR
Requires: %packagename-rssreader = %EVR
Requires: %packagename-recent-events = %EVR
Requires: %packagename-remote-control = %EVR
Requires: %packagename-screenshot = %EVR
Requires: %packagename-sound-effects = %EVR
Requires: %packagename-system-monitor = %EVR
Requires: %packagename-toons = %EVR
Requires: %packagename-xgamma = %EVR
Requires: %packagename-alsamixer = %EVR
Requires: %packagename-clock = %EVR
Requires: %packagename-dnd2share = %EVR
Requires: %packagename-drop-indicator = %EVR
Requires: %packagename-dustbin = %EVR
Requires: %packagename-icon-effect = %EVR
Requires: %packagename-illusion = %EVR
Requires: %packagename-keyboard-indicator = %EVR
Requires: %packagename-logout = %EVR
Requires: %packagename-mail = %EVR
Requires: %packagename-motion-blur = %EVR
Requires: %packagename-musicplayer = %EVR
Requires: %packagename-netspeed = %EVR
Requires: %packagename-powermanager = %EVR
Requires: %packagename-quick-browser = %EVR
Requires: %packagename-shortcuts = %EVR
Requires: %packagename-show-mouse = %EVR
Requires: %packagename-showdesktop = %EVR
Requires: %packagename-slider = %EVR
Requires: %packagename-stack = %EVR
Requires: %packagename-switcher = %EVR
Requires: %packagename-systray = %EVR
Requires: %packagename-terminal = %EVR
Requires: %packagename-tomboy = %EVR
Requires: %packagename-weather = %EVR
Requires: %packagename-weblets = %EVR
Requires: %packagename-wifi = %EVR
Requires: %packagename-gmenu = %EVR
Requires: %packagename-indicator-generic = %EVR
Requires: %packagename-messaging-menu = %EVR
Requires: %packagename-status-notifier = %EVR
Requires: %packagename-global-menu = %EVR
Requires: %packagename-doncky = %EVR

%description
This package contains various plugins for cairo-dock.

%description -l ru_RU.UTF-8
Данный пакет содержит различные плагины для cairo-dock.

%files
#---------------------------------------------------------------------
%package -n %packagename-common
Summary: That common package provides lang files
Group: Graphical desktop/Other
Requires: %packagename = %version
Requires: %packagename-desklet-rendering = %EVR
Requires: %packagename-dialog-rendering = %EVR
Requires: %packagename-rendering = %EVR

%description -n %packagename-common
That common package provides lang files.

%files -n %packagename-common -f %name.lang
%_datadir/%packagename/plug-ins/shared-files
%_datadir/%packagename/gauges/*

#---------------------------------------------------------------------
%package -n libCDApplet%sover
Summary: Library for libCDApplet-devel
Group: System/Libraries
Requires: vala

%description -n libCDApplet%sover
This package is a library for Cairo-Dock.

%files -n libCDApplet%sover
%_libdir/libCDApplet.so.%sover
%_libdir/libCDApplet.so.%sover.*

#---------------------------------------------------------------------
%package -n libCDApplet-devel
Summary: Development files for Vala binding for Cairo-Dock
Group: Development/Other
Requires: libCDApplet%sover = %EVR

Obsoletes: %packagename-vala < %version
Obsoletes: %packagename-vala-devel < %version

%description -n libCDApplet-devel
This package contains development files for Vala binding for Cairo-Dock.

%files -n libCDApplet-devel
%_datadir/vala/vapi/CDApplet.*
%_libdir/libCDApplet.so
%_pkgconfigdir/*.pc

#---------------------------------------------------------------------
%package -n %packagename-animated-icons
Summary: That package provides plugin "Animated icons"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-animated-icons
This plug-in provides many different animations for your icons.

%files -n %packagename-animated-icons
%_datadir/%packagename/plug-ins/Animated-icons
%_libdir/%packagename/libcd-Animated-icons.so

#---------------------------------------------------------------------
%package -n %packagename-cairo-penguin
Summary: That package provides plugin "Cairo Penguin"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-cairo-penguin
This plug-in adds a lively Penguin in your dock. Tux images are taken
from Pingus.

%files -n %packagename-cairo-penguin
%_datadir/%packagename/plug-ins/Cairo-Penguin
%_libdir/%packagename/libcd-Cairo-Penguin.so

#---------------------------------------------------------------------
%package -n %packagename-clipper
Summary: That package provides plugin "Clipper"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-clipper
This plug-in keeps a trace of the clipboard and mouse selection,
so that you can recall them quickly. It's a clone of the well-know Klipper.
This supports clipboard and mouse selection, predefined actions,
and persistent items.

%files -n %packagename-clipper
%_datadir/%packagename/plug-ins/Clipper
%_libdir/%packagename/libcd-Clipper.so

#---------------------------------------------------------------------
%package -n %packagename-composite-manager
Summary: That package provides plugin "Composite-Manager"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-composite-manager
This applet allows you to toggle the composite ON/OFF.
The composite is what allows transparency on the desktop, but it can slow down
your PC, especially during games.
The applet also lets you acces to some actions of the Window-Manager.

%files -n %packagename-composite-manager
%_datadir/%packagename/plug-ins/Composite-Manager
%_libdir/%packagename/libcd-Composite-Manager.so

#---------------------------------------------------------------------
%package -n %packagename-dbus
Summary: That package provides plugin "Dbus"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-dbus
This plug-in lets extern pllication interact on the dock.
The communication between both sides is based on Dbus.
Note: the DBus plugin is also required for external applets
(those from the extra plugins repository and also for running
Cairo-Dock as a systemd service).

%files -n %packagename-dbus
%_datadir/%packagename/plug-ins/Dbus
%_libdir/%packagename/libcd-Dbus.so

#---------------------------------------------------------------------
%package -n %packagename-disks
Summary: That package provides plugin "Disks"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-disks
Monitors disks speed and space.
This applet show your disks informations. You can activate both options at
once, but they're better separated in 2 or more instances of the applet.

%files -n %packagename-disks
%_datadir/%packagename/plug-ins/Disks
%_libdir/%packagename/libcd-disks.so

#---------------------------------------------------------------------
%package -n %packagename-folders
Summary: That package provides plugin "Folders"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-folders
This applet imports folders inside the Dock.
You can run multiple copies of this applet, each for a separate directory.

%files -n %packagename-folders
%_datadir/%packagename/plug-ins/Folders
%_libdir/%packagename/libcd-Folders.so

#---------------------------------------------------------------------
%package -n %packagename-impulse
Summary: That package provides plugin "Impulse"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-impulse
Did you know that your dock can dance? :)
If you click on this icon, the dock will dance!
In fact, you will have a graphical equalizer into the dock
It will analyse the signal given by PulseAudio.

%files -n %packagename-impulse
%_datadir/%packagename/plug-ins/Impulse
%_libdir/%packagename/libcd-Impulse.so

#---------------------------------------------------------------------
%package -n %packagename-network-monitor
Summary: That package provides plugin "Network-Monitor"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-network-monitor
This applet shows you a monitor of your active connections.

%files -n %packagename-network-monitor
%_datadir/%packagename/plug-ins/Network-Monitor
%_libdir/%packagename/libcd-network-monitor.so

#---------------------------------------------------------------------
%package -n %packagename-rssreader
Summary: That package provides plugin "RSSreader"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-rssreader
This applet is an RSS/Atom feed reader.

%files -n %packagename-rssreader
%_datadir/%packagename/plug-ins/RSSreader
%_libdir/%packagename/libcd-rssreader.so

#---------------------------------------------------------------------
%package -n %packagename-recent-events
Summary: That package provides plugin "Recent-Events"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-recent-events
This applet lists your recent actions (opened/created files, launched programs,
etc).
It also adds the list of recent actions in the menu of launchers that can
handle them
It handles Evolution, Pidgin, Empathy, etc.
It requires 'Zeitgeist' to be running.

%files -n %packagename-recent-events
%_datadir/%packagename/plug-ins/Recent-Events
%_libdir/%packagename/libcd-Recent-Events.so

#---------------------------------------------------------------------
%package -n %packagename-remote-control
Summary: That package provides plugin "Remote-Control"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-remote-control
This plug-in lets you control your dock from
the keyboard or even a remote controller.

%files -n %packagename-remote-control
%_datadir/%packagename/plug-ins/Remote-Control
%_libdir/%packagename/libcd-Remote-Control.so

#---------------------------------------------------------------------
%package -n %packagename-screenshot
Summary: That package provides plugin "Screenshot"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-screenshot
This applet allows you to create screenshots of your screen.

%files -n %packagename-screenshot
%_datadir/%packagename/plug-ins/Screenshot
%_libdir/%packagename/libcd-Screenshot.so

#---------------------------------------------------------------------
%package -n %packagename-sound-effects
Summary: That package provides plugin "Sound-Effects"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-sound-effects
This applet allows you to adjust sound notifications.
This plug-in add sound effects on various events in the dock:
when clicking an icon, when hovering an icon, etc.

%files -n %packagename-sound-effects
%_datadir/%packagename/plug-ins/Sound-Effects
%_libdir/%packagename/libcd-Sound-Effects.so

#---------------------------------------------------------------------
%package -n %packagename-system-monitor
Summary: That package provides plugin "System-monitor"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-system-monitor
This applet shows you the CPU load, RAM usage, graphic card temperature, etc.

%files -n %packagename-system-monitor
%_datadir/%packagename/plug-ins/System-monitor
%_libdir/%packagename/libcd-system-monitor.so

#---------------------------------------------------------------------
%package -n %packagename-toons
Summary: That package provides plugin "toons"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-toons
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %packagename-toons
%_datadir/%packagename/plug-ins/Toons
%_libdir/%packagename/libcd-Toons.so

#---------------------------------------------------------------------
%package -n %packagename-xgamma
Summary: That package provides plugin "Xgamma"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-xgamma
Setup the gama of your screen directly from the dock.
It is a simple port of xgamma. Quickly setup gamma with
left click, or more accurately with middle click.

%files -n %packagename-xgamma
%_datadir/%packagename/plug-ins/Xgamma
%_libdir/%packagename/libcd-Xgamma.so

#---------------------------------------------------------------------
%package -n %packagename-alsamixer
Summary: That package provides plugin "Alsa Mixer"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

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
%package -n %packagename-clock
Summary: That package provides plugin "Clock"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

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
%package -n %packagename-desklet-rendering
Summary: That package provides plugin "desklet-rendering"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-desklet-rendering
This module provides different views for your desklets.

%files -n %packagename-desklet-rendering
%_datadir/%packagename/plug-ins/desklet-rendering
%_libdir/%packagename/libcd-desklet-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-dialog-rendering
Summary: That package provides plugin "dialog-rendering"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-dialog-rendering
This plug-in provides some dialog decorators for dialog bubbles.

%files -n %packagename-dialog-rendering
%_datadir/%packagename/plug-ins/dialog-rendering
%_libdir/%packagename/libcd-dialog-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-dnd2share
Summary: That package provides plugin "dnd2share"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR
Requires: wget

%description -n %packagename-dnd2share
This applet lets you share files easily:
Drag-and-drop a file on the icon to upload it to one of the available
hosting sites. It supports many sites, like DropBox, Imageshack, pastebin, etc
You can upload text, image, video, and files.

%files -n %packagename-dnd2share
%_datadir/%packagename/plug-ins/dnd2share
%_libdir/%packagename/libcd-dnd2share.so

#---------------------------------------------------------------------
%package -n %packagename-rendering
Summary: That package provides plugin "dock rendering"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-rendering
This module adds different views to your dock.
Any dock or sub-dock can be displayed with the
view of your choice. Currently, 3D-plane, Caroussel,
Paraboer.
%files -n %packagename-rendering
%_datadir/%packagename/plug-ins/rendering
%_libdir/%packagename/libcd-rendering.so

#---------------------------------------------------------------------
%package -n %packagename-drop-indicator
Summary: That package provides plugin "drop-indicator"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR
Provides: %packagename-drop_indicator = %EVR
Obsoletes: %packagename-drop_indicator < %version

%description -n %packagename-drop-indicator
This plug-in displays an animated indicator when you drop something in the dock.

%files -n %packagename-drop-indicator
%_datadir/%packagename/plug-ins/drop-indicator
%_libdir/%packagename/libcd-drop_indicator.so

#---------------------------------------------------------------------
%package -n %packagename-dustbin
Summary: That package provides plugin "dustbin"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

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
%package -n %packagename-gnome-integration
Summary: That package provides plugin "gnome-integration"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-gnome-integration
This applet provides functions for a better integration into GNOME.

%files -n %packagename-gnome-integration
%_datadir/%packagename/plug-ins/gnome-integration
%_libdir/%packagename/libcd_gnome-integration.so

#---------------------------------------------------------------------
%package -n %packagename-icon-effect
Summary: That package provides plugin "icon-effect"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-icon-effect
This plug-in adds many special effects to your icons.

%files -n %packagename-icon-effect
%_datadir/%packagename/plug-ins/icon-effect
%_libdir/%packagename/libcd-icon-effect.so

#---------------------------------------------------------------------
%package -n %packagename-illusion
Summary: That package provides plugin "illusion"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-illusion
This plug-in provides animations for appearance & disappearance of icons.

%files -n %packagename-illusion
%_datadir/%packagename/plug-ins/illusion
%_libdir/%packagename/libcd-illusion.so

#---------------------------------------------------------------------
%package -n %packagename-kde-integration
Summary: That package provides plugin "kde-integration"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-kde-integration
This applet provides functions for a better integration into KDE.

%files -n %packagename-kde-integration
%_datadir/%packagename/plug-ins/kde-integration
%_libdir/%packagename/libcd_kde-integration.so

#---------------------------------------------------------------------
%package -n %packagename-xfce-integration 
Summary: That package provides plugin "xfce-integration"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-xfce-integration
This applet provides functions for a better integration into XFCE.

%files -n %packagename-xfce-integration
%_datadir/%packagename/plug-ins/xfce-integration
%_libdir/%packagename/libcd_xfce-integration.so

#---------------------------------------------------------------------
%package -n %packagename-keyboard-indicator
Summary: That package provides plugin "keyboard-indicator"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-keyboard-indicator
This applet lets you control the keyboard layout.

%files -n %packagename-keyboard-indicator
%_datadir/%packagename/plug-ins/keyboard-indicator
%_libdir/%packagename/libcd-keyboard-indicator.so

#---------------------------------------------------------------------
%package -n %packagename-logout
Summary: That package provides plugin "logout"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-logout
A very simple applet that adds an icon to log out
from your session.

%files -n %packagename-logout
%_datadir/%packagename/plug-ins/logout
%_libdir/%packagename/libcd-logout.so

#---------------------------------------------------------------------
%package -n %packagename-mail 
Summary: That package provides plugin "mail"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-mail
This applet is very useful to warn you when you get new e-mails.
It can check in any kind of mailbox (yahoo, gmail, etc).

%files -n %packagename-mail
%_datadir/%packagename/plug-ins/mail
%_libdir/%packagename/libcd-mail.so

#---------------------------------------------------------------------
%package -n %packagename-motion-blur
Summary: That package provides plugin "motion-blur"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-motion-blur
This plug-in adds a motion blur effect on docks.

%files -n %packagename-motion-blur
%_datadir/%packagename/plug-ins/motion-blur
%_libdir/%packagename/libcd-motion_blur.so

#---------------------------------------------------------------------
%package -n %packagename-musicplayer 
Summary: That package provides plugin "musicPlayer"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-musicplayer
This applet lets you control any music player.
First choose the player you want to control.
click to show/hide the player or pause,
middle-click to pause or go to next song,
Scroll up/down to change the song or control the volume.

%files -n %packagename-musicplayer
%_datadir/%packagename/plug-ins/musicPlayer
%_libdir/%packagename/libcd-musicPlayer.so

#---------------------------------------------------------------------
%package -n %packagename-netspeed
Summary: That package provides plugin "netspeed" 
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-netspeed
The netspeed applet show you the bit rate of your internet connection
and make some stats on it.

%files -n %packagename-netspeed
%_datadir/%packagename/plug-ins/netspeed
%_libdir/%packagename/libcd-netspeed.so

#---------------------------------------------------------------------
%package -n %packagename-powermanager 
Summary: That package provides plugin "powermanager"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-powermanager
A power manager for laptop's battery
It works with ACPI and DBus.

%files -n %packagename-powermanager
%_datadir/%packagename/plug-ins/powermanager
%_libdir/%packagename/libcd-powermanager.so

#---------------------------------------------------------------------
%package -n %packagename-quick-browser
Summary: That package provides plugin "quick-browser"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

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
%package -n %packagename-shortcuts 
Summary: That package provides plugin "shortcuts"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-shortcuts
An applets thatlet you acces quickly to all of your shortcuts.
It can manage disks, network points, and Nautilus bookmarks.
You can add or remove bookmarks bye drag'n'drop, even if you
don't have Nautilus. Middle-click to acces your desktop easily.

%files -n %packagename-shortcuts
%_datadir/%packagename/plug-ins/shortcuts
%_libdir/%packagename/libcd-shortcuts.so 

#---------------------------------------------------------------------
%package -n %packagename-show-mouse
Summary: That package provides plugin "show-mouse"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR
Provides: %packagename-show_mouse = %EVR
Obsoletes: %packagename-show_mouse < %version

%description -n %packagename-show-mouse
This plug-in draw some animation around the cursor when it's inside a dock
desklet.

%files -n %packagename-show-mouse
%_datadir/%packagename/plug-ins/show_mouse
%_libdir/%packagename/libcd-show_mouse.so

#---------------------------------------------------------------------
%package -n %packagename-showdesktop  
Summary: That package provides plugin "showDesktop"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-showdesktop
This applet let you acces quickly to your desktop.

%files -n %packagename-showdesktop
%_datadir/%packagename/plug-ins/showDesktop
%_libdir/%packagename/libcd-showDesktop.so

#---------------------------------------------------------------------
%package -n %packagename-slider   
Summary: That package provides plugin "slider"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-slider
The slider applet is a basic image slider.

%files -n %packagename-slider
%_datadir/%packagename/plug-ins/slider
%_libdir/%packagename/libcd-slider.so

#---------------------------------------------------------------------
%package -n %packagename-stack  
Summary: That package provides plugin "stack"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-stack
This applet allows you to build a stack of items, just like the Stack
applet of MacOS X. Items can be files, folders, URL, or even pieces of
text.

%files -n %packagename-stack
%_datadir/%packagename/plug-ins/stack
%_libdir/%packagename/libcd-stack.so

#---------------------------------------------------------------------
%package -n %packagename-switcher  
Summary: That package provides plugin "switcher"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-switcher
This applet allows you to interact with desktops: switch between them,
set a name, quickly add/remove them, etc.

%files -n %packagename-switcher
%_datadir/%packagename/plug-ins/switcher
%_libdir/%packagename/libcd-switcher.so

#---------------------------------------------------------------------
%package -n %packagename-systray   
Summary: That package provides plugin "systray"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-systray
This is a legacy version of the notification area on the panel.

%files -n %packagename-systray
%_datadir/%packagename/plug-ins/systray
%_libdir/%packagename/libcd-systray.so

#---------------------------------------------------------------------
%package -n %packagename-terminal  
Summary: That package provides plugin "terminal"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-terminal
Add a terminal to your dock!
You can drag'n'drop files or text into it and select an action.

%files -n %packagename-terminal
%_datadir/%packagename/plug-ins/terminal
%_libdir/%packagename/libcd-terminal.so

#---------------------------------------------------------------------
%package -n %packagename-tomboy   
Summary: That package provides plugin "tomboy"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-tomboy
Control your Gnote or TomBoy's notes directly in the dock!

%files -n %packagename-tomboy
%_datadir/%packagename/plug-ins/tomboy
%_libdir/%packagename/libcd-tomboy.so

#---------------------------------------------------------------------
%package -n %packagename-weather  
Summary: That package provides plugin "weather"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-weather
This applet displyas weather into your dock.
It can detach itself to be a ttally eye-candy 3D Desklet.
You can have many valuable info by (middle) clicking on
the icons. Data are provided by www.weather.com

%files -n %packagename-weather
%_datadir/%packagename/plug-ins/weather
%_libdir/%packagename/libcd-weather.so

#---------------------------------------------------------------------
%package -n %packagename-weblets 
Summary: That package provides plugin "weblets"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-weblets
This applet allows you to use interactive web pages on your desktop.

%files -n %packagename-weblets
%_datadir/%packagename/plug-ins/weblets
%_libdir/%packagename/libcd-weblets.so

#---------------------------------------------------------------------
%package -n %packagename-wifi
Summary: That package provides plugin "wifi"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-wifi 
The wifi applet show you the signal strenght of
the first active connection.

%files -n %packagename-wifi
%_datadir/%packagename/plug-ins/wifi
%_libdir/%packagename/libcd-wifi.so

#---------------------------------------------------------------------
%package -n %packagename-gmenu   
Summary: That package provides plugin "GMenu"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-gmenu 
This plug-in displays a menu with frequently used applications and files.

%files -n %packagename-gmenu
%_datadir/%packagename/plug-ins/GMenu
%_libdir/%packagename/libcd-GMenu.so

#---------------------------------------------------------------------
%package -n %packagename-indicator-generic   
Summary: That package provides plugin "Indicator Generic"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-indicator-generic
This plug-in can display all the available Indicators into your dock.
Indicators provide information about something, and a menu to act on it:
for instance, an indicator to control the printer jobs. Idle Indicators
are automatically hidden.

%files -n %packagename-indicator-generic
%_datadir/%packagename/plug-ins/Indicator-Generic
%_libdir/%packagename/libcd-Indicator-Generic.so 

#---------------------------------------------------------------------
%package -n %packagename-messaging-menu  
Summary: That package provides plugin "Messaging-Menu"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-messaging-menu 
This applet allows you to adjust messaging menu.
It handles Evolution, Pidgin, Empathy, etc.
It requires the Messaging service.

%files -n %packagename-messaging-menu
%_datadir/%packagename/plug-ins/Messaging-Menu
%_libdir/%packagename/libcd-Messaging-Menu.so

#---------------------------------------------------------------------
%package -n %packagename-status-notifier 
Summary: That package provides plugin "Status-Notifier"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-status-notifier 
This applet allows you to adjust status notifier.

%files -n %packagename-status-notifier
%_datadir/%packagename/plug-ins/Status-Notifier
%_libdir/%packagename/libcd-status-notifier.so
%_libdir/%packagename/status-notifier-watcher

#---------------------------------------------------------------------
%package -n %packagename-global-menu   
Summary: That package provides plugin "Global-Menu"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-global-menu 
This plugin allows you to manage the currently active window: closing,
minimizing, maximizing and displaying the application menu.

%files -n %packagename-global-menu
%_datadir/%packagename/plug-ins/Global-Menu
%_libdir/%packagename/libcd-Global-Menu.so
%_libdir/%packagename/appmenu-registrar

#---------------------------------------------------------------------
%package -n %packagename-doncky    
Summary: That package provides plugin "Doncky"
Group: Graphical desktop/Other
Requires: %packagename-common = %EVR

%description -n %packagename-doncky 
This applet allows you to write texts and monitor your system with
a "text style desklet".

%files -n %packagename-doncky
%_datadir/%packagename/plug-ins/Doncky
%_libdir/%packagename/libcd-doncky.so

#---------------------------------------------------------------------


%prep
%setup -n %name-%version
%patch -p1

%build
%cmake \
	-Denable-disks=yes \
	-Denable-network-monitor=yes \
	-Denable-weblets=yes \
	-Denable-global-menu=yes \
	-Denable-doncky=yes

%cmake_build

%install
%cmake_install
%find_lang %name
rm -f  %buildroot%_libdir/%packagename/%packagename-launcher-API-daemon

%changelog
* Mon Nov 24 2025 Polina Poidenko <polipoki@altlinux.org> 3.6.0-alt1
- New version 3.6.0.
- Update build dependencies.
- Separate subpackage libCDApplet1 in accordance with Shared Libs Policy.
- Remove old patches.
- lock-screen.sh: Remove redundant conditions.
- netspeed: Change /tmp on $TMPDIR.
- Added:
   + weblets
   + GMenu
   + Messaging-Menu
   + Status-Notifier
   + Global-Menu
   + Recent-Events
   + Indicator-Generic
- Removed:
   + Scooby-Do

* Sun Jun 06 2021 Arseny Maslennikov <arseny@altlinux.org> 3.4.1-alt16
- Fix FTBFS.

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt15
- Fix compilation with gcc10 -fno-common

* Sun Nov 24 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt14.2
- Fix typo in changelog

* Sun Nov 24 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt14.1
- Fix typo in description -l ru_RU.UTF-8 (Closes: 37535)

* Fri Nov 22 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt14
- Build without python
- Removed:
    - Global-Menu
    - GMenu
    - Status-Notifier
    - launcher-API-daemon
    - Recent-Events
    - Indicator-Generic

* Fri Jan 11 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt13
- Rebuild with libical-devel

* Wed Jan 09 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt12
- Rebuild without libwebkitgtk3
- remove plugin weblets

* Thu Sep 20 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt11
- drop ubt
- disable build python2 bindings

* Fri Feb 16 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.1-alt10.S1
- avoid nvidia-settings dependency on non-x86 arches

* Fri Jan 26 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt9.S1
- Update buildrequires

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt8
- Rebuilt without mono-mcs.

* Sun Jul 02 2017 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt7
- Workaround for time.h related conflict with 2.25 glibc
- Pull in upstream patch to update URL on weather plugin
- Default to xdg-screensaver for lock_screen.

* Thu Jun 16 2016 Mikhail Efremov <sem@altlinux.org> 3.4.1-alt6
- Rebuild with libetpan-1.7.2.

* Mon May 02 2016 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt5
- Fix Requires.

* Fri Mar 18 2016 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt4
- Added missing buildrequires
- Added plugin:
    + Global-Menu
    + GMenu
    + Indicator-Generic
    + Messaging-Menu
    + Recent-Events
    + Status-Notifier
    + launcher-API-daemon
Added:
    + support zeitgeist-2.0
    + bindings python3
    

* Mon Jan 25 2016 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt3
- Rebuild with libicall-2.0.0.

* Wed Sep 16 2015 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt2
- Small fix in spec
- Add netspeed.patch

* Wed Sep 09 2015 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- New version 3.4.1
- removed:
    - Gmenu
    - Recent-Events
- added:
  + Screenshot
  + Sound-Effects
  + cairo-dock-vala
  + cairo-dock-vala-devel
  + python-module-cairo-dock

* Sat Aug 23 2014 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt1.M70P.1
- Rebuild with libetpan-1.5.

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version 3.1.0

* Thu Jun 28 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.0.2-alt1
- new version
- fixed %packagename-common deps

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
