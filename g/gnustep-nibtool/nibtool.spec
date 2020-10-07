%set_verify_elf_method unresolved=strict

Name: gnustep-nibtool
Version: 0.1
Release: alt2
Summary: GNUstep nibtool
License: GPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

# http://svn.gna.org/svn/gnustep/apps/nibtool/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-gorm-devel

Requires: gnustep-gorm

%description
GNUstep nibtool.

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

%files
%_bindir/*

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.svn20100602.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20100602
- Fixed build

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20100602
- Initial build for Sisyphus

