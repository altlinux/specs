%set_verify_elf_method unresolved=strict

Name: gnustep-VolumeControl
Version: 0.5
Release: alt5.1
Summary: Audio mixer for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/wheezy/volumecontrol.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
VolumeControl is a GNUstep program for adjusting the audio mixer on
systems that use the OSS API. It allows the sound level, left/right
speakers, muting for master, PCM, bass, and treble levels to be
controlled.

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
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt5.1
- NMU: Rebuild with libgnutls30.

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt5
- Fixed menu file (by kostyalamer@)

* Mon Feb 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

