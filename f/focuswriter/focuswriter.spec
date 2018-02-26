Name:		focuswriter
Version:	1.3.6
Release:	alt1
Summary:	FocusWriter is a fullscreen, distraction-free word processor
License:	GPLv3
Group:		Text tools
Url:		http://gottcode.org/focuswriter/
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://gottcode.org/focuswriter/%name-%version-src.tar.bz2

# Automatically added by buildreq on Tue Mar 22 2011 (-bi)
BuildRequires: gcc-c++ libao-devel libhunspell-devel libqt4-devel libzip-devel

%description
FocusWriter is a fullscreen, distraction-free word processor
designed to immerse you as much as possible in your work.
The program autosaves your progress, and reloads the last files
you had open to make it easy to jump back in during your next
writing session, and has many other features that make it such
that only one thing matters: your writing.

%package -n %name-dictionaries
Summary:	Dictionaries for FocusWriter
Group:		Text tools
BuildArch:	noarch
Requires:	%name

%description -n %name-dictionaries
Spelling and morphological dictionary for FocusWriter
from OpenOffice.org

%prep
%setup

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
cp -a resources/dict %buildroot%_datadir/%name/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%exclude %_datadir/%name/dict
%_iconsdir/hicolor/*/apps/*

%files -n %name-dictionaries
%_datadir/%name/dict

%changelog
* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.5.1-alt1
- 1.3.5.1

* Sat Nov 05 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.4.1-alt1
- 1.3.4.1

* Tue Mar 22 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.2.1-alt1
- initial build for ALT Linux
