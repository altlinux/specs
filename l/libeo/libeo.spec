# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.qa3.1
Name: libeo
Version: 1.3.1
#Release: alt1.qa3
Summary: EO, the Evolving Objects library
License: LGPLv2.1
Url: http://eodev.sourceforge.net
Source: EO-%version.zip
Patch: libeo-1.2.0-alt-glibc-2.16.patch
Group: Development/C++

# Automatically added by buildreq on Mon Sep 05 2011
# optimized out: cmake cmake-modules libstdc++-devel openssh-common python-base python-devel
BuildRequires: boost-devel-headers boost-python-devel ctest doxygen gcc-c++ git-core gnuplot libgomp-devel unzip

%description
EO is a templates-based, ANSI-C++ compliant evolutionary computation
library. It contains classes for almost any kind of evolutionary
computation you might come up to - at least for the ones we could think
of. It is component-based, so that if you don't find the class you need
in it, it is very easy to subclass existing abstract or concrete
classes.

%define sum EO, the Evolving Objects library

%package devel
Group: Development/C++
Summary: Development environment for %sum
Requires: %name = %EVR
%description devel
Development environment for %sum

%package -n python-module-PyEO
Group: Development/Python
Summary: Python bindings for %sum
Requires: %name = %EVR
%description -n python-module-PyEO
Python bindings for %sum

%prep
%setup -q -c
%patch -p2
# Hack openMP test to be less consuming
sed -i 's/)100/)20/g' eo/test/t-openmp.cpp
sed -i '/#include <eoFunctor.h>/a\
#include <cstdlib>
' eo/src/eoFunctorStore.cpp

%build
# TODO dynamic build

cd eo
%add_optflags -fpermissive
%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_CMAKE_TESTING=1 \
	-DENABLE_PYEO=1

cd BUILD
%make_build VERBOSE=1

%check
cd eo/BUILD
make test

%install
cd eo/BUILD
cmake -DENABLE_PYEO=1 -DLIB_DESTINATION=%_lib -DLIB_SUFFIX=64 -DCMAKE_INSTALL_PREFIX=%buildroot%prefix -P cmake_install.cmake
mkdir -p %buildroot%_libexecdir/eo
install -D lib/libPyEO.so %buildroot%python_sitelibdir/PyEO.so
mv %buildroot%_datadir/eo/[^d]* %buildroot%_libexecdir/eo/
# TODO when building shared, do not move debuginfo
%if "%prefix/lib" != "%_libdir"
mv %buildroot%prefix/lib/* %buildroot%_libdir/
%endif

%files
%doc eo/README
%exclude %_libexecdir
%exclude %_libdir/eo

%files devel
%doc %_datadir/eo/doc
%_libdir/*.a
%_libdir/pkgconfig/eo.pc
%_includedir/eo

%files -n python-module-PyEO
%python_sitelibdir/*.so

#files examples
#_libexecdir/eo/examples
#
#files test
#_libexecdir/eo/test

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.qa3.1
- (AUTO) subst_x86_64.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.1-alt1.qa3
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.3.1-alt1.qa1.1
- rebuild with boost 1.57.0

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.1-alt1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Tue Dec 30 2012 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.2
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.1
- Rebuilt with Boost 1.51.0

* Tue Jun 19 2012 Fr. Br. George <george@altlinux.ru> 1.2.0-alt2
- Fix build

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 06 2011 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build from scratch

