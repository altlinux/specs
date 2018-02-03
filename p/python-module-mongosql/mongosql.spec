%define oname mongosql

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.1.0
Release: alt1.git20141011.1.1
Summary: SqlAlchemy queries with MongoDB-style
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mongosql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RussellLuo/py-mongosql.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-SQLAlchemy python-module-wheel
BuildPreReq: python-module-nose python-module-psycopg2
BuildPreReq: python-module-flask_jsontools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-SQLAlchemy python3-module-wheel
BuildPreReq: python3-module-nose python3-module-psycopg2
BuildPreReq: python3-module-flask_jsontools-tests
%endif

%py_provides %oname

%description
Extremely handy if you want to expose limited querying capabilities with
a JSON API while keeping it safe against SQL injections.

Tired of adding query parameters for pagination, filtering, sorting?
Here is the ultimate solution.

%package -n python3-module-%oname
Summary: SqlAlchemy queries with MongoDB-style
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Extremely handy if you want to expose limited querying capabilities with
a JSON API while keeping it safe against SQL injections.

Tired of adding query parameters for pagination, filtering, sorting?
Here is the ultimate solution.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.1.0-alt1.git20141011.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1.0-alt1.git20141011.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1.0-alt1.git20141011
- Initial build for Sisyphus

