%define oname shiboken
Name: %oname-py3
Version: 1.2.2
Release: alt3.git20140422.2.1
Summary: Generates bindings for C++ libraries using CPython source code (Python 3)
License: GPLv2, LGPLv2.1
Group: Development/KDE and QT
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Patch1: %name-%version-alt-gcc6.patch

# Updated build system %%__*python3* macros are in 0.1.9.2.
BuildRequires(pre): rpm-build-python3 >= 0.1.9.2
BuildPreReq: python3-devel
BuildPreReq: cmake libqt4-devel gcc-c++ libgeneratorrunner-devel
BuildPreReq: phonon-devel generatorrunner qt4-designer xml-utils
BuildPreReq: python3-module-sphinx-devel xsltproc python3-devel
BuildPreReq: libxml2-devel libxslt-devel libqt4-assistant-devel
BuildPreReq: python3-module-distribute

Requires: lib%name = %version-%release
Conflicts: %oname

%description
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

%package -n lib%name
Summary: Shared libraries of Shiboken (Python 3)
Group: System/Libraries

%description -n lib%name
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

This package contains shared libraries of Shiboken.

%package -n lib%name-devel
Summary: Development files of Shiboken (Python 3)
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: lib%oname-devel

%description -n lib%name-devel
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

This package contains development files of Shiboken.

%package -n python3-module-%oname
Summary: Python module of Shiboken (Python 3)
Group: Development/Python3
Requires: lib%name = %version-%release

%description -n python3-module-%oname
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

This package contains python module of Shiboken.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx\-build|py3_sphinx-build|g' \
	ApiExtractor/doc/CMakeLists.txt doc/CMakeLists.txt

%prepare_sphinx3 .
ln -s ../objects.inv doc

%build
export PATH=$PATH:%_qt4dir/bin
FLAGS="$(pkg-config phonon --cflags)"
%add_optflags $FLAGS

mkdir BUILD
pushd BUILD

cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DENABLE_GCC_OPTIMIZATION:BOOL=ON \
	-DENABLE_VERSION_SUFFIX:BOOL=OFF \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DQT_PHONON_INCLUDE_DIR:PATH="%_includedir/kde4" \
	-DUSE_PYTHON3:BOOL=ON \
	-DPYTHON3_INCLUDE_DIR=%__python3_includedir \
	-DPYTHON3_LIBRARY=%__libpython3 \
	..

%make_build VERBOSE=1

pushd doc
%make doc
popd

popd

%install
%makeinstall_std -C BUILD

%files
%doc COPYING* AUTHORS
%doc BUILD/doc/html
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake
%_pkgconfigdir/*

%files -n python3-module-%oname
%python3_sitelibdir/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt3.git20140422.2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt3.git20140422.2
- Fixed build with gcc-6

* Fri Apr 01 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt3.git20140422.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt3.git20140422
- (.spec) Fixed %%_libpython3 path (a new macro).
- Denis Medvedev changed environment for Python3.5 build.

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20140422
- Version 1.2.2

* Mon Nov 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20131015
- Version 1.2.1

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.git20130527
- New snapshot

* Tue Feb 19 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.2-alt1.1
- Fix build with Python 3.3

* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2 for Python 3

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1 for Python 3

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt3
- Rebuilt with disabled version suffix of generatorrunner

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt2
- Disabled library version suffix

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus

