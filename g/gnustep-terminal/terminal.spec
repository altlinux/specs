%set_verify_elf_method unresolved=strict

Name: gnustep-terminal
Version: 0.9.8
Release: alt6.1
Summary: Terminal emulator for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/terminal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Terminal is terminal emulator for GNUstep. Multiple windows, scroll
buffer and all the expected features are present. Furthermore it sports
terminal services.

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
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt6.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt6
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt5
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt4
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt3
- Set UTF-8 as default encoding

* Sun Jan 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt2
- Added menu file (thnx kostyalamer@)

* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

