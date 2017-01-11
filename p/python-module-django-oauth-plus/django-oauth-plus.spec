%define _unpackaged_files_terminate_build 1
%define oname django-oauth-plus

%def_with python3

Name: python-module-%oname
Version: 2.2.9
Release: alt1
Summary: Support of OAuth 1.0a in Django using python-oauth2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-oauth-plus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/6c/26/eac704ebce0fa62ffe1eb07ddfe610add38dbf77dcfec5f9e704f21ae3ab/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-tests python-module-oauth2
#BuildPreReq: python-module-south python-module-mock
#BuildPreReq: python-module-unittest-xml-reporting
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-tests python3-module-oauth2
#BuildPreReq: python3-module-south python3-module-mock
#BuildPreReq: python3-module-unittest-xml-reporting
#BuildPreReq: python-tools-2to3
%endif

%py_provides oauth_provider

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-httplib2 python-module-pbr python-module-psycopg2 python-module-pytest python-module-setuptools python-module-unittest2 python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-httplib2 python3-module-ntlm python3-module-pbr python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-unittest2 python3-module-yaml
BuildRequires: python-module-django python-module-mock python-module-oauth2 python-module-setuptools-tests python3-module-django python3-module-html5lib python3-module-mock python3-module-oauth2 python3-module-setuptools-tests rpm-build-python3 time

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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.2.5-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Initial build for Sisyphus

