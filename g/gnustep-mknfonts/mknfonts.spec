%set_verify_elf_method unresolved=strict

Name: gnustep-mknfonts
Version: 0.5
Release: alt4
Summary: Create nfont packages for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: https://launchpad.net/ubuntu/+source/mknfonts.tool/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-base-devel libfreetype-devel

Requires: gnustep-back

%description
Create nfont packages for GNUstep.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lfreetype -lgnustep-base'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%_bindir/*

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.5-alt4
- Build without libgnustep-objc2-devel.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added Requires: gnustep-back

* Tue Jan 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

