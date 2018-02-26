Name:		qtfm
Version:	5.5
Release:	alt1
Summary:	qtFM is a small, lightweight file manager
License:	GPLv2
Group:		File tools
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.qtfm.org/
Source0:	http://www.qtfm.org/%name-%version.tar.gz

BuildRequires: /usr/bin/convert gcc-c++ libmagic-devel libqt4-devel

%description
qtFM is a small, lightweight file manager for Linux desktops based on pure Qt
and works great with minimal desktop environments like Openbox.

Features:

 - lightweight, pure Qt, no kde libraries or other dependencies
 - full theme and mime filetype icon integration
 - tree, bookmarks, list, icon, detail and thumbnail views
 - customizable interface, rearrange views and toolbars to suit
 - powerful custom command system for user defined actions
 - customizable key bindings for built-in and custom actions
 - drag & drop functionality
 - tabs

%prep
%setup

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir}
install -Dp -m 0644 images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 images/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 images/%name.png %buildroot%_miconsdir/%name.png

%files
%doc CHANGELOG COPYING README
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 5.5-alt1
- 5.5

* Fri Dec 16 2011 Motsyo Gennadi <drool@altlinux.ru> 5.3-alt1
- 5.3

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 5.2-alt1
- initial build for ALT Linux
