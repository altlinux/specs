%define upstreamname lxmenu-data
Name: lxde-%upstreamname
Version: 0.1
Release: alt4

Summary: freedesktop.org menu for LXDE
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
Packager: LXDE Development Team <lxde at packages.altlinux.org>
BuildArch: noarch

Source: %upstreamname-%version.tar.gz

Patch1: menu-layout.patch

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: intltool
Provides: lxde-freedesktop-menu

%description
This package provides files required to build freedesktop.org 
menu spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

lxmenu-data package is required by lxpanel and lxlauncher.

%prep
%setup -n %upstreamname-%version
%patch1 -p2

%build
%configure

%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README TODO
%_datadir/desktop-directories/*
%_sysconfdir/xdg/menus/*

%changelog
* Fri Mar 11 2011 Radik Usupov <radik@altlinux.org> 0.1-alt4
- added virtual provide for further transition to global freedesktop menu

* Sun Oct 03 2010 Radik Usupov <radik@altlinux.org> 0.1-alt3
- change packager
- update upstream
- package is now noarch

* Mon Dec 28 2009 Mykola Grechukh <gns@altlinux.ru> 0.1-alt2
- PackageManager removed from DesktopSettings (#22280)

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
