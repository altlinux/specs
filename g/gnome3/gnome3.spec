%define ver_major 3.2

Name: gnome3
Version: %ver_major.0
Release: alt1

Summary: GNOME 3 Desktop installers
License: %gpl3plus
Group: Graphical desktop/GNOME

BuildArch: noarch

BuildPreReq: rpm-build-licenses

# The following are required versions of those packages that
# do not follow GNOME version numbers.
## Core components
%define session_ver %ver_major.0
%define librarian_ver 0.8.0
## Applications
%define network_manager_ver 0.8.995
%define terminal_ver %ver_major
%define epiphany_ver %ver_major
%define pidgin_ver 2.6.3
%define metacity_ver 2.34
%define media_ver 2.91.2
%define evince_ver %ver_major
%define applets_ver 2.91.4
%define gedit_plugins_ver %ver_major
%define gnome_nettool_ver 3.0
%define gud_ver %ver_major
%define gdm_ver %ver_major
%define gdu_ver 3.0
## Engines, themes
%define engines_ver %ver_major
%define icon_theme_ver %ver_major
%define themes_ver %ver_major
%define gtk_theme_prefix gtk3-theme
%define wm_theme_prefix metacity-theme
%define gnome_theme_prefix gnome-theme
## a11y
%define orca_ver 2.32.1

%define default_gnome_theme		%gnome_theme_prefix-clearlooks >= %ver_major
%define default_gnome_theme_name		Glossy
%define default_wm_theme		%wm_theme_prefix-clearlooks
%define default_wm_theme_name		Clearlooks
# TODO: Create a gtk2-themes-default virtual package;
# libgtk-engines-default has little sense to an end user.
%define more_gtk2_themes		libgtk-engine-thinice, libgtk-engines-default, libgtk-engine-crux
%define more_wm_themes			%wm_theme_prefix-metabox %wm_theme_prefix-clearlooks

%description
A set of virtual packages for GNOME Desktop version 3 installation.

%package minimal
Summary: GNOME 3 Desktop minimal installer
Group: Graphical desktop/GNOME
Obsoletes: %name-sisyphus-minimal
Provides: %name-sisyphus-minimal = %version-%release

# GNOME Desktop Core
Requires: gnome-session >= %session_ver
Requires: gnome-panel >= %ver_major
Requires: gnome-control-center >= %ver_major
Requires: gnome-shell >= %ver_major
# Window manager
# Requires: gnome-wm (see altbug #15947)
Requires: metacity-gnome >= %metacity_ver

# Help browser
Requires: yelp >= %ver_major
#Requires: gnome-menus >= %ver_major

# GNOME Utilities
Requires: gnome-search-tool >= %ver_major
Requires: gnome-system-monitor >= %ver_major
Requires: gucharmap >= %ver_major
Requires: gcalctool >= %ver_major

# Applications
## Default file manager
Requires: nautilus >= %ver_major
## Default terminal emulator
Requires: gnome-terminal >= %terminal_ver
## Default archiving tool
Requires: file-roller >= %ver_major
## Default text editor
Requires: gedit >= %ver_major

# Look & Feel
## Default themes
Requires: gnome-icon-theme >= %ver_major
Requires: gnome-icon-theme-symbolic >= %ver_major
Requires: gnome-themes-standard >= %ver_major

## Screensaver
Requires: gnome-screensaver

# And, of course, the documentation
Requires: gnome-user-docs >= %gud_ver

%description minimal
This virtual package installs GNOME Desktop with minimum components. It
installs only a few applets, necessary utilities and a minimal set of themes.
Doesn't install games and media programs.

## =========================================================================

%package default
Summary: GNOME 2 Desktop installer for optimal user's requirements
Group: Graphical desktop/GNOME
Requires: %name-minimal = %version-%release

## Color manager
Requires: gnome-color-manager
## Password keeper
Requires: gnome-keyring
# Encryption keys management
Requires: seahorse
#Requires: seahorse-agent
## All gvfs-backends
Requires: gvfs-backends
Requires: fuse-gvfs
Requires: gnome-disk-utility >= %gdu_ver
## Display manager (gdm or gdm2.20)
Requires: gdm-gnome >= %ver_major
## Default web-browser (firefox or galeon?)
Requires: epiphany >=  %epiphany_ver
## Epiphany extensions
Requires: epiphany-extensions
## Default mailer
Requires: evolution >= %ver_major
## Default messenger
Requires: empathy >= %ver_major
## Default RSS-reader
#Requires: liferea
## Default document reader (currently pdf, ps, tiff, dvi)
Requires: evince >= %evince_ver
## and E-Book Reader
#Requires: fbreader

## Applets
Requires: gnome-applets >= %applets_ver

# Utilities
Requires: gnome-utils >= %ver_major
Requires: gconf-editor >= 3.0
Requires: dconf-editor >= 0.10

## Let's have nice notifications
Requires: notification-daemon

# Applications
## Plugins for gedit
Requires: gedit-plugins >= %gedit_plugins_ver
## Stock multimedia applications
Requires: gnome-media >= %media_ver
## Default music player
#Requires: rhythmbox
## Default media player
Requires: totem
## Stock GNOME games
Requires: gnome-games >= %ver_major
## Default image viewer
Requires: eog >= %ver_major
Requires: eog-plugins >= 2.91.90
## Default CD/DVD burning interface
Requires: brasero >= %ver_major
## Clipboard manager
Requires: parcellite
# A quick previewer for Nautilus
Requires: sushi
# Menu editor
#Requires: alacarte

