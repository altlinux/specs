%set_verify_elf_method unresolved=strict

Name: gnustep-Innerspace
Version: 0.2.0
Release: alt2
Summary: Innerspace is a screensaver
License: GPL
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/innerspace/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libX11-devel

Requires: gnustep-back

%description
Innerspace is a screensaver which is compatible with BackSpace from the
NeXTSTEP era. It can, with few changes to the module, run old BackSpace
modules.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

