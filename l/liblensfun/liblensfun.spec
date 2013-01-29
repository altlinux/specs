Name: liblensfun
Version: 0.2.6
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A library to rectifying the defects introduced by your photographic equipment
License: LGPLv3 and CC-BY-SA
Group: Graphics

Url: http://lensfun.berlios.de/
Source: http://download.berlios.de/lensfun/lensfun-%version.tar.bz2
Patch1: lensfun-0.2.5-lensdbadditions.patch
Patch3: lensfun-0.2.5-alt-debuginfo.patch
Patch4: lensfun-0.2.6-fc-cmake_LIB_SUFFIX.patch
Patch5: lensfun-0.2.6-fc-cmake_pkgconfig.patch

BuildRequires: cmake doxygen gcc-c++ glib2-devel libpng-devel python-modules

%description
A library to rectifying the defects introduced by your photographic equipment.

%package devel
Summary: Development tools for programs which will use the lensfun library
Group: Development/C
Requires: liblensfun = %version-%release

%description devel
Development tools for programs which will use the lensfun library.

%prep
%setup -n lensfun-%version
%patch1 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1

%build
%cmake -DBUILD_TESTS:BOOL=OFF
pushd BUILD
%make_build

%install
pushd BUILD
%makeinstall_std

%files
%_libdir/*.so.*
%_datadir/lensfun

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6 (ALT #28197)
- removed obsolete (fixed by upstream) patches

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt3.2
- Fixed build with libpng15

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt3.1
- Rebuilt for debuginfo

* Wed Dec 08 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt3
- Apply PLD patch that fixes bug (broken vectorization) caused SIGSEGV in ufraw.
  SSE vectorization enabled in this build.

* Mon Aug 16 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt2
- Disable SSE vectorization to avoid crashes until upstream fix this code.
- Add lens data for Nikkor 50mm F/1.8 D and Nikkor 18-105mm F/3.5-5.6.

* Fri Apr 02 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt1
- 0.2.5

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 0.2.4-alt1
- 0.2.4

* Fri Oct 09 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt5
- Added patch by Dmitry Levin to fix problematic source that was
  compiled into wrong code by gcc 4.4.

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt4
- Compile with gcc 4.3.

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt3
- Fix FTBFS with GCC 4.4.

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt2
- Remove obsolete ldconfig calls.

* Mon Oct 20 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Sep 03 2008 Victor Forsyuk <force@altlinux.org> 0.2.2b-alt2
- Package lensfun.pc.

* Fri Aug 22 2008 Victor Forsyuk <force@altlinux.org> 0.2.2b-alt1
- Initial build.
