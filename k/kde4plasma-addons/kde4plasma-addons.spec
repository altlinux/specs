%define _kde_alternate_placement 1

%add_findpackage_path %_kde4_bindir

%define rname kdeplasma-addons
Name: kde4plasma-addons
%define major 4
%define minor 8
%define bugfix 4
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4
License: GPL
Url: http://www.kde.org

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Patch1: kdeplasma-addons-4.5.0-alt-lancelot-new-document.patch
Patch2: kdeplasma-addons-4.5.0-alt-lancelot-services.patch
# MDK



Requires: plasma-applet-blackboard = %version-%release
Requires: plasma-applet-binaryclock = %version-%release
Requires: plasma-applet-bubblemon = %version-%release
Requires: plasma-applet-calculator = %version-%release
Requires: plasma-applet-charselect = %version-%release
Requires: plasma-applet-comic = %version-%release
Requires: plasma-applet-eyes = %version-%release
Requires: plasma-applet-fifteenpuzzle = %version-%release
Requires: plasma-applet-filewatcher = %version-%release
Requires: plasma-applet-frame = %version-%release
Requires: plasma-applet-fuzzy-clock = %version-%release
Requires: plasma-applet-incomingmsg = %version-%release
Requires: plasma-applet-icontasks = %version-%release
Requires: plasma-applet-kolourpicker = %version-%release
Requires: plasma-applet-konqprofiles = %version-%release
Requires: plasma-applet-konsoleprofiles = %version-%release
Requires: plasma-applet-lancelot = %version-%release
Requires: plasma-applet-leavenote = %version-%release
Requires: plasma-applet-life = %version-%release
Requires: plasma-applet-luna = %version-%release
Requires: plasma-applet-microblog = %version-%release
Requires: plasma-applet-notes = %version-%release
Requires: plasma-applet-nowplaying = %version-%release
Requires: plasma-applet-opendesktop = %version-%release
Requires: plasma-applet-paste = %version-%release
Requires: plasma-applet-pastebin = %version-%release
Requires: plasma-applet-previewer = %version-%release
Requires: plasma-applet-rtm = %version-%release
Requires: plasma-applet-showdashboard = %version-%release
Requires: plasma-applet-showdesktop = %version-%release
Requires: plasma-applet-systemloadviewer = %version-%release
Requires: plasma-applet-timer = %version-%release
Requires: plasma-applet-unitconverter = %version-%release
Requires: plasma-applet-plasmaboard = %version-%release
Requires: plasma-applet-webslice = %version-%release
Requires: plasma-applet-spellcheck = %version-%release
Requires: plasma-applet-qalculate = %version-%release
Requires: plasma-applet-knowledgebase = %version-%release
Requires: plasma-applet-kimpanel = %version-%release
Requires: plasma-applet-news = %version-%release
Requires: plasma-applet-rssnow = %version-%release
Requires: plasma-applet-weather = %version-%release
Requires: plasma-applet-weatherstation = %version-%release
Requires: plasma-applet-bookmarks = %version-%release
Requires: plasma-containment-griddesktop = %version-%release
Requires: plasma-containment-groupingdesktop = %version-%release
Requires: plasma-containment-groupingpanel = %version-%release
Requires: plasma-dataengine-comic = %version-%release
Requires: plasma-dataengine-microblog = %version-%release
Requires: plasma-dataengine-ocs = %version-%release
Requires: plasma-dataengine-potd = %version-%release
Requires: plasma-dataengine-rtm = %version-%release
Requires: plasma-dataengine-kdeobservatory = %version-%release
Requires: plasma-dataengine-kimpanel = %version-%release
Requires: plasma-runner-audioplayercontrol = %version-%release
Requires: plasma-runner-browserhistory = %version-%release
Requires: plasma-runner-contacts = %version-%release
Requires: plasma-runner-converter = %version-%release
Requires: plasma-runner-events = %version-%release
Requires: plasma-runner-katesessions = %version-%release
Requires: plasma-runner-konquerorsessions = %version-%release
Requires: plasma-runner-konsolesessions = %version-%release
Requires: plasma-runner-spellchecker = %version-%release
Requires: plasma-runner-mediawiki = %version-%release
Requires: plasma-runner-kopete = %version-%release
Requires: plasma-runner-charrunner = %version-%release
Requires: plasma-runner-datetime = %version-%release
Requires: plasma-wallpaper-mandelbrot = %version-%release
Requires: plasma-wallpaper-marble = %version-%release
Requires: plasma-wallpaper-pattern = %version-%release
Requires: plasma-wallpaper-virus = %version-%release
Requires: plasma-wallpaper-weather = %version-%release
Requires: plasma-wallpaper-potd = %version-%release

