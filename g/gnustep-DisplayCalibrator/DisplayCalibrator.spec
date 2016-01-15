%set_verify_elf_method unresolved=strict

Name: gnustep-DisplayCalibrator
Version: 0.7
Release: alt5.1
Summary: Gamma calibration for GNUstep
License: Free
Group: Graphical desktop/GNUstep
Url: http://packages.ubuntu.com/ru/lucid/displaycalibrator.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
DisplayCalibrator is a GNUstep application to calibrate the gamma of
your display.

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
%doc readme
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt5.1
- NMU: Rebuild with libgnutls30.

* Wed Mar 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt5
- Fixed

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

