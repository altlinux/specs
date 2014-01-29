%set_verify_elf_method unresolved=strict

Name: gnustep-LuserNET
Version: 0.4.2
Release: alt2
Summary: News reader for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/jessie/lusernet.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Pantomime-devel

Requires: gnustep-Pantomime
Requires: gnustep-back

%description
LuserNET is an NNTP based news reader for GNUstep. Although it's at an
early version, it's already quite usable. The following features are
available:

* Coloring of messages based on quoting depth.
* Background read-ahead.
* Intelligent scrolling.
* Handles multiple servers.
* Completely asynchronous.
* Good MIME conformance and handling.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc Changes README
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

