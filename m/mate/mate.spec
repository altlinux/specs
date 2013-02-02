%define ver_major 1.4

Name: mate
Version: %ver_major.0
Release: alt2

Summary: MATE Desktop installers
License: %gpl2plus
Group: Graphical desktop/MATE

BuildArch: noarch

BuildPreReq: rpm-build-licenses

# The following are required versions of those packages that
# do not follow MATE version numbers.
## Core components
%define session_ver %ver_major.0
%define librarian_ver 0.8.0
## Applications
%define network_manager_ver 0.8.995
%define terminal_ver %ver_major
%define epiphany_ver %ver_major
%define pidgin_ver 2.6.3
%define evince_ver %ver_major
%define gud_ver %ver_major
%define gdm_ver %ver_major
%define gdu_ver 3.0
## Engines, themes
%define engines_ver %ver_major
%define icon_theme_ver %ver_major
%define themes_ver %ver_major
%define gtk_theme_prefix gtk-theme
%define mate_theme_prefix mate-theme
## a11y
%define orca_ver 2.32.1

# TODO: Create a gtk2-themes-default virtual package;
# libgtk-engines-default has little sense to an end user.
%define more_gtk2_themes		libgtk-engine-thinice, libgtk-engines-default, libgtk-engine-crux

%description
A set of virtual packages for MATE Desktop version 3 installation.

%package minimal
Summary: MATE Desktop minimal installer
Group: Graphical desktop/MATE
Provides: %name-core = %version-%release

# expired: should be dropped and replaced w/gio and shared-mime-info
Requires: mate-mime-data

# components
Requires: mate-corba
Requires: mate-vfs
Requires: mate-dialogs
Requires: mate-polkit
Requires: mate-settings-daemon
Requires: python-corba
Requires: python-mate

# MATE Desktop Core
Requires: mate-session >= %session_ver
Requires: mate-panel >= %ver_major
Requires: mate-control-center >= %ver_major
Requires: mate-desktop >= %ver_major
# Window manager
# Requires: mate-wm (see altbug #15947)
Requires: mate-window-manager

# Help browser
Requires: yelp >= %ver_major
Requires: mate-menus >= %ver_major

# MATE Utilities
#Requires: mate-search-tool >= %ver_major
#Requires: mate-system-monitor >= %ver_major
Requires: mate-charmap
Requires: mate-calc >= %ver_major

# Applications
## Default file manager
Requires: mate-file-manager >= %ver_major
## Default terminal emulator
Requires: mate-terminal >= %terminal_ver
## Default archiving tool
Requires: mate-file-archiver
## Default text editor
#Requires: mate-text-editor

# Look & Feel
## Default themes
Requires: mate-icon-theme >= %ver_major
Requires: mate-icon-theme-faenza >= %ver_major
Requires: mate-themes >= %ver_major
#Requires: libgtk3-engine-adwaita
Requires: libgtk2-engine-adwaita

## Screensaver
Requires: mate-screensaver

# And, of course, the documentation
#Requires: mate-user-docs >= %gud_ver

%description minimal
This virtual package installs MATE Desktop with minimum components. It
installs only a few applets, necessary utilities and a minimal set of themes.
Doesn't install games and media programs.

## =========================================================================

%package default
Summary: MATE Desktop installer for optimal user's requirements
Group: Graphical desktop/MATE
Requires: %name-minimal = %version-%release

## Color manager
#Requires: mate-color-manager
## Password keeper
Requires: mate-keyring
# Encryption keys management
Requires: seahorse
#Requires: seahorse-agent
## All gvfs-backends
Requires: gvfs-backends
Requires: fuse-gvfs
#Requires: mate-disk-utility
## Display manager
#Requires: mate-display-manager
## Default web-browser (firefox)
Requires: firefox
## Default mailer
#Requires: evolution >= %ver_major
## Default messenger
#Requires: empathy >= %ver_major
#Requires: mate-contacts >= %ver_major
## Default RSS-reader
#Requires: liferea
## Default document reader (currently pdf, ps, tiff, dvi)
Requires: mate-document-viewer >= %evince_ver
## and E-Book Reader
#Requires: fbreader

## Applets
Requires: mate-applets

# Utilities
Requires: mate-utils >= %ver_major
Requires: mate-conf-editor 
#Requires: dconf-editor >= 0.10

## Let's have nice notifications
Requires: mate-notification-daemon

