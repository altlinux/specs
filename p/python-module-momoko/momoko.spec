%define oname momoko

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.1.1
Release: alt1.git20150803
Summary: Wraps (asynchronous) Psycopg2 for Tornado
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Momoko
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/FSX/momoko.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado python-module-psycopg2cffi
BuildPreReq: python-module-unittest2 python-module-psycopg2
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado python3-module-psycopg2cffi
BuildPreReq: python3-module-unittest2 python3-module-psycopg2
%endif

%py_provides %oname
%py_requires tornado psycopg2cffi psycopg2

%description
Momoko wraps Psycopg2's functionality for use in Tornado.

%if_with python3
%package -n python3-module-%oname
Summary: Wraps (asynchronous) Psycopg2 for Tornado
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado psycopg2cffi psycopg2

%description -n python3-module-%oname
Momoko wraps Psycopg2's functionality for use in Tornado.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Momoko wraps Psycopg2's functionality for use in Tornado.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
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
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst THANKS examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst THANKS examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150803
- Initial build for Sisyphus

