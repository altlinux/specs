%define oname django-oauth2-provider

%def_with python3

Name: python-module-%oname
Version: 0.2.7
Release: alt1.dev.git20140318.1.1
Summary: Provide OAuth2 access to your app
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-oauth2-provider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/caffeinehit/django-oauth2-provider.git 
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-tests python-module-shortuuid
#BuildPreReq: python-module-django-dbbackend-sqlite3
#BuildPreReq: python-module-oauth2
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-tests python3-module-shortuuid
#BuildPreReq: python3-module-django-dbbackend-sqlite3
#BuildPreReq: python3-module-oauth2
#BuildPreReq: python-tools-2to3
%endif

%py_provides provider
%py_requires oauth2

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-django python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml tzdata
BuildRequires: python-module-alabaster python-module-django-dbbackend-sqlite3 python-module-django-tests python-module-docutils python-module-html5lib python-module-httplib2 python-module-objects.inv python-module-setuptools-tests python-module-shortuuid python3-module-django python3-module-httplib2 python3-module-setuptools-tests rpm-build-python3 time

%description
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires django.test

%description tests
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Provide OAuth2 access to your app
Group: Development/Python3
%py3_provides provider
%py3_requires oauth2

%description -n python3-module-%oname
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires django.test

%description -n python3-module-%oname-tests
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
django-oauth2-provider is a Django application that provides
customizable OAuth2-authentication for your Django projects.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

export PYTHONPATH=%buildroot%python_sitelibdir
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
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.dev.git20140318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.dev.git20140318.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.dev.git20140318
- Initial build for Sisyphus

