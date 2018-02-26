Name: cinnamon-meta
Version: 1.4.0
Release: alt2

Summary: Cinnamon desktop meta package
License: GPLv2+
Group: Graphical desktop/GNOME

Url: http://www.altlinux.org/Gnome
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
This package requires the various bits and pieces
for a reasonable Cinnamon desktop.

%package -n cinnamon-minimal
Summary: A minimal Cinnamon desktop meta package
Group: Graphical desktop/GNOME
#Requires: cinnamon gnome-panel nautilus notification-daemon
Requires: cinnamon nautilus notification-daemon

%description -n cinnamon-minimal
This package requires the various bits and pieces
for a minimal Cinnamon desktop.

%package -n cinnamon-fallback
Summary: A fallback Cinnamon desktop meta package
Group: Graphical desktop/GNOME
Requires: gnome-applets
Requires: gnome-applets-cpufreq gnome-applets-gweather
Requires: gnome-applets-multiload gnome-applets-stickynotes
Requires: gnome-applets-trash

%description -n cinnamon-fallback
This package requires the GNOME2 bits and pieces
for a fallback Cinnamon desktop environment.

%package -n cinnamon-sound
Summary: A Cinnamon desktop meta package for PulseAudio support
Group: Graphical desktop/GNOME
Requires: pulseaudio-daemon alsa-plugins-pulse

%description -n cinnamon-sound
This package requires PulseAudio related packages
for a Cinnamon desktop.

%package -n cinnamon-default
Summary: A default Cinnamon desktop meta package
Group: Graphical desktop/GNOME
Requires: cinnamon-minimal cinnamon-fallback cinnamon-sound
# shamelessly borrowed from gnome3-minimal-3.2.0-alt1
Requires: yelp >= 3.2
Requires: gnome-search-tool >= 3.2
Requires: gnome-system-monitor >= 3.2
Requires: gucharmap >= 3.2
Requires: gcalctool >= 3.2
Requires: nautilus >= 3.2
Requires: gnome-terminal >= 3.2
Requires: file-roller >= 3.2
Requires: gedit >= 3.2
Requires: gnome-screensaver  

%description -n cinnamon-default
This package requires the various bits and pieces
for a default Cinnamon desktop.

%prep

%files -n cinnamon-minimal
%files -n cinnamon-fallback
%files -n cinnamon-sound
%files -n cinnamon-default

%changelog
* Fri Apr 13 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- added fallback and sound packages to account for slava@'s feedback

* Thu Apr 12 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- initial release

