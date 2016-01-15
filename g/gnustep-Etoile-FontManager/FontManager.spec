%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-FontManager
Version: 0.1
Release: alt2.svn20121130.1
Summary: App for the purpose of (guess what) managing fonts
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/FontManager.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator

Requires: gnustep-back

%description
Font Manager is an app for the purpose of (guess what) managing fonts.
It can currently show you your installed fonts and show samples of them.
Planned features are disabling/enabling fonts and easy installation of
fonts (including previewing of uninstalled fonts).

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=FontManager

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=FontManager

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog COPYING README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt2.svn20121130.1
- NMU: Rebuild with libgnutls30.

* Mon Mar 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.svn20121130
- Added menu file (thnx kostyalamer@)

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20121130
- Initial build for Sisyphus

