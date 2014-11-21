%define oname SQLAlchemy-Searchable

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20141117
Summary: Provides fulltext search capabilities for declarative SQLAlchemy models
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Searchable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/sqlalchemy-searchable.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyparsing python-module-SQLAlchemy
BuildPreReq: python-module-psycopg2 python-module-SQLAlchemy-Utils
BuildPreReq: python-module-validators
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyparsing python3-module-SQLAlchemy
BuildPreReq: python3-module-psycopg2 python3-module-SQLAlchemy-Utils
BuildPreReq: python3-module-validators
%endif

%py_provides sqlalchemy_searchable

%description
Fulltext searchable models for SQLAlchemy. Only supports PostgreSQL.

%package -n python3-module-%oname
Summary: Provides fulltext search capabilities for declarative SQLAlchemy models
Group: Development/Python3
%py3_provides sqlalchemy_searchable

%description -n python3-module-%oname
Fulltext searchable models for SQLAlchemy. Only supports PostgreSQL.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Fulltext searchable models for SQLAlchemy. Only supports PostgreSQL.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fulltext searchable models for SQLAlchemy. Only supports PostgreSQL.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141117
- Initial build for Sisyphus

