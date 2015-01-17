%define oname sacrud_deform

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20150114
Summary: Form generator for SQLAlchemy models
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sacrud_deform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/sacrud_deform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sacrud python-module-SQLAlchemy
BuildPreReq: python-module-colander python-module-deform
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-webtest python-module-webhelpers
BuildPreReq: python-module-BeautifulSoup4 python-module-waitress
BuildPreReq: python-module-webob python-module-markupsafe
BuildPreReq: python-module-ColanderAlchemy
BuildPreReq: python-module-sphinx-devel itcase_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sacrud python3-module-SQLAlchemy
BuildPreReq: python3-module-colander python3-module-deform
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-webtest python3-module-webhelpers
BuildPreReq: python3-module-BeautifulSoup4 python3-module-waitress
BuildPreReq: python3-module-webob python3-module-markupsafe
BuildPreReq: python3-module-ColanderAlchemy
%endif

%py_provides %oname

%description
Form generotor for SQLAlchemy models.

%package -n python3-module-%oname
Summary: Form generator for SQLAlchemy models
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Form generotor for SQLAlchemy models.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Form generotor for SQLAlchemy models.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Form generotor for SQLAlchemy models.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%make coverage
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
sed -i 's|coverage html|coverage3 html|' Makefile
%make coverage
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
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150114
- Version 0.0.5

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141106
- Initial build for Sisyphus

