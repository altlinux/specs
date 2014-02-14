%set_verify_elf_method unresolved=strict

Name: gnustep-GSBench
Version: 0.5.2
Release: alt4
Summary: Benchmarking tool for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GSBench.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-objc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-projectcenter-devel

Requires: gnustep-projectcenter
Requires: gnustep-back

%description
A benchmarking tool for GNUstep, originated from NXBench.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

export CC=gcc
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	INTERNAL_OBJCFLAGS="-fobjc-exceptions -DUSER_NATIVE_OBJC_EXCEPTIONS %optflags_shared" \
	USE_NONFRAGILE_ABI=no
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt4
- Built with gcc

* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt2
- Added Requires: gnustep-projectcenter and Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