# Applications
## Plugins for gedit
#Requires: gedit-plugins
## Stock multimedia applications
Requires: mate-media
## Default music player
#Requires: rhythmbox
## Default media player
#Requires: totem
## Stock MATE games
#Requires: mate-games
## Default image viewer
Requires: mate-image-viewer >= %ver_major
## Default CD/DVD burning interface
#Requires: brasero >= %ver_major
## Clipboard manager
Requires: parcellite
# A quick previewer for Nautilus
#Requires: sushi
# Menu editor
#Requires: mate-menu-editor

# Look & Feel
## All default themes
#Requires: metacity-themes-default
#Requires: mate-themes-default >= %ver_major

Requires: mate-power-manager >= %ver_major
#Requires: NetworkManager-mate >= %network_manager_ver
## Bluetooth pairing and control applet
Requires: mate-bluetooth
## frontend for various networking tools
#Requires: mate-nettool
# user settings utility
#Requires: mate-tweak-tool >= %ver_major

# misc
Requires: mate-file-manager-sound-converter
Requires: mate-file-manager-sendto
Requires: mate-file-manager-open-terminal
Requires: mate-file-manager-image-converter
Requires: mate-netspeed
Requires: python-module-caja

Provides: mate-desktop-environment = %version

%description default
This virtual package installs MATE Desktop for an average user's
requirements. It installs components from mate-minimal package, some
games, media programs such as mixer, audio and video players, additional
themes, and some other programs that comprise MATE Desktop.
## =========================================================================

%package default-ru
Summary: MATE Desktop installer for optimal user's requirements, russian part
Group: Graphical desktop/MATE
## spell checking dictionary
Requires: hunspell-ru

%description default-ru
This virtual package installs spell checking dictionary for russian language

## =========================================================================

%package full
Summary: MATE Desktop full installer
Group: Graphical desktop/MATE
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
#Requires: materadio
## CD-ripper
#Requires: grip
## Image viewer, browser and simple editor
#Requires: gthumb
## Non-linear DV editor
#Requires: kino
#Requires: dvgrab
## SANE (Scanner Access Now Easy) frontend
#Requires: xsane

# Networking
## Utilities
## VNC server for the MATE Desktop
#Requires: vino
## VNC client for the MATE Desktop
#Requires: vinagre
## Internet telephon
#Requires: ekiga
## Client for ed2k network
#Requires: aMule

# Windows (TM) communications
## RDP
#Requires: rdesktop
## NX
#Requires: freenx
# Requires: nxlaunch

# Disks management
#Requires: gparted
Requires: consolehelper

# Look & Feel
## 3D screensavers
#Requires: mate-screensaver-modules-xscreensaver-gl

%description full
This virtual package installs full MATE Desktop except components from
mate-mobile and mate-a11y packages.

## =========================================================================
%package office
Summary: MATE Desktop applications for real office users
Group: Graphical desktop/MATE

## OpenOffice.org and MATE extensions for it
### Some openoffice.org-langpack-* packages need to be added to distribution profiles
#Requires: openoffice.org-gnome
## Diagram creation program
Requires: dia
## International dictionary (synchronize this section in -office package)
# GUI
Requires: stardict-gtk
# Some language independent StarDict dictionaries
Requires: stardict-engcom

%description office
This virtual package installs OpenOffice.org office suite with MATE extensions and
some applicatios necessary for every office user.

## =========================================================================

%package office-ru
Summary: russian stardict dictionaries for mate-office(-light) packages
Group: Graphical desktop/MATE
Requires: stardict-mueller7
Requires: stardict-slovnyk_en-ru
Requires: stardict-slovnyk_ru-en

%description office-ru
This virtual package installs stardict dictionaries for russian language

## =========================================================================
%package office-light
Summary: MATE 3 Desktop applications for real office users (light version)
Group: Graphical desktop/MATE

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
Requires: stardict-mate
# Some StarDict dictionaries
Requires: stardict-engcom

## Presentation tool ???

%description office-light
This virtual package installs applications necessary for every office
users such as word processor (Abiword), spreadsheet editor (Gnumeric) and
some other usefull programs

## =========================================================================
%package a11y
Summary: MATE Desktop accessibility applications
Group: Graphical desktop/MATE
# A synonym
Provides: sisyphus-accessibility
Obsoletes: %name-sisyphus-accessibility 
Provides: %name-sisyphus-accessibility = %version-%release
Requires: mate-minimal = %version-%release

Requires: gok >= %ver_major
Requires: mate-mag
Requires: dasher
Requires: mate-themes-accessibility
Requires: orca >= %orca_ver

%description a11y
This virtual package installs MATE Desktop accessibility applications.
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
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- dropped mate-display-manager

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1.1
- Build for Sisyphus

* Sun Oct 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- first version, based on gnome3 spec

