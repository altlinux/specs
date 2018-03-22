%def_with python3

Name: xraylib
Version: 3.1.0
Release: alt1.git20141114.1.1
Summary: X-ray matter interaction cross sections for X-ray fluorescence applications
License: BSD
Group: Sciences/Physics
Url: https://github.com/tschoonj/xraylib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tschoonj/xraylib.git
Source: %name-%version.tar

BuildPreReq: gcc-fortran gcc-c++ swig
BuildPreReq: python-devel python-module-Cython libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython libnumpy-py3-devel
%endif

%description
This is xraylib, a library for X-ray matter interactions cross sections
for X-ray fluorescence applications.

%package -n lib%name
Summary: X-ray matter interaction cross sections for X-ray fluorescence applications
Group: System/Libraries

%description -n lib%name
This is xraylib, a library for X-ray matter interactions cross sections
for X-ray fluorescence applications.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This is xraylib, a library for X-ray matter interactions cross sections
for X-ray fluorescence applications.

This package contains development files of %name.

%package -n python-module-%name
Summary: Python bindings of %name
Group: Development/Python
Requires: lib%name = %EVR
%py_provides %name

%description -n python-module-%name
This is xraylib, a library for X-ray matter interactions cross sections
for X-ray fluorescence applications.

This package contains python bindings of %name.

%package -n python3-module-%name
Summary: Python bindings of %name
Group: Development/Python3
Requires: lib%name = %EVR
%py3_provides %name

%description -n python3-module-%name
This is xraylib, a library for X-ray matter interactions cross sections
for X-ray fluorescence applications.

This package contains python bindings of %name.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%autoreconf
%configure \
	--enable-static=no \
	--enable-python-integration \
	--disable-perl
%make_build

%if_with python3
pushd ../python3
export PYTHON=python3
export PYTHON_VERSION=%_python3_version
export CYTHON=cython3
sed -i 's|(SWIG)|(SWIG) -py3|' $(find ./ -name Makefile.am)
%autoreconf
%configure \
	--enable-static=no \
	--enable-python-integration \
	--disable-perl
%make_build
popd
%endif

%install
%makeinstall_std
rm -f %buildroot%python_sitelibdir/*.la
%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif


%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/buildroot install
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	buildroot%_bindir/%name
install -m755 buildroot%_bindir/%name %buildroot%_bindir/%name.py3
rm -f buildroot%python3_sitelibdir/*.la
install -d %buildroot%python3_sitelibdir
mv buildroot%python3_sitelibdir/* \
	%buildroot%python3_sitelibdir/
%ifarch x86_64
mv buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
popd
%endif

%files -n lib%name
%doc AUTHORS BUGS Changelog README TODO
%_libdir/*.so.*
%_datadir/%name

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n python-module-%name
%doc example/*.py
%_bindir/%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%_bindir/%name.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1.git20141114.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt1.git20141114.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.git20141114
- Initial build for Sisyphus

