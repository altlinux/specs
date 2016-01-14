%set_verify_elf_method unresolved=strict

Name: gnustep-FisicaLab
Version: 0.3.3
Release: alt3.1
Summary: FisicaLab.app is an educational application to solve physics problems
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnu.org/software/fisicalab/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: libgsl-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
FisicaLab consist in a chalkboard to set the problems and a palette with
elements like mobiles, blocks, forces,... that let the user set the
problems.

FisicaLab can solve the fallowing problems:
* Kinematics of particles in 2D.
* Circular kinematics of particles in 2D.
* Static of particles in 2D.
* Static of rigid bodies in 2D.
* Dynamics of particles in 2D.
* Circular dynamics of particles in 2D.
* Heat, calorimetry, ideal gas and expansion.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

export CC=clang CPP="clang -E"
%autoreconf
%configure

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -Dp -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt3.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Version 0.3.3

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Version 0.3.2

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

