%set_verify_elf_method unresolved=strict

Name: gnustep-SimpleAgenda
Version: 0.43
Release: alt8.1
Summary: Simple calendar and agenda application
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://coyote.octets.fr/simpleagenda/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-dbuskit-devel libical-devel libuuid-devel
BuildPreReq: gnustep-Etoile-AddressesKit-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-dbuskit gnustep-Etoile-AddressesKit
Requires: gnustep-back

%description
SimpleAgenda is a simple calendar and agenda application.

Based on libical, SimpleAgenda handles multiple local and distant
(through webcal) calendars. You can share your calendars with Mozilla
Calendar, Evolution and possibly others. It works for me but backup your
data if it's really important !

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%_includedir/libical'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.43-alt8.1
- NMU: Rebuild with libgnutls30.

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt8
- Fixed build

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt7
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt6
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt5
- Rebuilt with new gnustep-gui

* Thu Nov 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt4
- Rebuilt with new libical

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt3
- Added Requires: gnustep-dbuskit

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt1
- Initial build for Sisyphus

