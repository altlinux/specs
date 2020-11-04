%set_verify_elf_method unresolved=strict

Name: gnustep-Wrapper
Version: 0.1.0
Release: alt7
Summary: Create GNUstep app-wrappers of non-GNUstep applications
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.freshports.org/deskutils/gnustep-wrapper
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back gnustep-gworkspace

%description
GNUstepWrapper provides an easy way to create GNUstep app-wrappers of
non-GNUstep applications. It is the most useful in conjunction with
Enrico Sersale's GWorkspace environment.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

rm -f %buildroot%_libdir/*.so

%files
%doc AUTHORS NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%_libdir/*.so.*
%_menudir/*

%post
make_services

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt7
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt6
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt5.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt5
- Added menu file (thnx kostyalamer@)

* Wed Feb 26 2014 Eugeny A. Rostovtsev <real at altlinux.org> 0.1.0-alt4
- Added postinstall and Requires: gnustep-gworkspace

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

