%set_verify_elf_method unresolved=strict

Name: gnustep-Chess
Version: 33
Release: alt2.cvs20140127
Summary: Chess game
License: GPL
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/ported-apps/Games/Chess
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-c++
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Chess game.

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
%doc COPYING
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 33-alt2.cvs20140127
- Added Requires: gnustep-back

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 33-alt1.cvs20140127
- Initial build for Sisyphus