# Automatically added by buildreq on Mon Sep 15 2008 (-bi)
#BuildRequires: gcc-c++ kde4base-workspace-core kde4base-workspace-devel kde4network-kopete kde4pim-kmail kde4pimlibs-devel libXScrnSaver-devel libXcomposite-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libldap-devel libxkbfile-devel nvidia_glx_173.14.12 python-modules-xml rpm-build-ruby shared-mime-info xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4base-workspace-devel kde4pimlibs-devel
BuildRequires: gcc-c++ libldap-devel scim-devel attica-devel libqca2-devel
BuildRequires: soprano soprano-backend-redland libsoprano-devel libqalculate-devel
BuildRequires: python-modules-xml shared-mime-info
BuildRequires: python-devel eigen2 libdbusmenu-qt-devel
BuildRequires: kde4network-devel kde4pim-devel kde4graphics-devel kde4edu-devel
BuildRequires: kde4base-workspace-devel >= %version kde4pimlibs-devel >= %version

%description
kdeplasma is a compilation of plasma items ( runners, applets, plasmoids ) for kde4.

%package maxi
Summary: %name maximum package
Group: Graphical desktop/KDE
Requires: %name
Requires: plasma-applet-bball = %version-%release
Requires: plasma-applet-dict = %version-%release
Requires: plasma-applet-mediaplayer = %version-%release
Requires: plasma-applet-magnifique = %version-%release
%description maxi
Maximum package of %name

%package common
Summary: %name common package
Group: System/Configuration/Other
%description common
Common package for %name

%package -n plasma-applet-icontasks
Summary: Icon-Only Task Manager
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-icontasks
This is a desktop applet which provides a view
of the user's running graphical tasks and allows them to
switch between these tasks.

%package -n plasma-dataengine-kimpanel
Summary: DataEngine for Kimpanel
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-kimpanel
DataEngine for Kimpanel

%package -n plasma-applet-kimpanel
Summary: A generic input method panel for Oriental languages
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: plasma-dataengine-kimpanel
%description -n plasma-applet-kimpanel
A generic input method panel for Oriental languages

%package -n plasma-applet-bubblemon
Summary: Monitor your system
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-bubblemon
A pretty bubble that monitors your system.

%package -n plasma-applet-filewatcher
Summary: Monitor applet for files
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-filewatcher
Monitor applet for files.

%package -n plasma-applet-notes
Summary: Plasma notes applets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-notes
Plasma notes applets.

%package -n plasma-wallpaper-mandelbrot
Summary: Mandelbrot wallpaper
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-mandelbrot
Mandelbrot wallpaper.

%package -n plasma-wallpaper-potd
Summary: Potd wallpaper
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: plasma-dataengine-potd
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-potd
Potd wallpaper.

%package -n plasma-wallpaper-virus
Summary: Virus wallpaper
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-virus
Virus wallpaper.

%package -n plasma-wallpaper-marble
Summary: OpenGL world planet wallpaper
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-marble
OpenGL world planet wallpaper.

%package -n plasma-wallpaper-pattern
Summary: Pattern wallpaper
Group: Graphical desktop/KDE
Provides: plasma-wallpaper
Requires: %name-common = %version-%release
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-pattern
Pattern wallpaper.

%package -n plasma-wallpaper-weather
Summary: Weather wallpaper
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-wallpaper = %version-%release
%description -n plasma-wallpaper-weather
Weather wallpaper.

%package -n plasma-applet-showdesktop
Summary: Show desktop contents
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-showdesktop
Show desktop contents.

%package -n plasma-applet-comic
Summary: Make your day happy with daily desktop comics applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: plasma-dataengine-comic
%description -n plasma-applet-comic
Make your day happy with daily desktop comics applet

%package -n plasma-applet-konqprofiles
Summary: Live konqueror profile viewer
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-konqprofiles
Live konqueror profile viewer.

%package -n plasma-applet-konsoleprofiles
Summary: Live konsole profile viewer
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-konsoleprofiles
Live konsole profile viewer.

%package -n plasma-applet-luna
Summary: Lunar calendar
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-luna
Lunar calendar applet.

%package -n plasma-applet-bball
Summary: A bouncy ball for plasma
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-bball
A bouncy ball for plasma

