%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-Vindaloo
Version: 0.2
Release: alt3.svn20130128.1
Summary: A PDF reader
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Services/User/Vindaloo/
Source: %name-%version.tar
Source1: gnustep-Vindaloo.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-PopplerKit-devel
BuildPreReq: gnustep-Etoile-IconKit-devel

Requires: gnustep-back gnustep-PopplerKit gnustep-Etoile-IconKit

%description
A PDF viewer using PopplerKit.

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
	PROJECT_NAME=Vindaloo

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=Vindaloo

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/gnustep-Vindaloo

%files
%doc ChangeLog README docs/*
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt3.svn20130128.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3.svn20130128
- Don't break when zoom factor is 0

* Fri Mar 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.svn20130128
- Fixed run without document

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20130128
- Initial build for Sisyphus

