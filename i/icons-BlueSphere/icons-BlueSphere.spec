%define _name BlueSphere

Name: icons-%_name
Version: 0.3.0
Release: alt5

Summary: A set of Icons for GNOME 2 and KDE desktops by Vadim Plessky
License: LGPL
Group: Graphical desktop/GNOME
Url: http://svgicons.sourceforge.net

Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/svgicons/%_name-%version.tar.bz2

BuildArch: noarch

Conflicts: kdeartwork-extra <= 3.1.0-alt2
Requires: gnome-icon-theme >= 1.2.0

%description
An icon theme is a set of icons that share a common look and feel. The
user can then select the icon theme that they want to use, and all apps
use icons from the theme. The initial user of icon themes is the icon
field of the desktop file specification, but in the future it can have
other uses (such as mimetype icons).

%install
%__mkdir_p %buildroot%_iconsdir
%__tar -jxvf %SOURCE0 -C %buildroot%_iconsdir/

%__subst 's|\(Inherits=\).*$|\1default.gnome,hicolor,default.kde|' %buildroot%_iconsdir/%_name/index.theme
%__rm -f %buildroot%_iconsdir/%_name/index.desktop

%files
%_iconsdir/*

%changelog
* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt5
- Inherits=gnome,hicolor,default.kde

* Sun Mar 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt4
- Inherits to icons/gnome and icons/crystalsvg as a default gnome/kde icons.

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt3
- no more inherits to icons/Gnome.

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt2
- fixed index.* files.

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- First build for Sisyphus.
