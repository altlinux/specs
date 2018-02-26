Name: gwibber
Version: 3.1.90
Release: alt1.1
Summary: Microblogging client for Gnome desktop
License: GPLv2
Group: Networking/Instant messaging
Url: http://gwibber.com/

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel >= 2.5
BuildPreReq: python-module-setuptools python-module-distutils-extra
BuildRequires: intltool
BuildRequires: python-module-pygtk-devel python-module-dbus-devel python-module-pygnome-devel python-module-imaging-devel

Requires: python-module-pygnome-gconf python-module-notify python-module-pywebkitgtk python-module-simplejson python-module-egenix-mx-base python-module-feedparser python-module-pyxdg python-module-mako

Requires(post,postun): desktop-file-utils

%description
Gwibber is a status management client application for the GNOME desktop
environment. It can transmit status message updates to Twitter, Jaiku,
Facebook, and Pidgin.

%prep
%setup -q

%build
%python_build

%install
%python_install
# they created but not installed
mkdir %buildroot/%_desktopdir
install -m644 build/share/applications/* %buildroot/%_desktopdir/

%files
%doc README
%_bindir/*
%python_sitelibdir/%name/
%_datadir/%name/*
%_datadir/indicators/messages/applications/*
%_datadir/dbus-1/services/*
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.90-alt1.1
- Rebuild with Python-2.7

* Mon Sep 05 2011 Alexey Morsov <swi@altlinux.ru> 3.1.90-alt1
- new trunk version

* Fri Mar 11 2011 Alexey Morsov <swi@altlinux.ru> 2.91.91-alt1
-  initial build for sisyphus
