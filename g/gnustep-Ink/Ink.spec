%set_verify_elf_method unresolved=strict

Name: gnustep-Ink
Version: 0.1
Release: alt4.svn20121003.1
Summary: Ink is the GNUstep editor
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Ink.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/tests/examples/trunk/gui/Ink/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back
Conflicts: gnustep-examples

%description
Ink is a basic editor for rtf(d) and plain text.

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
%doc ChangeLog *.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.svn20121003.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.svn20121003
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.svn20121003
- Added menu file (thnx kostyalamer@)

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.svn20121003
- Added explicit conflict with gnustep-examples

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20121003
- Initial build for Sisyphus

