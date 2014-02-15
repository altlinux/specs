%set_verify_elf_method unresolved=strict

Name: gnustep-Mixer
Version: 1.8.0
Release: alt5
Summary: Mixer application designed for WindowMaker
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/squeeze/gnustep/mixer.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-c++
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libX11-devel libXpm-devel libXext-devel

Requires: gnustep-back
Requires: ossp

%description
There's nothing in the program that makes it *require* WindowMaker,
except maybe the look. Mixer.app is a mixer utility for Linux systems.
Requires /dev/mixer to work. Provides three customizable controls on a
tiny 64x64 app.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README
%_bindir/*
%_menudir/*

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt5
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt4
- Requires: ossp
- Added menu file (thnx kostyalamer@)

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt3
- Disabled use of /dev/sound/mixer
- Added script for run program

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Added Requires: alsa-oss (thnx mike@)

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

