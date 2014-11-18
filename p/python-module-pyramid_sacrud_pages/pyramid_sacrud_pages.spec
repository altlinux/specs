%define oname pyramid_sacrud_pages

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141116
Summary: Tree pages for pyramid CRUD interface sacrud
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_sacrud_pages/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/pyramid_sacrud_pages.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-nose
BuildPreReq: python-module-pyramid_sacrud python-module-SQLAlchemy
BuildPreReq: python-module-sqlalchemy_mptt python-module-webtest
BuildPreReq: python-module-pyramid_beaker python-module-pyramid_jinja2
BuildPreReq: python-module-BeautifulSoup4 python-module-waitress
BuildPreReq: python-module-beaker python-module-webhelpers
BuildPreReq: python-module-sphinx-devel itcase_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-nose
BuildPreReq: python3-module-pyramid_sacrud python3-module-SQLAlchemy
BuildPreReq: python3-module-sqlalchemy_mptt python3-module-webtest
BuildPreReq: python3-module-pyramid_beaker python3-module-pyramid_jinja2
BuildPreReq: python3-module-BeautifulSoup4 python-module-waitress
BuildPreReq: python3-module-beaker python3-module-webhelpers
BuildPreReq: python3-module-paginate_sqlalchemy python3-module-deform
BuildPreReq: python3-module-transaction python3-module-pyramid_beaker
BuildPreReq: python3-module-sacrud_deform python3-module-colander
BuildPreReq: python3-module-peppercorn python3-module-sacrud
BuildPreReq: python3-module-paginate python3-module-chameleon.core
BuildPreReq: python3-module-markupsafe python3-module-jinja2
BuildPreReq: python3-module-zope.sqlalchemy
%endif

%py_provides %oname

%description
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Tree pages for pyramid CRUD interface sacrud
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyramid_sacrud_pages provides a collections of pages to your Pyramid
application. This is very similar to django.contrib.flatpages but with a
tree structure and traversal algorithm in URL dispath.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

cp -fR %_datadir/itcase_sphinx_theme docs/_themes
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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst example
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
%doc *.rst example
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141116
- Version 0.0.2

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141106
- Initial build for Sisyphus

