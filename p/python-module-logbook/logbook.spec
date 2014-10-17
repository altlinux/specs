%define oname logbook

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1.dev.git20141012
Summary: A logging replacement for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Logbook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/logbook.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-sphinx-devel
BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
BuildPreReq: python3-module-py
%endif

%py_provides %oname

%description
An awesome logging implementation that is fun to use.

%package -n python3-module-%oname
Summary: A logging replacement for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An awesome logging implementation that is fun to use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
An awesome logging implementation that is fun to use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An awesome logging implementation that is fun to use.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
export USE_CYTHON=1
CFLAGS="%optflags" python scripts/travis_build.py
%python_build_debug

%if_with python3
pushd ../python3
CFLAGS="%optflags" python3 scripts/travis_build.py
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
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev.git20141012
- Initial build for Sisyphus

