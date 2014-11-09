%define oname pyramid_sacrud

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141107
Summary: Pyramid CRUD interface based on sacrud and SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_sacrud/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/pyramid_sacrud.git
Source: %name-%version.tar
# git://github.com/ITCase/pyramid_sacrud_example.git
Source1: _pyramid_sacrud_example.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-sacrud
BuildPreReq: python-module-peppercorn python-module-pyramid_jinja2
BuildPreReq: python-module-pyramid-tests python-module-colander
BuildPreReq: python-module-deform python-module-sacrud_deform
BuildPreReq: python-module-pyramid_beaker python-module-transaction
BuildPreReq: python-module-paginate_sqlalchemy python-module-webtest
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-webhelpers
BuildPreReq: python-module-sphinx-devel itcase_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-sacrud
BuildPreReq: python3-module-peppercorn python3-module-pyramid_jinja2
BuildPreReq: python3-module-pyramid-tests python3-module-colander
BuildPreReq: python3-module-deform python3-module-sacrud_deform
BuildPreReq: python3-module-pyramid_beaker python3-module-transaction
BuildPreReq: python3-module-paginate_sqlalchemy python3-module-webtest
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-webhelpers
%endif

%py_provides %oname

%description
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid CRUD interface based on sacrud and SQLAlchemy
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyramid_sacrud will solve your problem of CRUD interface for Pyramid.
Unlike classical CRUD interface, pyramid_sacrud allows override and
flexibly customize interface. (that is closer to django.contrib.admin).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

pushd docs
cp -fR %_datadir/itcase_sphinx_theme _themes
tar -xf %SOURCE1
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
cp -fR %oname/locale %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/locale %buildroot%python3_sitelibdir/%oname/
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
#sed -i 's|nosetests|nosetests3|' Makefile
#make test
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
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141107
- Version 0.0.2

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.git20141106
- Added %oname/locale

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141106
- Initial build for Sisyphus

