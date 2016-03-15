%define oname sqlalchemy-elasticquery

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141222.1
Summary: Use ElasticSearch query search in SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy-elasticquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/loverajoel/sqlalchemy-elasticquery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-modules-json
BuildPreReq: python-module-flask_sqlalchemy python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python-tools-2to3
BuildPreReq: python3-module-flask_sqlalchemy python3-modules-sqlite3
%endif

%py_provides sqlalchemy_elasticquery

%description
This extension allow you use the ElasticSearch syntax for search in
SQLAlchemy.

%package -n python3-module-%oname
Summary: Use ElasticSearch query search in SQLAlchemy
Group: Development/Python3
%py3_provides sqlalchemy_elasticquery

%description -n python3-module-%oname
This extension allow you use the ElasticSearch syntax for search in
SQLAlchemy.

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
export PYTHONPATH=%buildroot%python_sitelibdir
python test/test.py
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/test.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20141222.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141222
- Initial build for Sisyphus

