Name:		focuswriter
Version:	1.6.0
Release:	alt2
Summary:	FocusWriter is a fullscreen, distraction-free word processor
License:	GPLv3
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Text tools
Url:		http://gottcode.org/focuswriter/
Source0:	http://gottcode.org/focuswriter/%name-%version-src.tar.bz2

# Automatically added by buildreq on Sat Aug 27 2016 (-bi)
# optimized out: elfutils gcc-c++ libGL-devel libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-widgets libstdc++-devel pkg-config python-base python-modules qt5-base-devel xz
BuildRequires: libhunspell-devel qt5-multimedia-devel zlib-devel

%description
FocusWriter is a fullscreen, distraction-free word processor
designed to immerse you as much as possible in your work.
The program autosaves your progress, and reloads the last files
you had open to make it easy to jump back in during your next
writing session, and has many other features that make it such
that only one thing matters: your writing.

%prep
%setup

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/appdata/%name.*
%_man1dir/%name.*
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt2
- fix BuildRequires for Qt5

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sat Jun 25 2016 Motsyo Gennadi <drool@altlinux.ru> 1.5.6-alt1
- 1.5.6

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Sun Jun 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Sun Jun 29 2014 Motsyo Gennadi <drool@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Apr 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Fri Mar 28 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Fri May 31 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon Apr 08 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Mar 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Nov 29 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Sep 23 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.5.1-alt1
- 1.3.5.1

* Sat Nov 05 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.4.1-alt1
- 1.3.4.1

* Tue Mar 22 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.2.1-alt1
- initial build for ALT Linux
