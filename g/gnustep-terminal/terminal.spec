%set_verify_elf_method unresolved=strict

Name: gnustep-terminal
Version: 0.9.9
Release: alt1
Summary: Terminal emulator for GNUstep
License: GPL-2.0
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/terminal/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu
Patch1: check-write-return-value.patch
Patch2: fix-int-to-pointer-cast.patch
Patch3: gcc-10.patch

BuildPreReq: gnustep-make-devel /proc
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
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
* Sat Jan 02 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt1
- New version.
- Apply patches from Debian.

* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt8
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt7
- Build without libgnustep-objc2-devel.

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