# Look & Feel
## All default themes
Requires: metacity-themes-default >= %metacity_ver
#Requires: gnome-themes-default >= %ver_major

Requires: gnome-power-manager >= %ver_major
Requires: NetworkManager-gnome >= %network_manager_ver
## Bluetooth pairing and control applet
Requires: gnome-bluetooth
## frontend for various networking tools
Requires: gnome-nettool >= %gnome_nettool_ver
# user settings utility
Requires: gnome-tweak-tool >= %ver_major

%description default
This virtual package installs GNOME Desktop for an average user's
requirements. It installs components from gnome-minimal package, some
games, media programs such as mixer, audio and video players, additional
themes, and some other programs that comprise GNOME Desktop.
## =========================================================================

%package default-ru
Summary: GNOME 3 Desktop installer for optimal user's requirements, russian part
Group: Graphical desktop/GNOME
## spell checking dictionary
Requires: hunspell-ru

%description default-ru
This virtual package installs spell checking dictionary for russian language

## =========================================================================

%package full
Summary: GNOME 3 Desktop full installer
Group: Graphical desktop/GNOME
Requires: %name-default = %version-%release

# Sound & graphics & video
## All Rhythmbox plugins
#Requires: rhythmbox-plugins
## module player
#Requires: modplugplay
## Applications for taking pictures
## and videos from a webcam
#Requires: cheese
# GTK UVC video viewer
#Requires: guvcview
## FM-tuner
#Requires: gnomeradio
## CD-ripper
#Requires: grip
## Image viewer, browser and simple editor
Requires: gthumb
## Non-linear DV editor
Requires: kino
#Requires: dvgrab
## SANE (Scanner Access Now Easy) frontend
Requires: xsane

# Networking
## Utilities
## VNC server for the GNOME Desktop
Requires: vino
## VNC client for the GNOME Desktop
Requires: vinagre
## Internet telephon
Requires: ekiga
## Client for ed2k network
Requires: aMule

# Windows (TM) communications
## RDP
Requires: rdesktop
## NX
Requires: freenx
# Requires: nxlaunch

# Disks management
Requires: gparted
Requires: consolehelper

# Look & Feel
## 3D screensavers
#Requires: gnome-screensaver-modules-xscreensaver-gl

%description full
This virtual package installs full GNOME Desktop except components from
gnome-mobile and gnome-a11y packages.

## =========================================================================
%package office
Summary: GNOME 3 Desktop applications for real office users
Group: Graphical desktop/GNOME

## OpenOffice.org and GNOME extensions for it
### Some openoffice.org-langpack-* packages need to be added to distribution profiles
Requires: openoffice.org-gnome
## Diagram creation program
Requires: dia
## International dictionary (synchronize this section in -office package)
# GUI
Requires: stardict-gnome
# Some language independent StarDict dictionaries
Requires: stardict-engcom

%description office
This virtual package installs OpenOffice.org office suite with GNOME extensions and
some applicatios necessary for every office user.

## =========================================================================

%package office-ru
Summary: russian stardict dictionaries for gnome-office(-light) packages
Group: Graphical desktop/GNOME
Requires: stardict-mueller7
Requires: stardict-slovnyk_en-ru
Requires: stardict-slovnyk_ru-en

%description office-ru
This virtual package installs stardict dictionaries for russian language

## =========================================================================
%package office-light
Summary: GNOME 3 Desktop applications for real office users (light version)
Group: Graphical desktop/GNOME

## Word processor
Requires: abiword
## Spreadsheet program
Requires: gnumeric
## Vector Drawing Application
Requires: inkscape
## Diagram creation program
Requires: dia
## International dictionary (synchronize this section in -office package)
# GUI
Requires: stardict-gnome
# Some StarDict dictionaries
Requires: stardict-engcom

## Presentation tool ???

%description office-light
This virtual package installs applications necessary for every office
users such as word processor (Abiword), spreadsheet editor (Gnumeric) and
some other usefull programs

## =========================================================================
%package a11y
Summary: GNOME 3 Desktop accessibility applications
Group: Graphical desktop/GNOME
# A synonym
Provides: sisyphus-accessibility
Obsoletes: %name-sisyphus-accessibility 
Provides: %name-sisyphus-accessibility = %version-%release
Requires: gnome-minimal = %version-%release

Requires: gok >= %ver_major
Requires: gnome-mag
Requires: dasher
Requires: gnome-themes-accessibility
Requires: orca >= %orca_ver

%description a11y
This virtual package installs GNOME Desktop accessibility applications.
These include an on-screen keyboard, a screen reader, Dasher - an
innovative graphical input tool, and Magnifier (the name says for
itself).

%files minimal
%files default
#%files default-ru
#%files full
#%files office
#%files office-ru
#%files office-light
#%files a11y

%changelog
* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- added gnome-color-manager, sushi in -default

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- removed seahorse-agent

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- removed gnome-menus, alacarte

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for people/gnome
