%define oname netius

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.5.3
Release: alt1.git20150202.1
Summary: Fast and readable async non-blocking network apps
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/netius/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hivesolutions/netius.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

%package tests
Summary: Tests and examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

This package contains tests and examples for %oname.

%package -n python3-module-%oname
Summary: Fast and readable async non-blocking network apps
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

%package -n python3-module-%oname-tests
Summary: Tests and examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Netius is a Python network library that can be used for the rapid
creation of asynchronous non-blocking servers and clients. It has no
dependencies, it's cross-platform, and brings some sample netius-powered
servers out of the box, namely a production-ready WSGI server.

This package contains tests and examples for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *.md doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/examples

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/examples
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.3-alt1.git20150202.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.git20150202
- Initial build for Sisyphus

