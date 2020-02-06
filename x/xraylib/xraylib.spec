%define _unpackaged_files_terminate_build 1

Name: xraylib
Version: 3.3.0
Release: alt1
Summary: X-ray matter interaction cross sections for X-ray fluorescence applications
License: BSD
Group: Sciences/Physics
Url: https://github.com/tschoonj/xraylib

# https://github.com/tschoonj/xraylib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-fortran gcc-c++ swig
BuildRequires: python3-devel python3-module-Cython libnumpy-py3-devel
# TODO: remove libnumpy-devel when libnumpy-py3-devel is fixed
BuildRequires: libnumpy-devel

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

%build
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

%install
%makeinstall_std
sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
	%buildroot%_bindir/%name
rm -f %buildroot%python3_sitelibdir/*.la
%if "%_lib" == "lib64"
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%files
%_bindir/%name

%files -n lib%name
%doc AUTHORS BUGS Changelog README* TODO
%_libdir/*.so.*
%_datadir/%name

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n python3-module-%name
%python3_sitelibdir/*.py
%python3_sitelibdir/*.so
%python3_sitelibdir/__pycache__/*

%changelog
* Thu Feb 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0 (Closes: #38044).
- Disabled python-2.

* Thu May 10 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.0-alt2.git20141114
- fixed packaging on 64bit arches other than x86_64

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1.git20141114.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt1.git20141114.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.git20141114
- Initial build for Sisyphus

