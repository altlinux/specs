%set_verify_elf_method unresolved=strict

Name: gnustep-PlopFolio
Version: 0.1.0
Release: alt6
Summary: Personal dashboard for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/wheezy/plopfolio.app
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu
Patch1: gnustep-base-1.27-includes.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
This is a free replacement of Serence's proprietary KlipFolio
application. PlopFolio supports Klips available from KlipFarm
(http://klipfarm.com). PlopFolio is developed using the Objective-C
language and works well with GNUstep (on GNU/Linux, FreeBSD, and more)
and Cocoa on Mac OS X.

%prep
%setup
%patch1 -p2

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
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

