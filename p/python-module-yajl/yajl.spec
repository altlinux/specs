%define oname yajl

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20140530.1.1.1
Summary: A CPython module for Yet-Another-Json-Library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yajl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rtyler/py-yajl.git
Source: %name-%version.tar

#BuildPreReq: libyajl1-devel
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-cjson
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires cjson

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: libyajl1-devel python-module-cjson python-module-setuptools python3-devel python3-module-pytest rpm-build-python3

%description
The yajl module provides a Python binding to the Yajl library originally
written by Lloyd Hilaiel.

%package -n python3-module-%oname
Summary: A CPython module for Yet-Another-Json-Library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The yajl module provides a Python binding to the Yajl library originally
written by Lloyd Hilaiel.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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

%check
python setup.py test
python setup.py build_ext -i
export PYTHONPATH=$PWD
python tests/unit.py
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
python3 tests/unit.py
popd
%endif

%files
%doc README.markdown compare.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.markdown compare.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1.git20140530.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.git20140530.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20140530.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20140530
- Initial build for Sisyphus