%package -n plasma-applet-charselect
Summary: Character Selector
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-charselect
View, select, and copy characters from a font collection

%package -n plasma-applet-eyes
Summary: XEyes clone
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-eyes
XEyes clone

%package -n plasma-applet-incomingmsg
Summary: Notification of new messages
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-incomingmsg
Notification of new messages

%package -n plasma-applet-leavenote
Summary: Leave notes for users while they are away
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-leavenote
Leave notes for users while they are away

%package -n plasma-applet-life
Summary: Conway's Game of Life applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-life
Conway's Game of Life applet

%package -n plasma-applet-news
Summary: Show news from various sources
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-news
Show news from various sources

%package -n plasma-applet-paste
Summary: Paste text snippets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-paste
Paste text snippets

%package -n plasma-applet-pastebin
Summary: Paste text/images to a remote server
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-pastebin
Paste text/images to a remote server

%package -n plasma-applet-previewer
Summary: Quickly preview a variety of files
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-previewer
Quickly preview a variety of files

%package -n plasma-applet-rssnow
Summary: Show news from various sources
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-rssnow
Show news from various sources

%package -n plasma-applet-timer
Summary: Timer applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-timer
Countdown over a specified time period

%package -n plasma-applet-weatherstation
Summary: LCD Weather Station
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-weatherstation
Weather reports with an LCD display style

%package -n plasma-applet-lancelot
Summary: Plasma lancelot applets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-lancelot
Plasma lancelot applets.

%package -n libkimpanelruntime4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkimpanelruntime4
%name library.

%package -n liblancelot4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n liblancelot4
%name library.

%package -n plasma-applet-microblog
Summary: Microblog applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: plasma-dataengine-microblog
Provides: plasma-applet-twitter = %version-%release
Obsoletes: plasma-applet-twitter < %version-%release
%description -n plasma-applet-microblog
Microblog applet

%package -n plasma-applet-nowplaying
Summary: SWoong notifier applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-nowplaying
Song notifier applet

%package -n plasma-applet-binaryclock
Summary: Simplified way to see the hours
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-binaryclock
Simplified way to see the hours.

%package -n plasma-applet-dict
Summary: Dict applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-dict
A dict applets.

%package -n plasma-applet-fuzzy-clock
Summary: A lazy way to see the hours
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-fuzzy-clock
A lazy way to see the hours.

%package -n plasma-applet-frame
Summary: A basic pictures frame to desktop
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-frame
A basic pictures frame to desktop.

%package -n plasma-applet-showdashboard
Summary: Plasma showdashboard applets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-showdashboard
Plasma showdashboard applets.

%package -n plasma-applet-mediaplayer
Summary: Widget that can play video and sound
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-mediaplayer
Widget that can play video and sound.

%package -n plasma-applet-opendesktop
Summary: Communicate using the Social Desktop
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-opendesktop
Communicate using the Social Desktop.

%package -n plasma-applet-calculator
Summary: Plasma calculator applets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-calculator
Plasma calculator applets.

%package -n plasma-applet-weather
Summary: Weather Forecast
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-weather
Weather Forecast.

%package -n plasma-applet-fifteenpuzzle
Summary: Plasma fifteenpuzzle applets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-fifteenpuzzle
Plasma fifteenpuzzle applets.

%package -n plasma-applet-kolourpicker
Summary: Basic color picker
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-kolourpicker
Basic color picker.

%package -n plasma-applet-systemloadviewer
Summary: System Load Viewer
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-systemloadviewer
System Load Viewer.

%package -n plasma-applet-magnifique
Summary: A magnification glass for Plasma canvas
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-magnifique
A magnification glass for Plasma canvas.

%package -n plasma-applet-rtm
Summary: Remember The Milk Todo list applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-applet-rememberthemilk = %version-%release
Requires: plasma-dataengine-rtm = %version-%release
%description -n plasma-applet-rtm
Remember The Milk Todo list applet.

%package -n plasma-applet-unitconverter
Summary: Unit Converter
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-unitconverter
Unit Converter.

%package -n plasma-containment-griddesktop
Summary: Plasma containment
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-containment-griddesktop
Plasma containment.

%package -n plasma-containment-groupingdesktop
Summary: Plasma containment
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-containment-groupingdesktop
Plasma containment.

%package -n plasma-containment-groupingpanel
Summary: Plasma containment
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-containment-groupingpanel
Plasma containment.

%package -n plasma-dataengine-pastebin
Summary: Engine of the pastebin plasma applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-pastebin
Engine of the pastebin plasma applet

