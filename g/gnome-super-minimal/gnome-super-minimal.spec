%define ver_major 45

Name: gnome-super-minimal
Version: %ver_major.0
Release: alt1

Summary: GNOME 3 Desktop very minimal installer
License: GPL-3.0+
Group: Graphical desktop/GNOME

Conflicts: gnome3-minimal

BuildArch: noarch

# GNOME Desktop Core
Requires: gnome-session-wayland
Requires: gnome-session-xsession

Requires: pipewire wireplumber
Requires: gnome-control-center
Requires: xorg-drv-libinput
Requires: gnome-shell
Requires: gnome-shell-extensions
Requires: gnome-browser-connector

# default font
Requires: fonts-otf-abattis-cantarell
# backgrounds
Requires: gnome-backgrounds

# Help browser
Requires: yelp

# Applications
## Default file manager
Requires: nautilus
Requires: nautilus-share samba-usershares

# Look & Feel
## Default themes
Requires: gnome-icon-theme
Requires: gnome-icon-theme-symbolic
Requires: gnome-themes-extra
#Requires: libgtk3-engine-adwaita
Requires: libgtk2-engine-adwaita

# And, of course, the documentation
Requires: gnome-user-docs

%description
A virtual package for GNOME Desktop installation without non-important applications.
Suitable for building distributions.
The idea is to use a minimum number of metapackages in the system to protect system breakdowns from apt-get autoremove 
and to allow the removal of applications that the user does not need.

%files

%changelog
* Thu Oct 12 2023 Roman Alifanov <ximper@altlinux.org> 45.0-alt1
- replace gnome-session to gnome-session-wayland and gnome-session-xsession

* Wed Aug 09 2023 Roman Alifanov <ximper@altlinux.org> 44.0-alt1
- Initial build for Sisyphus.
