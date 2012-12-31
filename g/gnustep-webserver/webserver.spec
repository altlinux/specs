%set_verify_elf_method unresolved=strict

Name: gnustep-webserver
Version: 1.4.8
Release: alt2.git20121031
Summary: Embedded webserver library
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-webserver.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-performance-devel /proc

%description
The GNUstep embedded webserver library.

%package -n lib%name
Summary: Embedded webserver library
Group: System/Libraries

%description -n lib%name
The GNUstep embedded webserver library.

%package -n lib%name-devel
Summary: Development files of embedded webserver library
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep embedded webserver library.

This package contains development files of embedded webserver library.

%package -n lib%name-devel-doc
Summary: Documentation for embedded webserver library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The GNUstep embedded webserver library.

This package contains development documentation for embedded webserver
library.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/GNUstep

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt2.git20121031
- Rebuilt with libobjc2 instead of libobjc

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt1.git20121031
- Initial build for Sisyphus

