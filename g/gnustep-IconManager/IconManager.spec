%set_verify_elf_method unresolved=strict

Name: gnustep-IconManager
Version: 0.3
Release: alt3
Summary: IconManager is a tool to handle AppIcons and MiniWindows 
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/IconManager.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
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
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc README INSTALL
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Rebuilt with new gnustep-gui

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

