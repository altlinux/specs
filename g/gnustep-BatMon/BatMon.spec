%set_verify_elf_method unresolved=strict

Name: gnustep-BatMon
Version: 0.7
Release: alt4.1
Summary: Battery monitor for laptops
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/batmon/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Battery Monitor is a battery monitor for laptops. It displays the
current status of the battery (charge/discharge and energy level) as
well as some information about the general health of the cell.

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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt4.1
- NMU: Rebuild with libgnutls30.

* Wed Mar 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4
- Fixed menu file

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added menu file (thnx kostyalamer@)

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

