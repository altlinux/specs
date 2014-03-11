%set_verify_elf_method unresolved=strict

Name: gnustep-CDPlayer
Version: 0.5.1
Release: alt6
Summary: Small CD Audio Player for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: libcdaudio-devel gnustep-gui-devel
BuildPreReq: gnustep-systempreferences-devel

Requires: gnustep-cddb.bundle
Requires: gnustep-systempreferences
Requires: gnustep-back

%description
CDPlayer.app is a small CD Audio Player for GNUstep. This application is
only tested on Linux/GNUstep.

CDPlayer is useful only if your CD drive is directly connected with your
sound card. It cannot cope with SATA drives where it is necessary to
read the digital data from the disc and then convert it to audio output.

%package devel
Summary: Development files of CDPlayer
Group: Development/Objective-C
BuildArch: noarch
Requires: %name = %EVR

%description devel
CDPlayer.app is a small CD Audio Player for GNUstep. This application is
only tested on Linux/GNUstep.

CDPlayer is useful only if your CD drive is directly connected with your
sound card. It cannot cope with SATA drives where it is necessary to
read the digital data from the disc and then convert it to audio output.

This package contains development files of CDPlayer.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	prefs=sysprefs \
	CONFIG_SYSTEM_LIBS='-lcdaudio'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	prefs=sysprefs

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc CHANGELOG CREDITS README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files devel
%_includedir/*

%changelog
* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt6
- Fixed menu file (by kostyalamer@)

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt5
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt4
- Added Requires: gnustep-systempreferences and Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added menu file (thnx kostyalamer@)

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

