Name: liblensfun
Version: 0.3.2
Release: alt1.1

Summary: A library to rectifying the defects introduced by your photographic equipment
Group: System/Libraries
License: LGPLv3 and CC-BY-SA
Url: http://sourceforge.net/projects/lensfun/

Source: http://downloads.sourceforge.net/lensfun/lensfun-%version.tar.gz

BuildRequires: cmake gcc-c++ glib2-devel libpng-devel
BuildRequires: doxygen rpm-build-python3 python3-module-setuptools python3-module-docutils

%description
A library to rectifying the defects introduced by your photographic equipment.

%package devel
Summary: Development tools for programs which will use the lensfun library
Group: Development/C++
Requires: liblensfun = %version-%release

%description devel
Development tools for programs which will use the lensfun library.

%package tools
Summary: Tools for managing lensfun data
Group: Graphics
License: LGPLv3
BuildArch: noarch
Requires: %name = %version-%release

%description tools
This package contains tools to fetch lens database, updates and manage lens
adapters in lensfun.

%prep
%setup -n lensfun-%version
subst 's/rst2man/py3_rst2man.py/g' docs/CMakeLists.txt
subst 's/\t/      /' apps/lensfun-add-adapter

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DBUILD_TESTS:BOOL=OFF \
	-DBUILD_DOC:BOOL=ON

%cmake_build
%cmake_build man

%install
%cmakeinstall_std
pushd BUILD/apps/
%__python3 setup.py install --skip-build --root=%buildroot --prefix=%_prefix
popd

%files
%_libdir/%name.so.*
%_datadir/lensfun/
%doc ChangeLog README.*

%files devel
%_includedir/lensfun/
%_libdir/%name.so
%_pkgconfigdir/lensfun.pc
%doc %_datadir/doc/lensfun*/

%files tools
%_bindir/g-lensfun-update-data
%_bindir/lensfun-add-adapter
%_bindir/lensfun-update-data
%python3_sitelibdir_noarch/*
%_man1dir/*


%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0
- removed obsolete patches
- new -tools subpackage

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8
- removed old patches

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
