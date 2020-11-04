%set_verify_elf_method unresolved=strict

Name: gnustep-coreimage
Version: r36695
Release: alt4
Summary: GNUstep CoreImage
License: LGPLv2+
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-coreimage
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/gnustep/gnustep-coreimage.git
Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
GNUstep CoreImage.

%package -n lib%name
Summary: Shared libraries of GNUstep CoreImage
Group: System/Libraries

%description -n lib%name
Shared libraries of GNUstep CoreImage.

%package -n lib%name-devel
Summary: Development files of GNUstep CoreImage
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files of GNUstep CoreImage.

%prep
%setup
%patch1 -p1

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> r36695-alt4
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> r36695-alt3
- Build without libgnustep-objc2-devel.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r36695-alt2.git20130603
- Built with clang

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r36695-alt1.git20130603
- Initial build for Sisyphus

