%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xraylib
Version: 4.1.1
Release: alt1
Summary: X-ray matter interaction cross sections for X-ray fluorescence applications
License: BSD-3-Clause
Group: Sciences/Physics
Url: https://github.com/tschoonj/xraylib

# https://github.com/tschoonj/xraylib.git
Source: %name-%version.tar
Patch2000: %name-e2k.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-fortran gcc-c++ swig
BuildRequires: python3-devel python3-module-Cython libnumpy-py3-devel

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
%ifarch %e2k
%patch2000 -p1
%endif

# change python shebangs to python3
find . -name '*.py' | xargs sed -i \
	-e '1s|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
	-e '1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
	%nil

%build
%add_optflags -D_FILE_OFFSET_BITS=64

export PYTHON=python3
export PYTHON_VERSION=%_python3_version
export CYTHON=cython3
sed -i 's|(SWIG)|(SWIG) -py3|' $(find ./ -name Makefile.am)

%autoreconf
%configure \
	--enable-static=no \
	--enable-python-integration \
	--disable-perl \
	%nil

%make_build

%install
%makeinstall_std

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -pv %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

rm -f %buildroot%python3_sitelibdir/*.la

%files -n lib%name
%doc license*.txt
%doc AUTHORS Changelog README* TODO
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
* Mon Jan 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt1
- Updated to upstream version 4.1.1.

* Fri Aug 13 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.1.0-alt2
- Added workaround for ICE in fortran compiler for Elbrus.

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1
- Updated to upstream version 4.1.0.

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

