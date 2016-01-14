%set_verify_elf_method unresolved=strict

Name: gnustep-TimeMon
Version: 4.1
Release: alt6.svn20130303.1
Summary: CPU time usage monitor
License: Permission to use, copy, modify, and distribute without fee
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/timemon/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
TimeMon gives a graphical representation of where the CPU cycles are
going. It's coarse, but better than nothing. The best feature is that it
runs in an icon on your dock, so that you never lose it.

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
%doc ChangeLog README.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 4.1-alt6.svn20130303.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt6.svn20130303
- Snapshot from svn

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt6
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt5
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt4
- Rebuilt with new gnustep-gui

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt3
- Fixed menu file by kostyalamer@

* Fri Mar 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Initial build for Sisyphus

