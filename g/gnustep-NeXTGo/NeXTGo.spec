%set_verify_elf_method unresolved=strict

Name: gnustep-NeXTGo
Version: 3.0
Release: alt4
Summary: NeXTGo is the classic Go game
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/nextgo/index.html
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu
Patch1: link-libs.patch

BuildPreReq: clang-devel gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
NeXTGo is the classic Go game originally written for the OPENSTEP/Mach
environment.

%prep
%setup
%patch1 -p2

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc FAQ README* NeXTGoHelp.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.0-alt4
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt3.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3
- Built with clang
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

