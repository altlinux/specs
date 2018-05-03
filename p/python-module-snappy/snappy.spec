%define oname snappy

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt2.1.1
Summary: Python library for the snappy compression library from Google
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-snappy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libsnappy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
Python bindings for the snappy compression library from Google.

%if_with python3
%package -n python3-module-%oname
Summary: Python3 library for the snappy compression library from Google
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the snappy compression library from Google.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' snappy.py
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
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Fixed source for Python3

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

