%define oname sacrud

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150114
Summary: sacrud - CRUD interface for SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sacrud
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/sacrud.git
Source: %name-%version.tar
# git://github.com/ITCase/pyramid_sacrud_example.git
Source1: _pyramid_sacrud_example.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-transaction
BuildPreReq: python-module-zope.sqlalchemy python-module-webhelpers
BuildPreReq: python-module-webtest python-module-nose
BuildPreReq: python-module-pyramid-tests python-modules-sqlite3
BuildPreReq: python-module-six
BuildPreReq: python-module-sphinx-devel itcase_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-transaction
BuildPreReq: python3-module-zope.sqlalchemy python3-module-webhelpers
BuildPreReq: python3-module-webtest python3-module-nose
BuildPreReq: python3-module-pyramid-tests python3-modules-sqlite3
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires zope.sqlalchemy sqlite3

%description
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing six

%description tests
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: sacrud - CRUD interface for SQLAlchemy
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.sqlalchemy sqlite3 six

%description -n python3-module-%oname
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
SACRUD will solve your problem of CRUD interface for SQLAlchemy, by
providing extension for Pyramid (yet) or use it in pure form. Unlike
classical CRUD interface, pyramid_sacrud allows override and flexibly
customize interface. (that is closer to django.contrib.admin).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

pushd docs
tar -xf %SOURCE1
cp -fR %_datadir/itcase_sphinx_theme _themes
popd

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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150114
- Version 0.2.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.git20141106
- Initial build for Sisyphus

