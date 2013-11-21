%set_verify_elf_method unresolved=strict

Name: gnustep-SimpleAgenda
Version: 0.43
Release: alt4
Summary: Simple calendar and agenda application
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-dbuskit-devel libical-devel libuuid-devel
BuildPreReq: gnustep-AddressManager-devel

Requires: gnustep-dbuskit

%description
SimpleAgenda is a simple calendar and agenda application.

Based on libical, SimpleAgenda handles multiple local and distant
(through webcal) calendars. You can share your calendars with Mozilla
Calendar, Evolution and possibly others. It works for me but backup your
data if it's really important !

%prep
%setup

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
%autoreconf
%configure

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -I%_includedir/libical'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Nov 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt4
- Rebuilt with new libical

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt3
- Added Requires: gnustep-dbuskit

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt1
- Initial build for Sisyphus

