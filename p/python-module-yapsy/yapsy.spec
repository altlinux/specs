%define oname yapsy

%def_with python3

Name: python-module-%oname
Version: 1.10.423
Release: alt1.git20141110
Summary: Yet another plugin system
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Yapsy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tibonihoo/yapsy.git
Source: %name-%version.tar
Source1: README.md
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-modules-logging
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-coveralls
%endif

%py_provides %oname
%py_requires logging

%description
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

The main purpose is to depend only on Python's standard libraries and to
implement only the basic functionalities needed to detect, load and keep
track of several plugins. It supports both Python 2 and 3.

%package -n python3-module-%oname
Summary: Yet another plugin system
Group: Development/Python3
%py3_provides %oname
%py3_requires logging

%description -n python3-module-%oname
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

The main purpose is to depend only on Python's standard libraries and to
implement only the basic functionalities needed to detect, load and keep
track of several plugins. It supports both Python 2 and 3.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

This package contains documentation for %oname.

%prep
%setup
install -p -m644 %SOURCE1 .

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.423-alt1.git20141110
- Initial build for Sisyphus

