%set_verify_elf_method unresolved=strict

Name: gnustep-thematic
Version: 0.2
Release: alt3.svn20140112.1
Summary: Theme editor for GNUstep
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-thematic
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/apps/thematic/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-gorm
Requires: gnustep-projectcenter
Requires: gnustep-back

%description
Thematic.app is a theme editor for GNUstep.

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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt3.svn20140112.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3.svn20140112
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.svn20140112
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20140112
- New snapshot

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20131105
- Initial build for Sisyphus

