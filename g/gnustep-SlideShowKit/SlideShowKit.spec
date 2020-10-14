%set_verify_elf_method unresolved=strict

Name: gnustep-SlideShowKit
Version: 20041011
Release: alt3
Summary: A small kit to include slideshow in your application
License: Free
Group: Graphical desktop/GNUstep
Url: http://home.gna.org/gsimageapps/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: clang-devel gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
A small kit to include slideshow in your application.

%package -n lib%name
Summary: Shared libraries of SlideShowKit
Group: System/Libraries

%description -n lib%name
A small kit to include slideshow in your application.

This package contains shared libraries of SlideShowKit.

%package -n lib%name-devel
Summary: Development files of SlideShowKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
A small kit to include slideshow in your application.

This package contains development files of SlideShowKit.

%prep
%setup
%patch1 -p2

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 20041011-alt3
- Build without libgnustep-objc2-devel.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041011-alt2
- Built with clang

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041011-alt1
- Initial build for Sisyphus

