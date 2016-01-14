%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ModelBuilder
Version: r6592
Release: alt2.git20101126.1
Summary: Etoile's Model Builder
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/ModelBuilder.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-EtoileUI-devel gnustep-Etoile-IconKit-devel
BuildPreReq: gnustep-Etoile-EtoileSerialize-devel

Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-EtoileUI gnustep-Etoile-IconKit
Requires: gnustep-Etoile-EtoileSerialize

%description
Etoile's Model Builder.

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
	PROJECT_NAME=ModelBuilder

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ModelBuilder

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> r6592-alt2.git20101126.1
- NMU: Rebuild with libgnutls30.

* Mon Mar 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r6592-alt2.git20101126
- Added menu file (thnx kostyalamer@)

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r6592-alt1.git20101126
- Initial build for Sisyphus

