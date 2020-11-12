%define oname mathutils

Name: python3-module-%oname
Version: 2.81.2
Release: alt2

Summary: Library providing Matrix, Vector, Quaternion, Euler and Color classes

License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/mathutils/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake

BuildRequires: cmake gcc-c++
BuildRequires: python3-devel python3-module-setuptools

%description
A general math utilities library providing Matrix, Vector, Quaternion,
Euler and Color classes, written in C for speed.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing -DNDEBUG=1
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std
%if %_lib == lib64
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/mathutils.so %buildroot%python3_sitelibdir/
%endif

%check
# Ran 0 tests, but repeated build
#python3 setup.py test

%files
%python3_sitelibdir/*

%changelog
* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.81.2-alt2
- build python3 package from tarball, cleanup spec

* Wed Feb 26 2020 Grigory Ustinov <grenka@altlinux.org> 2.81.2-alt1
- Build new version for python3.8.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.74-alt1.git20150315.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.74-alt1.git20150315.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.74-alt1.git20150315.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.74-alt1.git20150315.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.74-alt1.git20150315
- Initial build for Sisyphus