%package -n plasma-dataengine-comic
Summary: Plasma comic dataengines
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-comic
Plasma comic dataengines.

%package -n plasma-dataengine-rtm
Summary: An engine to work with Remember the Milk
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-dataengine-rememberthemilk = %version-%release
%description -n plasma-dataengine-rtm
An engine to work with Remember the Milk.

%package -n plasma-dataengine-microblog
Summary: Plasma microblog dataengine
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: plasma-dataengine-twitter = %version-%release
Obsoletes: plasma-dataengine-twitter < %version-%release
%description -n plasma-dataengine-microblog
Plasma microblog dataengine.

%package -n plasma-dataengine-potd
Summary: Picture of the Day
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-potd
Data Engine for getting various online Pictures of The Day.

%package -n plasma-dataengine-ocs
Summary: Open Collaboration Services
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-ocs
Open Collaboration Services.

%package -n plasma-dataengine-kdeobservatory
Summary: Plasma kdeobservatory dataengine
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-dataengine-kdeobservatory
Plasma kdeobservatory dataengine.

%package -n libplasmacomicprovidercore4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmacomicprovidercore4
%name library.

%package -n libplasmaappletdialog4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmaappletdialog4
%name library.

%package -n libplasmaconverter4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmaconverter4
%name library.

%package -n libconversion4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libconversion4
%name library.

%package -n libocsclient4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libocsclient4
%name library.

%package -n libplasmapotdprovidercore4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmapotdprovidercore4
%name library.

%package -n libplasmaweather4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasmaweather4
%name library.

%package -n librtm4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n librtm4
%name library.

%package -n liblancelot4-datamodels
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n liblancelot4-datamodels
%name library.

%package -n plasma-runner-audioplayercontrol
Summary: Plasma runner audioplayercontrol
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-audioplayercontrol
Plasma runner audioplayercontrol

%package -n plasma-runner-converter
Summary: Plasma converter runners
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-converter
Plasma converter runners.

%package -n plasma-runner-contacts
Summary: Plasma contacts runners
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-contacts
Plasma contacts runners.

%package -n plasma-runner-spellchecker
Summary: Plasma runner spellchecker
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-spellchecker
Plasma runner spellchecker

%package -n plasma-runner-browserhistory
Summary: Plasma runner browserhistory
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-browserhistory
Plasma runner browserhistory

%package -n plasma-runner-katesessions
Summary: Plasma katesessions runner
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-katesessions
Plasma runner katesessions

%package -n plasma-runner-konquerorsessions
Summary: Plasma runner konquerorsessions
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-konquerorsessions
Plasma runner konquerorsessions

%package -n plasma-runner-konsolesessions
Summary: Plasma runner konsolesessions
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-konsolesessions
Plasma runner konsolesessions

%package -n plasma-runner-charrunner
Summary: Plasma runner 
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-charrunner
Plasma runner 

%package -n plasma-runner-datetime
Summary: Plasma runner 
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-datetime
Plasma runner 

%package -n plasma-applet-plasmaboard
Summary: A plasmaboard plasma applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-plasmaboard
A plasmaboard plasma applet

%package -n plasma-runner-mediawiki
Summary: Plasma runner mediawiki
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-mediawiki
Plasma runner mediawiki

%package -n plasma-runner-events
Summary: Plasma runner events
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-events
Plasma runner events

%package -n plasma-runner-kopete
Summary: Plasma runner kopete
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-runner-kopete
Plasma runner kopete

%package -n plasma-applet-webslice
Summary:  Applet that show a part of a webpage
Group:    Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-webslice
Applet that show a part of a webpage

%package -n plasma-applet-spellcheck
Summary:  Fast spell checking applet
Group:    Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-spellcheck
Fast spell checking applet

%package -n plasma-applet-qalculate
Summary: A Qalculate plasma applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-qalculate
A Qalculate plasma applet

%package -n plasma-applet-knowledgebase
Summary: Widget that can query the knowledgebase of opendesktop.org
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-knowledgebase
Widget that can query the knowledgebase of opendesktop.org

%package -n plasma-applet-blackboard
Summary: A blackboard plasma applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-blackboard
A blackboard plasma applet

%package -n plasma-applet-bookmarks
Summary: A bookmarks plasma applet
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description -n plasma-applet-bookmarks
A bookmarks plasma applet

%package -n libplasma4_groupingcontainment
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libplasma4_groupingcontainment
%name library.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kde4libs-devel
%description devel
This package contains header files needed if you wish to build applications
based on %name


