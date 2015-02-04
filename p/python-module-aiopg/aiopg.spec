%define oname aiopg

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150203
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiopg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiopg.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-psycopg2
BuildPreReq: python-module-SQLAlchemy
%endif
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-psycopg2
BuildPreReq: python3-module-SQLAlchemy
%endif

%py_provides %oname
%py_requires asyncio psycopg2 sqlalchemy

%description
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%package -n python3-module-%oname
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio psycopg2 sqlalchemy

%description -n python3-module-%oname
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs html

rm -f requirements.txt

%check
%if_with python2
python setup.py test
#python runtests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#python3 runtests.py -v
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150102
- Initial build for Sisyphus

