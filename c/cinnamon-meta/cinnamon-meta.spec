%define ver_major 1.6

Name: cinnamon-meta
Version: %ver_major.0
Release: alt1

Summary: Cinnamon desktop meta package
License: %gpl2plus
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/Cinnamon
Packager: Vladimir Didenko <cow@altlinux.org>
BuildArch: noarch

BuildPreReq: rpm-build-licenses


%description
A set of virtual packages for Cinnamon Desktop installation.


%package -n cinnamon-minimal
Summary: A minimal Cinnamon desktop meta package
Group: Graphical desktop/GNOME

# Cinnamon Desktop Core
Requires: cinnamon >= %ver_major
Requires: gnome-session >= 3.4
# Window manager
Requires: muffin >= 1.0.5

%description -n cinnamon-minimal
This package provides minimal set of components to run 
Cinnamon desktop.

%package -n cinnamon-default
Summary: A default Cinnamon desktop meta package
Group: Graphical desktop/GNOME

Requires: cinnamon-minimal
# Sound support
Requires: pulseaudio-daemon alsa-plugins-pulse
# Default file manager
Requires: nemo
# Default terminal
Requires: gnome-terminal 
# Screensaver
Requires: gnome-screensaver  
#Gvfs
Requires: gvfs gvfs-backends
#Cinnamon doesn't have own freedesktop menu yet
Requires: altlinux-freedesktop-menu-gnome3

# Look and Feel
Requires: gnome-icon-theme >= %ver_major
Requires: gnome-icon-theme-symbolic >= %ver_major
Requires: gnome-themes-standard >= %ver_major
Requires: libgtk3-engine-adwaita
Requires: libgtk2-engine-adwaita

%description -n cinnamon-default
This package provides the various bits and pieces
for a default Cinnamon desktop.

%package -n cinnamon-full
Summary: Meta package for Cinnamon desktop and default applications
Group: Graphical desktop/GNOME

Requires: cinnamon-default

# Color manager
Requires: gnome-color-manager
# Password keeper
Requires: gnome-keyring
# Encryption keys management
Requires: seahorse
# Clipboard manager
Requires: parcellite
# Display manager 
Requires: gdm gdm-gnome 

# Default web-browser 
Requires: firefox
# Default mailer
Requires: thunderbird
# Default messenger
Requires: pidgin

# Default Document viewer
Requires: evince
# Default text editor
Requires: gedit
Requires: gedit-plugins 

# Utilities
Requires: gnome-utils 
Requires: gconf-editor >= 3.0
Requires: dconf-editor >= 0.10
Requires: gnome-control-center
# Required to set keyboard layout to Alt+Shift, Ctrl+Shift etc.
Requires: gnome-tweak-tool >= 3.6

# Default music player
Requires: rhythmbox
# Default video player
Requires: gnome-mplayer
# Default image viewer
Requires: gthumb
# Default CD/DVD burning interface
Requires: brasero 

Requires: gnome-power-manager 
Requires: NetworkManager-gnome >= 0.8.995

%description -n cinnamon-full
This package provides Cinnamon desktop and set
of default applications.

%prep

%files -n cinnamon-minimal
%files -n cinnamon-default
%files -n cinnamon-full

%changelog
* Sat Nov 17 2012 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt1
- dropped fallback package: cinnamon has own fallback
- dropped sound package: moved dependencies to default package
- new full package: provides list of default applications

* Fri Apr 13 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- added fallback and sound packages to account for slava@'s feedback

* Thu Apr 12 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- initial release

