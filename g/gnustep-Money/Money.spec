%set_verify_elf_method unresolved=strict

Name: gnustep-Money
Version: 0.1
Release: alt5.1
Summary: The Document-base application is a kind of special, but commonly used applications
License: Free
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gstutorial/en/ch13.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
The Document-base application is a kind of special, but commonly used
applications. You can open multiple documents, edit and save each of
them. Most text editors belong to the document-base application.

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
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt5.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added menu file (thnx kostyalamer@)

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Fixed description

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

