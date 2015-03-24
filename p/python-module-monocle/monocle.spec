%define oname monocle

%def_without python3

Name: python-module-%oname
Version: 0.29
Release: alt1.git20150323
Summary: An async programming framework with a blocking look-alike syntax
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/monocle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/saucelabs/monocle.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core-test python-module-tornado
BuildPreReq: python-module-nose python-module-OpenSSL
BuildPreReq: python-module-service-identity
BuildPreReq: python-modules-logging python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core-test python3-module-tornado
BuildPreReq: python3-module-nose python3-module-OpenSSL
BuildPreReq: python3-module-service-identity
%endif

%py_provides %oname
%py_requires twisted.python tornado logging multiprocessing
%py_requires service_identity

%description
monocle straightens out event-driven code using Python's generators. It
aims to be portable between event-driven I/O frameworks, and currently
supports Twisted and Tornado.

%if_with python3
%package -n python3-module-%oname
Summary: An async programming framework with a blocking look-alike syntax
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.python tornado logging multiprocessing

%description -n python3-module-%oname
monocle straightens out event-driven code using Python's generators. It
aims to be portable between event-driven I/O frameworks, and currently
supports Twisted and Tornado.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md examples tests
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples tests
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20150323
- Initial build for Sisyphus

