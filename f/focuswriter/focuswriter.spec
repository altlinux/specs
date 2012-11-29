Name:		focuswriter
Version:	1.4.1
Release:	alt1
Summary:	FocusWriter is a fullscreen, distraction-free word processor
License:	GPLv3
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Text tools
Url:		http://gottcode.org/focuswriter/
Source0:	http://gottcode.org/focuswriter/%name-%version-src.tar.bz2

BuildRequires: gcc-c++ libenchant-devel libzip-devel libqt4-devel

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
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
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
