Name: gnustep-performance
Version: 0.4.0
Release: alt2.svn20131105
Summary: The GNUstep Performance library
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/performance/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
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
%doc ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/GNUstep

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.svn20131105
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.svn20131105
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20130821
- Version 0.4.0

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2.git20130304
- New snapshot

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2.git20130118
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2.git20120111
- Rebuilt with libobjc2 instead of libobjc

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20120111
- Initial build for Sisyphus

