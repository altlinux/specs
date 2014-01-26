%set_verify_elf_method unresolved=strict

Name: gnustep-SMBKit
Version: 20140126
Release: alt1.cvs20140126
Summary: GNUstep SMBKit
License: LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://savannah.gnu.org/projects/gnustep/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libsmbclient-devel

%description
GNUstep SMBKit.

%package -n lib%name
Summary: Shared libraries of GNUstep SMBKit
Group: System/Libraries

%description -n lib%name
Shared libraries of GNUstep SMBKit.

%package -n lib%name-devel
Summary: Development files of GNUstep SMBKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files of GNUstep SMBKit.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/samba-4.0' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Jan 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140126-alt1.cvs20140126
- Initial build for Sisyphus

