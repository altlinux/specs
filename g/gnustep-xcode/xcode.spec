Name: gnustep-xcode
Version: 0.1
Release: alt3.svn20121015
Summary: The XCLib framework is used to parse and process xcodeproj files
License: GPL
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/xcode/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel /proc

%description
The XCLib framework is used to parse and process xcodeproj files so that
they can be built by a tool or an IDE using this framework.

%package -n lib%name
Summary: Shared libraries of XCLib framework
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
The XCLib framework is used to parse and process xcodeproj files so that
they can be built by a tool or an IDE using this framework.

This package contains shared libraries of XCLib framework.

%package -n lib%name-devel
Summary: Development files of XCLib framework
Group: Development/Objective-C
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The XCLib framework is used to parse and process xcodeproj files so that
they can be built by a tool or an IDE using this framework.

This package contains development files of XCLib framework.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.svn20121015
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.svn20121015
- Built with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20121015
- Initial build for Sisyphus