%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1


%build
%K4cmake
# -DKEXIV2_LIBRARIES:PATH=%_K4link/libkexiv2.so
%K4make

%install
%K4install




%files maxi
%files
%files common
%dir %_K4apps/kdeplasma-addons/

%files -n plasma-applet-icontasks
%_K4lib/plasma_applet_icontasks.so
%_K4apps/desktoptheme/default/icontasks/
%_K4apps/kdeplasma-addons/mediabuttonsrc
%_K4srv/plasma-applet-icontasks.desktop

%files -n plasma-wallpaper-potd
%_K4lib/plasma_wallpaper_potd.so
%_K4srv/plasma-wallpaper-potd.desktop

%files -n plasma-containment-griddesktop
%_K4lib/plasma_containment_griddesktop.so
%_K4srv/plasma-containment-griddesktop.desktop

%files -n plasma-containment-groupingdesktop
%_K4lib/plasma_containment_groupingdesktop.so
%_K4srv/plasma-containment-groupingdesktop.desktop

%files -n plasma-containment-groupingpanel
%_K4lib/plasma_containment_groupingpanel.so
%_K4srv/plasma-containment-groupingpanel.desktop

%files -n plasma-runner-events
%_K4lib/plasma_runner_events.so
%_K4lib/kcm_plasma_runner_events.so
%_K4srv/plasma-runner-events.desktop
%_K4srv/plasma-runner-events_config.desktop

%files -n plasma-runner-charrunner
%_K4lib/kcm_krunner_charrunner.so
%_K4lib/krunner_charrunner.so
%_K4srv/CharRunner_config.desktop
%_K4srv/CharacterRunner.desktop

%files -n plasma-applet-bookmarks
%_K4lib/plasma_applet_bookmarks.so
%_K4srv/plasma-applet-bookmarks.desktop

%files -n plasma-dataengine-kdeobservatory
%_K4lib/plasma_engine_kdeobservatory.so
%_K4apps/plasma/services/kdeobservatory.operations
%_K4srv/plasma-engine-kdeobservatory.desktop

%files -n plasma-runner-datetime
%_K4lib/plasma_runner_datetime.so
%_K4srv/plasma-runner-datetime.desktop

%files -n liblancelot4-datamodels
%_K4libdir/liblancelot-datamodels.so.*

#%files -n libkimpanelruntime4
#%_K4libdir/libkimpanelruntime.so.*

%files -n plasma-dataengine-kimpanel
%_K4lib/plasma_engine_kimpanel.so
%_K4apps/plasma/services/kimpanel.*
%_K4srv/plasma-dataengine-kimpanel.desktop

%files -n plasma-applet-kimpanel
%_K4exec/kimpanel-scim-panel
%_K4lib/plasma_applet_kimpanel.so
%_K4cfg/kimpanelconfig.kcfg
%_K4srv/plasma-applet-kimpanel.desktop

%files -n plasma-applet-plasmaboard
%_K4apps/plasmaboard
%_K4lib/plasma_applet_plasmaboard.so
%_K4srv/plasma_applet_plasmaboard.desktop

%files -n plasma-runner-mediawiki
%_K4lib/krunner_mediawiki.so
%_K4srv/plasma-runner-techbase.desktop
%_K4srv/plasma-runner-wikipedia.desktop
%_K4srv/plasma-runner-wikitravel.desktop

%files -n plasma-runner-kopete
%_K4lib/krunner_kopete.so
%_K4srv/plasma-runner-kopete.desktop

%files -n plasma-applet-webslice
%_K4lib/plasma_applet_webslice.so
%_K4srv/plasma-applet-webslice.desktop

%files -n plasma-applet-spellcheck
%_K4lib/plasma_applet_spellcheck.so
%_K4srv/plasma-applet-spellcheck.desktop

%files -n plasma-applet-qalculate
%_K4lib/plasma_applet_qalculate.so
%_K4srv/plasma-applet-qalculate.desktop
%_kde4_iconsdir/hicolor/*/apps/qalculate-applet.*

%files -n plasma-applet-knowledgebase
%_K4lib/plasma_applet_knowledgebase.so
%_K4srv/plasma-applet-knowledgebase.desktop

%files -n plasma-applet-blackboard
%_K4lib/plasma_applet_blackboard.so
%_K4srv/plasma-applet-blackboard.desktop

%files -n plasma-runner-audioplayercontrol
%_K4lib/kcm_krunner_audioplayercontrol.so
%_K4lib/krunner_audioplayercontrol.so
%_K4srv/plasma-runner-audioplayercontrol.desktop
%_K4srv/plasma-runner-audioplayercontrol_config.desktop

%files -n plasma-dataengine-rtm
%_K4lib/plasma_engine_rtm.so
%_K4srv/plasma-engine-rtm.desktop
%_K4apps/plasma/services/rtmauth.operations
%_K4apps/plasma/services/rtmtask.operations
%_K4apps/plasma/services/rtmtasks.operations

%files -n plasma-dataengine-potd
%_K4lib/plasma_potd_*.so
%_K4lib/plasma_engine_potd.so
%_K4srv/plasma-dataengine-potd.desktop
%_K4srv/apodprovider.desktop
%_K4srv/epodprovider.desktop
%_K4srv/flickrprovider.desktop
%_K4srv/oseiprovider.desktop
%_K4srv/wcpotdprovider.desktop
%_K4srvtyp/plasma_potdprovider.desktop

%files -n plasma-dataengine-ocs
%_K4lib/plasma_engine_ocs.so
%_K4srv/plasma-dataengine-ocs.desktop

%files -n plasma-applet-weather
%_K4lib/plasma_applet_weather.so
%_K4srv/plasma-applet-weather.desktop
%_K4apps/desktoptheme/default/weather/wind-arrows.svgz

%files -n plasma-applet-unitconverter
%_K4lib/plasma_applet_unitconverter.so
%_K4srv/plasma-applet-unitconverter.desktop

%files -n plasma-applet-rtm
%_K4lib/plasma_applet_rtm.so
%_K4srv/plasma-applet-rememberthemilk.desktop

%files -n plasma-applet-opendesktop
%_K4lib/plasma_applet_opendesktop.so
%_K4lib/plasma_applet_opendesktop_activities.so
%_K4apps/plasma-applet-opendesktop
%_K4apps/plasma-applet-opendesktop-activities
%_K4apps/plasma/services/ocsPerson.operations
%_K4srv/plasma-applet-opendesktop.desktop
%_K4srv/plasma-applet-opendesktop-activities.desktop

%files -n plasma-applet-mediaplayer
%_K4lib/plasma_applet_mediaplayer.so
%_K4srv/plasma-applet-mediaplayer.desktop

%files -n plasma-applet-magnifique
%_K4lib/plasma_applet_magnifique.so
%_K4srv/plasma-applet-magnifique.desktop

%files -n plasma-applet-bubblemon
%_K4lib/plasma_applet_bubblemon.so
%_K4srv/plasma-applet-bubblemon.desktop
%_K4apps/desktoptheme/default/bubblemon/bubble.svg

%files -n plasma-applet-systemloadviewer
%_K4lib/plasma-applet_systemloadviewer.so
%_K4srv/plasma-applet-systemloadviewer.desktop

%files -n plasma-applet-filewatcher
%_K4lib/plasma_applet_fileWatcher.so
%_K4srv/plasma-fileWatcher-default.desktop

%files -n plasma-applet-notes
%_K4lib/plasma_applet_notes.so
%_K4apps/desktoptheme/default/widgets/notes.*
%_K4srv/plasma-notes-default.desktop


%files -n plasma-applet-showdesktop
%_K4lib/plasma_applet_showdesktop.so
%_K4srv/plasma-applet-showdesktop.desktop

%files -n plasma-applet-comic
%_K4lib/plasma_applet_comic.so
%_K4lib/plasma_packagestructure_comic.so
#%_K4apps/plasma-comic
#%_K4srv/xkcdprovider.desktop
#%_K4srv/userfriendlyprovider.desktop
#%_K4srv/snoopyprovider.desktop
#%_K4srv/dilbertprovider.desktop
#%_K4srv/garfieldprovider.desktop
#%_K4srv/osnewsprovider.desktop
#%_K4srv/phdprovider.desktop
%_K4srv/plasma-packagestructure-comic.desktop
%_K4srvtyp/plasma_comicprovider.desktop
%_K4conf/comic.knsrc

%files -n plasma-applet-konqprofiles
%_K4lib/plasma_applet_konqprofiles.so
%_K4srv/plasma-applet-konqprofiles.desktop

%files -n plasma-applet-konsoleprofiles
%_K4lib/plasma_applet_konsoleprofiles.so
%_K4srv/plasma-applet-konsoleprofiles.desktop

%files -n plasma-applet-luna
%_K4lib/plasma_applet_luna.so
%_K4apps/desktoptheme/default/widgets/luna.*
%_K4srv/plasma-applet-luna.desktop
%_kde4_iconsdir/hicolor/*/apps/luna.*

%files -n plasma-applet-bball
%_K4lib/plasma_applet_bball.so
%_K4srv/plasma-applet-bball.desktop
%_kde4_iconsdir/hicolor/*/apps/bball.*
%_K4apps/bball/

%files -n plasma-applet-charselect
%_K4lib/plasma_applet_charselect.so
%_K4srv/plasma-applet-charselect.desktop

%files -n plasma-applet-eyes
%_K4lib/plasma_applet_eyes.so
%_K4apps/desktoptheme/default/widgets/eyes.*
%_K4srv/plasma-applet-eyes.desktop
%_kde4_iconsdir/hicolor/*/apps/eyes.*

%files -n plasma-applet-incomingmsg
%_K4lib/plasma_applet_incomingmsg.so
%_K4srv/plasma-applet-incomingmsg.desktop

%files -n plasma-applet-leavenote
%_K4lib/plasma_applet_leavenote.so
%_K4srv/plasma-applet-leavenote.desktop

%files -n plasma-applet-life
%_K4lib/plasma_applet_life.so
%_K4srv/plasma-applet-life.desktop
%_kde4_iconsdir/hicolor/*/apps/lifegame.*

%files -n plasma-applet-news
%_K4apps/desktoptheme/default/stylesheets/news.css
%_K4lib/plasma_applet_news.so
%_K4srv/plasma-applet-news.desktop

%files -n plasma-applet-paste
%_K4lib/plasma_applet_paste.so
%_K4srv/plasma-applet-paste.desktop

%files -n plasma-applet-pastebin
%_K4lib/plasma_applet_pastebin.so
%_K4srv/plasma-applet-pastebin.desktop
%_K4apps/plasma_pastebin
%_K4conf/pastebin.knsrc

%files -n plasma-applet-previewer
%_K4lib/plasma_applet_previewer.so
%_K4srv/plasma-applet-previewer.desktop
%_K4srv/ServiceMenus/preview.desktop
%_K4apps/desktoptheme/default/widgets/previewer-*.*
%_kde4_iconsdir/hicolor/*/apps/previewer.*

%files -n plasma-applet-rssnow
%_K4lib/plasma_applet_rssnow.so
%_K4apps/desktoptheme/default/rssnow
%_K4srv/plasma-applet-rssnow.desktop
%_K4apps/rssnow/

%files -n plasma-applet-timer
%_K4lib/plasma_applet_timer.so
%_K4apps/desktoptheme/default/widgets/timer.*
%_K4srv/plasma-applet-timer.desktop

%files -n plasma-applet-weatherstation
%_K4apps/desktoptheme/default/weatherstation/
%_K4lib/plasma_applet_weatherstation.so
%_K4srv/plasma-applet-weatherstation.desktop

%files -n plasma-applet-lancelot
%_kde4_bindir/lancelot
%_K4lib/plasma_applet_lancelot_part.so
%_K4lib/plasma_applet_lancelot_launcher.so
%_K4srv/plasma-applet-lancelot-launcher.desktop
%_kde4_iconsdir/hicolor/*/apps/lancelot*.*
%_kde4_iconsdir/hicolor/*/apps/plasmaapplet-shelf.*
%_K4srv/plasma-applet-lancelot-part.desktop
%_K4srv/lancelot.desktop
%_K4xdg_mime/lancelotpart-mime.xml
%_K4apps/desktoptheme/*/lancelot
%_K4apps/lancelot

%files -n liblancelot4
%_K4libdir/liblancelot.so.*

%files -n plasma-applet-microblog
%_K4lib/plasma_applet_microblog.so
%_K4srv/plasma-applet-microblog.desktop
%_K4apps/desktoptheme/default/widgets/microblog.svgz

%files -n plasma-applet-nowplaying
%_K4apps/desktoptheme/default/widgets/nowplaying/nocover.svgz
%_K4lib/plasma_applet_nowplaying.so
%_K4srv/plasma-applet-nowplaying.desktop

%files -n plasma-applet-binaryclock
%_K4lib/plasma_applet_binaryclock.so
%_K4srv/plasma-applet-binaryclock.desktop

%files -n plasma-applet-dict
%_K4lib/plasma_applet_dict.so
%_K4srv/plasma-dict-default.desktop
%_kde4_iconsdir/*/*/apps/accessories-dictionary.*

