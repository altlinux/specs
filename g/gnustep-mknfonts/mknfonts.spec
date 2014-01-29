%set_verify_elf_method unresolved=strict

Name: gnustep-mknfonts
Version: 0.5
Release: alt2
Summary: Create nfont packages for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: https://launchpad.net/ubuntu/+source/mknfonts.tool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel libfreetype-devel

Requires: gnustep-back

%description
Create nfont packages for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lfreetype -lgnustep-base -lobjc2 -lm'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_bindir/*

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added Requires: gnustep-back

* Tue Jan 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

