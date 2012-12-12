%define ver_major 0.96

Name: sugar-desktop-environment
Version: %ver_major.0
Release: alt1

Summary: Sugar Desktop installers
License: %gpl2plus
Group: Graphical desktop/Sugar

BuildArch: noarch
BuildRequires(pre): rpm-build-licenses

%description
A set of virtual packages for Sugar Desktop installation.

%package -n sugar-minimal
Summary: Sugar Desktop minimal installer
Group: Graphical desktop/Sugar
Provides: %name-core = %version-%release

Requires: sugar-glucose

%description -n sugar-minimal
This virtual package installs Sugar Desktop with minimum components. It
installs only a few activities and necessary utilities.

%package -n sugar-default
Summary: Sugar Desktop installer for optimal user's requirements
Group: Graphical desktop/Sugar
#Requires: %name-minimal = %version-%release

Requires: sugar
Requires: sugar-abacus
Requires: sugar-analyze
Requires: sugar-artwork
Requires: sugar-base
#Requires: sugar-browse
Requires: sugar-calculator
Requires: sugar-calendario
Requires: sugar-chat
Requires: sugar-clock
Requires: sugar-connect
Requires: sugar-countries
Requires: sugar-datastore
Requires: sugar-distance
Requires: sugar-finance
Requires: sugar-flip
Requires: sugar-flipsticks
Requires: sugar-getiabooks
Requires: sugar-help
Requires: sugar-imageviewer
Requires: sugar-implode
Requires: sugar-infoslicer
Requires: sugar-jukebox
Requires: sugar-labyrinth
Requires: sugar-log
Requires: sugar-logos
Requires: sugar-maze
Requires: sugar-measure
Requires: sugar-memorize
Requires: sugar-moon
Requires: sugar-nutrition
Requires: sugar-paint
Requires: sugar-physics
Requires: sugar-pippy
Requires: sugar-playgo
Requires: sugar-portfolio
Requires: sugar-presence-service
Requires: sugar-pukllanapac
Requires: sugar-read
Requires: sugar-recall
Requires: sugar-record
Requires: sugar-ruler
Requires: sugar-settings-manager
Requires: sugar-speak
Requires: sugar-stopwatch
#Requires: sugar-tamtam
Requires: sugar-terminal
Requires: sugar-toolkit
Requires: sugar-toolkit-gtk3
Requires: sugar-turtleart
Requires: sugar-typing-turtle
Requires: sugar-view-slides
Requires: sugar-visualmatch
Requires: sugar-write
Requires: sugar-xoirc
Requires: sugar-xomail
Requires: etoys-sugar

%description -n sugar-default
This virtual package -n sugar-installs Sugar Desktop for an average user's
requirements. 

%package -n sugar-full
Summary: Sugar Desktop full installer
Group: Graphical desktop/Sugar
Requires: %name-default = %version-%release

%description -n sugar-full
This virtual package installs full Sugar Desktop except .

#%files -n sugar-minimal
%files -n sugar-default
#%files -n sugar-full

%changelog
* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.0-alt1
- initial build
