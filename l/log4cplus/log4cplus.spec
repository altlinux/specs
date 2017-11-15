%def_with python3

Name: log4cplus
Version: 2.0.0
Release: alt2.rc2
Summary: Logging library to C++
License: Apache License
Group: Development/C++
Url: http://log4cplus.sourceforge.net/

# https://github.com/log4cplus/log4cplus.git
Source: %name-%version.tar
# https://github.com/log4cplus/ThreadPool.git
Source1: threadpool.tar
# https://github.com/catchorg/Catch2.git
Source2: catch.tar

BuildRequires: gcc-c++ doxygen graphviz swig
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

%package -n lib%name
Summary: Shared libraries of logging library to C++
Group: System/Libraries

%description -n lib%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains shared libraries of log4cplus.

%package -n lib%name-devel
Summary: Development files of logging library to C++
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development files of log4cplus.

%package -n lib%name-devel-docs
Summary: Development documentation for logging library to C++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development documentation and manpages for
log4cplus.

%package -n python-module-%name
Summary: Python bindings of logging library to C++
Group: Development/Python
Requires: lib%name = %version-%release
%py_provides %name

%description -n python-module-%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains Python bindings of log4cplus.

%if_with python3
%package -n python3-module-%name
Summary: Python bindings of logging library to C++
Group: Development/Python3
Requires: lib%name = %version-%release
%py3_provides %name

%description -n python3-module-%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains Python bindings of log4cplus.
%endif

%prep
%setup

tar -xf %SOURCE1
tar -xf %SOURCE2

%if_with python3
cp -fR . ../python3
%endif

%build
%autoreconf
%configure \
	--enable-static=no \
	--enable-threads=yes \
	--with-working-c-locale \
	--with-python
%make_build

%if_with python3
pushd ../python3
export PYTHON=python3
%autoreconf
%configure \
	--enable-static=no \
	--enable-threads=yes \
	--with-working-c-locale \
	--with-python
sed -i 's|^\(SWIG =.*\)|\1 -py3|' $(find ./ -name Makefile)
%make_build
popd
%endif

pushd docs
doxygen doxygen.config
popd

%install
%makeinstall_std
%if "%_libexecdir" != "%_libdir"
mv %buildroot%python_sitelibdir_noarch/%name/* \
	%buildroot%python_sitelibdir/%name/
%endif

%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/buildroot install
install -d %buildroot%python3_sitelibdir
mv buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir/
%if "%_libexecdir" != "%_libdir"
mv buildroot%python3_sitelibdir_noarch/%name/* \
	%buildroot%python3_sitelibdir/%name/
%endif
popd
%endif

install -d %buildroot%_man3dir
install -m644 docs/man/man3/* %buildroot%_man3dir

%check
%make check

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README* TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-docs
%doc docs/html/*
%_man3dir/*

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2.rc2
- Updated to upstream version 2.0.0-rc2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.git20150807.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150807
- New snapshot (ALT #31238)

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.0-alt1.git20150412.1
- Rebuilt for gcc5 C++11 ABI.

* Thu May 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150412
- Version 2.0.0
- Added module for Python

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.rc2
- Version 1.2.0-rc2

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.rc1
- Version 1.2.0-rc1

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.rc3
- Version 1.1.1-rc3

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

