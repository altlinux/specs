%define oname SQLAlchemy-i18n

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20141022
Summary: Internationalization extension for SQLAlchemy models
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/sqlalchemy-i18n.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-SQLAlchemy-Utils
BuildPreReq: python-module-six python-module-Pygments
BuildPreReq: python-module-jinja2 python-module-docutils
BuildPreReq: python-module-flexmock python-module-psycopg2
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-SQLAlchemy-Utils
BuildPreReq: python3-module-six python3-module-Pygments
BuildPreReq: python3-module-jinja2 python3-module-docutils
BuildPreReq: python3-module-flexmock python3-module-psycopg2
%endif

%py_provides sqlalchemy_i18n

%description
Internationalization extension for SQLAlchemy models.

%package -n python3-module-%oname
Summary: Internationalization extension for SQLAlchemy models
Group: Development/Python3
%py3_provides sqlalchemy_i18n

%description -n python3-module-%oname
Internationalization extension for SQLAlchemy models.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Internationalization extension for SQLAlchemy models.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Internationalization extension for SQLAlchemy models.

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
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141022
- Initial build for Sisyphus

