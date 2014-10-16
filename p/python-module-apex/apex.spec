%define oname apex

%def_with python3

Name: python-module-%oname
Version: 0.9.10
Release: alt1.git20130729
Summary: Pyramid toolkit to add Velruse, Flash Messages,CSRF, ReCaptcha and Sessions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/apex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cd34/apex.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cryptacular
BuildPreReq: python-module-zope.sqlalchemy
BuildPreReq: python-module-velruse
BuildPreReq: python-module-pyramid-tests
BuildPreReq: python-module-pyramid_mailer
BuildPreReq: python-module-requests
BuildPreReq: python-module-wtforms
BuildPreReq: python-module-wtforms-recaptcha
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-docutils
BuildPreReq: python-module-webtest
BuildPreReq: python-module-virtualenv
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-colander
BuildPreReq: python-module-PasteDeploy
BuildPreReq: python-module-pbkdf2
BuildPreReq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cryptacular
BuildPreReq: python3-module-zope.sqlalchemy
BuildPreReq: python3-module-velruse
BuildPreReq: python3-module-pyramid-tests
BuildPreReq: python3-module-pyramid_mailer
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-wtforms
BuildPreReq: python3-module-wtforms-recaptcha
BuildPreReq: python3-module-sphinx-devel
BuildPreReq: python3-module-docutils
BuildPreReq: python3-module-webtest
BuildPreReq: python3-module-virtualenv
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-PasteDeploy
BuildPreReq: python3-module-pbkdf2
BuildPreReq: python3-module-zope.deprecation
BuildPreReq: python3-module-openid
BuildPreReq: python3-module-zope.component
%endif

%py_provides %oname
%py_requires zope.sqlalchemy velruse pyramid_mailer pyramid requests
%py_requires wtforms wtforms-recaptcha

%description
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid toolkit to add Velruse, Flash Messages,CSRF, ReCaptcha and Sessions
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.sqlalchemy velruse pyramid_mailer pyramid requests
%py3_requires wtforms wtforms-recaptcha

%description -n python3-module-%oname
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Toolkit for Pyramid, a Pylons Project, to add Authentication and
Authorization using Velruse (OAuth) and/or a local database, CSRF,
ReCaptcha, Sessions, Flash messages and I18N.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if_with 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.git20130729
- Initial build for Sisyphus

