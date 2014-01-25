%set_verify_elf_method unresolved=strict

Name: gnustep-gscrypt
Version: r31301
Release: alt1.git20100910
Summary: GNUstep GSCrypt Library
License: GPLv3
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-gscrypt
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gscrypt.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libpam0-devel

%description
GNUstep GSCrypt Library.

%package -n lib%name
Summary: GNUstep GSCrypt Library
Group: System/Libraries

%description -n lib%name
GNUstep GSCrypt Library.

%package -n lib%name-devel
Summary: Development files of GNUstep GSCrypt Library
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
GNUstep GSCrypt Library.

This package contains development files of GNUstep GSCrypt Library.

%prep
%setup

mkdir gscrypt
cp *.h gscrypt/

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lpam -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files -n lib%name
%doc ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31301-alt1.git20100910
- Initial build for Sisyphus

