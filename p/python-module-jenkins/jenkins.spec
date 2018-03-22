%define oname jenkins

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20091202.1.1.1
Summary: Python ctypes wrapper around Bob Jenkins' hash functions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jenkins/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lgastako/jenkins.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
This python module provides Bob Jenkin's hash functions in python (via
a ctypes wrapper calling the original C implementation).

%package -n python3-module-%oname
Summary: Python ctypes wrapper around Bob Jenkins' hash functions
Group: Development/Python3

%description -n python3-module-%oname
This python module provides Bob Jenkin's hash functions in python (via
a ctypes wrapper calling the original C implementation).

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|@CPYTHON@|.cpython-33m|' ../python3/jenkins.py
%endif

sed -i 's|@CPYTHON@||' jenkins.py

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1.git20091202.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20091202.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20091202.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20091202
- Initial build for Sisyphus

