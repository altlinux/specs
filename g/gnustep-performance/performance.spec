Name: gnustep-performance
Version: 0.3.2
Release: alt1.git20120111
Summary: The GNUstep Performance library
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-performance.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel /proc

%description
The GNUstep performance library.

%package -n lib%name
Summary: The GNUstep Performance library
Group: System/Libraries

%description -n lib%name
The GNUstep performance library.

%package -n lib%name-devel
Summary: Development files of the GNUstep Performance library
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep performance library.

This package contains development files of the GNUstep Performance
library.

%package -n lib%name-devel-doc
Summary: Documentation for the GNUstep Performance library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The GNUstep performance library.

This package contains development documentation for the GNUstep
Performance library.

%prep
%setup

sed -i 's|objc/|objc2|g' $(find ./ -type f)

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc'
 
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
* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20120111
- Initial build for Sisyphus

