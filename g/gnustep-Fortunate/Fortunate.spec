%set_verify_elf_method unresolved=strict

Name: gnustep-Fortunate
Version: 3.0
Release: alt4.1
Summary: Fortunate displays a quotation in a window
License: Public domain / BSD
Group: Graphical desktop/GNUstep
Url: http://www.orange-carb.org/~csaldanh/software.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-pbxbuild

Requires: fortune
Requires: gnustep-back

%description
Fortunate displays a quotation in a window. Fortunate is a
Cocoa/Objective-C graphical front-end to the command-line BSD fortune
(included) which, since the dawn of time, has been providing countless
seconds of fun each time a user logs in.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

pbxbuild -p Fortunate3.0.pbproj -g

%make_build -C pbxbuild \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std -C pbxbuild GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc CHANGES README.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt4
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

