%define oname django-oauth-plus

%def_with python3

Name: python-module-%oname
Version: 2.2.5
Release: alt1
Summary: Support of OAuth 1.0a in Django using python-oauth2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-oauth-plus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django-tests python-module-oauth2
BuildPreReq: python-module-south python-module-mock
BuildPreReq: python-module-unittest-xml-reporting
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-oauth2
BuildPreReq: python3-module-south python3-module-mock
BuildPreReq: python3-module-unittest-xml-reporting
BuildPreReq: python-tools-2to3
%endif

%py_provides oauth_provider

%description
Support of OAuth 1.0a in Django using python-oauth2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires django.test

%description tests
Support of OAuth 1.0a in Django using python-oauth2.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Support of OAuth 1.0a in Django using python-oauth2
Group: Development/Python3
%py3_provides oauth_provider

%description -n python3-module-%oname
Support of OAuth 1.0a in Django using python-oauth2.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires django.test

%description -n python3-module-%oname-tests
Support of OAuth 1.0a in Django using python-oauth2.

This package contains tests for %oname.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/runtests
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/runtests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/runtests
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/runtests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Initial build for Sisyphus

