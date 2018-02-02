%define oname pyuv

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20150619.1.1
Summary: Python interface for libuv
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyuv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/saghul/pyuv.git
# branch: v1.x
Source: %name-%version.tar
# https://github.com/libuv/libuv.git
# branch: v1.x
Source1: libuv.tar

BuildRequires(pre): /dev/pts /proc
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

%package -n python3-module-%oname
Summary: Python interface for libuv
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

This package contains documentation for %oname.

%prep
%setup

mkdir deps
pushd deps
tar -xf %SOURCE1
popd

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS ChangeLog *.rst TODO examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog *.rst TODO examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.git20150619.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20150619.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150619
- Version 1.1.0

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150116
- New snapshot

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150115
- Initial build for Sisyphus

