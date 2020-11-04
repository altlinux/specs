%set_verify_elf_method unresolved=strict

Name: gnustep-IconManager
Version: 0.3
Release: alt7
Summary: IconManager is a tool to handle AppIcons and MiniWindows 
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/IconManager.app
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
This tool is useful on desktops that can't handle GNUstep AppIcons and
MiniWindows. This package comes with an app called IMPreferences to
configure the tool.

Features:
This tool let you
* Set the size of the icons
* The position of icons and
* How these will be added.

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
%doc README INSTALL
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.3-alt7
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.3-alt6
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt5.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt5
- Built with clang

* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Rebuilt with new gnustep-gui

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

