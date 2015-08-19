
Name: roxterm
Version: 3.1.4
Release: alt2

Summary: A tabbed, vte- (GTK+) based terminal emulator
License: GPL
Group: Development/Python

Url: http://sourceforge.net/projects/roxterm/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
BuildPreReq: python-module-lockfile gcc4.7-c++
BuildPreReq: git-core gnupg
BuildPreReq: docbook-xsl po4a ImageMagick-tools 
BuildPreReq: itstool libgtk+3-devel
BuildPreReq: libvte3-devel libICE-devel
BuildPreReq: libSM-devel librsvg-devel
BuildPreReq: libdbus-devel libdbus-glib-devel
BuildPreReq: librsvg

%description
A tabbed, vte- (GTK+) based terminal emulator providing advanced features such as multiple tabs with a small footprint

%prep
%setup

%build
%__python ./mscript.py configure PREFIX=/usr
%__python ./mscript.py build

%install
%__python ./mscript.py install DESTDIR=%buildroot
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-config
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_docdir/roxterm/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_mandir/*/man1/*
%_man1dir/*
%_datadir/roxterm/*

%changelog
* Tue Aug 18 2015 Konstantin Artyushkin <akv@altlinux.org> 3.1.4-alt2
- initial build for ALT Linux Sisyphus

