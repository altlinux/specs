#set_verify_elf_method unresolved=strict

Name: gnustep-MP3ToWav
Version: 0.4.1
Release: alt5
Summary: MP3ToWav plugin for Burn.app
License: Free
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libao-devel libmad-devel gnustep-Burn-devel

Requires: gnustep-Burn
Requires: gnustep-back

%description
MP3ToWav plugin for Burn.app.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%_includedir/Burn'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

%files
%doc README
%_libdir/GNUstep

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt5
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt4
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt3.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added Requires: gnustep-Burn and Requires: gnustep-back

* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