%files -n plasma-applet-fuzzy-clock
%_K4lib/plasma_applet_fuzzy_clock.so
%_K4srv/plasma-clock-fuzzy.desktop

%files -n plasma-applet-frame
%_K4apps//plasma-applet-frame
%_K4lib/plasma_applet_frame.so
%_K4srv/plasma-frame-default.desktop

%files -n plasma-applet-showdashboard
%_K4lib/plasma_applet_showdashboard.so
%_K4srv/plasma-applet-showdashboard.desktop

%files -n plasma-applet-calculator
%_K4lib/plasma_applet_calculator.so
%_K4srv/plasma-applet-calculator.desktop

%files -n plasma-applet-fifteenpuzzle
%_K4lib/plasma_applet_fifteenPuzzle.so
%_K4srv/plasma-applet-fifteenPuzzle.desktop
%_kde4_iconsdir/*/*/*/fifteenpuzzle.*
%dir %_K4apps/desktoptheme/default/fifteenPuzzle/
%_K4apps/desktoptheme/default/fifteenPuzzle/blanksquare.svg

%files -n plasma-applet-kolourpicker
%_K4lib/plasma_applet_kolourpicker.so
%_K4srv/plasma-kolourpicker-default.desktop

%files -n plasma-dataengine-comic
%_K4lib/plasma_comic*
%_K4lib/plasma_engine_comic.*
%_K4srv/plasma-comic-default.desktop
%_K4srv/plasma-dataengine-comic.desktop

%files -n plasma-dataengine-microblog
%_K4lib/plasma_engine_microblog.so
%_K4srv/plasma-dataengine-microblog.desktop
%_K4apps/plasma/services/tweet.operations

%files -n plasma-runner-contacts
%_K4lib/krunner_contacts.so
%_K4srv/plasma-runner-contacts.desktop

%files -n plasma-runner-spellchecker
%_K4lib/krunner_spellcheckrunner.so
%_K4lib/kcm_krunner_spellcheck.so
%_K4srv/plasma-runner-spellchecker.desktop
%_K4srv/plasma-runner-spellchecker_config.desktop

%files -n plasma-runner-converter
%_K4lib/krunner_converter.so
%_K4srv/plasma-runner-converter.desktop

%files -n plasma-runner-browserhistory
%_K4lib/krunner_browserhistory.so
%_K4srv/browserhistory.desktop

%files -n plasma-runner-katesessions
%_K4lib/krunner_katesessions.so
%_K4srv/katesessions.desktop

%files -n plasma-runner-konquerorsessions
%_K4lib/krunner_konquerorsessions.so
%_K4srv/konquerorsessions.desktop

%files -n plasma-runner-konsolesessions
%_K4lib/krunner_konsolesessions.so
%_K4srv/konsolesessions.desktop

%files -n plasma-wallpaper-mandelbrot
%_K4lib/plasma_wallpaper_mandelbrot.so
%_K4srv/plasma-wallpaper-mandelbrot.desktop

%files -n plasma-wallpaper-virus
%_K4lib/plasma_wallpaper_virus.so
%_K4srv/plasma-wallpaper-virus.desktop
%_K4conf/virus_wallpaper.knsrc

%files -n plasma-wallpaper-weather
%_K4lib/plasma_wallpaper_weather.so
%_K4srv/plasma-wallpaper-weather.desktop
%_K4conf/plasmaweather.knsrc

%files -n plasma-wallpaper-pattern
%_K4lib/plasma_wallpaper_pattern.so
%_K4srv/plasma-wallpaper-pattern.desktop
%_K4apps/plasma_wallpaper_pattern

%files -n plasma-wallpaper-marble
%_K4lib/plasma_wallpaper_marble.so
%_K4srv/plasma-wallpaper-marble.desktop

%files -n libplasmacomicprovidercore4
%_K4libdir/libplasmacomicprovidercore.so.*

%files -n libplasmapotdprovidercore4
%_K4libdir/libplasmapotdprovidercore.so.*
%files -n libplasmaweather4
%_K4libdir/libplasmaweather.so.*
%files -n librtm4
%_K4libdir/librtm.so.*
%files -n libplasma4_groupingcontainment
%_K4libdir/libplasma_groupingcontainment.so.*

%files devel
%_K4apps/cmake/modules/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Fri Apr 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Tue May 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1.M51.1
- built for M51

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- requires all applets only with -maxi subpackage

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- add lancelot and bball fixes

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Wed Jan 21 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- removed deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 19 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- initial specfile
