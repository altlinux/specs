Name: shiboken
Version: 1.1.1
Release: alt1
Summary: Generates bindings for C++ libraries using CPython source code
License: GPLv2, LGPLv2.1
Group: Development/KDE and QT
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake libqt4-devel gcc-c++ libgeneratorrunner-devel
BuildPreReq: phonon-devel generatorrunner qt4-designer xml-utils
BuildPreReq: python-module-sphinx-devel xsltproc
BuildPreReq: libxml2-devel libxslt-devel libqt4-assistant-devel

Requires: lib%name = %version-%release

%description
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

%package -n lib%name
Summary: Shared libraries of Shiboken
Group: System/Libraries

%description -n lib%name
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

This package contains shared libraries of Shiboken.

%package -n lib%name-devel
Summary: Development files of Shiboken
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Shiboken is a plugin (front-end) for Generator Runner. It generates
bindings for C++ libraries using CPython source code.

This package contains development files of Shiboken.

%prep
%setup

%prepare_sphinx .
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
	-DUSE_PYTHON3:BOOL=OFF \
	..

%make_build VERBOSE=1

pushd doc
%make doc
popd

popd

%install
%makeinstall_std -C BUILD

gzip ChangeLog

%files
%doc ChangeLog* COPYING*
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

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt3
- Rebuilt with disabled version suffix of generatorrunner

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt2
- Disabled library version suffix

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus

