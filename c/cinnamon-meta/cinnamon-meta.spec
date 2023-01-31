%define ver_major 5.6

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

%package -n cinnamon-default
Summary: A default Cinnamon desktop meta package
Group: Graphical desktop/GNOME

# cow@: cinnamon-minimal is now moved to cinnamon package.
# See https://bugzilla.altlinux.org/42722 for details
Requires: cinnamon-minimal >= %ver_major
Provides: cinnamon-full = %version-%release
# Default terminal
Requires: gnome-terminal

# Look and Feel
Requires: gnome-icon-theme
Requires: gnome-icon-theme-symbolic
Requires: gnome-themes-standard
Requires: libgtk2-engine-adwaita
Requires: gnome-backgrounds
# default font
Requires: fonts-otf-abattis-cantarell
# additional icons for cinnamon apps
Requires: xapps-icons

# Cinnamon uses yelp to show help
Requires: yelp

%description -n cinnamon-default
This package provides the various bits and pieces
for a default Cinnamon desktop.

%package -n cinnamon-regular
Summary: Meta package for Cinnamon desktop and set of default applications
Group: Graphical desktop/GNOME

Requires: cinnamon-default = %version-%release

# Sound support
Requires: pulseaudio-daemon alsa-plugins-pulse
# Color manager
Requires: gnome-color-manager
# Password keeper
Requires: gnome-keyring
# Encryption keys management
Requires: seahorse
# Clipboard manager
Requires: parcellite
# Display manager
Requires: lightdm slick-greeter lightdm-settings
# Integration with fileroller (see #34711)
Requires: nemo-fileroller
# Support Samba files sharing
Requires: nemo-share

# Default Document viewer
Requires: xreader
# Default text editor
Requires: xed

# Utilities
Requires: gnome-utils
Requires: dconf-editor >= 0.10
Requires: gcalctool

# Default video player
Requires: celluloid
# Default image viewer
Requires: xviewer

Requires: gnome-power-manager
Requires: NetworkManager-gnome >= 0.8.995
#Bluetooth configuration
Requires: blueman

%description -n cinnamon-regular
This package provides Cinnamon desktop and set
of default applications.

%prep

%files -n cinnamon-default
%files -n cinnamon-regular

%changelog
* Mon Jan 30 2023 Vladimir Didenko <cow@altlinux.org> 5.6.0-alt1
- version bump
- cinnamon-minimal moved to cinnamon-package

* Wed Mar 17 2022 Vladimir Didenko <cow@altlinux.org> 5.2.0-alt1
- version bump
- replace blueberry by blueman

* Mon Jun 1 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt4
- move pulseaudio from cinnamon-default to cinnamon-regular since
  it is not mandatory dependency

* Sat May 16 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt3
- restore nemo-share

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt2
- remove nemo-share

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- bump version

* Mon Nov 25 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- bump version
- replace xplayer by celluloid

* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 4.2.0-alt4
- remove firefox, thunderbird, pidgin
- remove gconf-editor
- remove gnome-music

* Fri Aug 16 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt3
- remove brasero

* Tue Jul 16 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt2
- add dependency on xapps-icons (closes: #36996)

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- bump version

* Wed Nov 28 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- add yelp to cinnamon-default (closes: #35658)
- bump version

* Mon Mar 26 2018 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt2
- add nemo-fileroller to cinnamon-regular (closes: #34711)

* Mon Sep 4 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- switch to slick-greeter

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- new requirements for cinnamon 3.2
- switch to xapps

* Wed Oct 21 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Sep 8 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt3
- add gnome-backgrounds to requirements (closes: #31262)

* Wed Jul 8 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- add gvfs-utils to requirements (required by xdg-open)

* Wed May 20 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Mar 27 2015 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt4
- add dependency on blueberry for bluetooth configuration

* Wed Feb 25 2015 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt3
- add dependency on metacity-theme-adwaita

* Mon Dec 29 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt2
- add gucharmap as dependency

* Wed Nov 5 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Thu Oct 23 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- 2.3.0
- replace rhythmbox by gnome-music

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt2
- remove gnome-control-center from deps

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0
- added nemo-share

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt2
- rebuild for GNOME-3.10

* Tue Sep 17 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue May 28 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt2
- replace gdm by lightdm

* Fri May 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0
- added dependency to cinnamon-control-center
- replace gnome-screensaver by cinnamon-screensaver

* Tue Jan 28 2013 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt5
- added dependency to fontconfig-infinality

* Tue Jan 28 2013 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt4
- added dependency to Cantarell font

* Tue Jan 28 2013 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt3
- deleted gnome-tweak-tool due dependency to gnome-shell
- added gcalctool
- renamed full package to regular - see
  http://www.altlinux.org/Desktop_Environment_Policy
- replaced gnome-mplayer by totem

* Wed Nov 21 2012 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt2
- dropped dependency to gnome menu

* Sat Nov 17 2012 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt1
- dropped fallback package: cinnamon has own fallback
- dropped sound package: moved dependencies to default package
- new full package: provides list of default applications

* Fri Apr 13 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- added fallback and sound packages to account for slava@'s feedback

* Thu Apr 12 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- initial release
