%set_verify_elf_method unresolved=strict

Name: gnustep-palettes
Version: r20982
Release: alt4
Summary: GNUstep palettes
License: Free
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-palettes
Packager: Andrey Cherepanov <cas@altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/palettes/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-gorm-devel

Requires: gnustep-gorm
Requires: gnustep-back

%description
GNUstep palettes.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build -C Boxes \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lGorm'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std -C Boxes GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%_libdir/GNUstep

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> r20982-alt4
- Build without libgnustep-objc2-devel.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r20982-alt3.svn20050327
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r20982-alt2.svn20050327
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r20982-alt1.git20050327
- Initial build for Sisyphus

