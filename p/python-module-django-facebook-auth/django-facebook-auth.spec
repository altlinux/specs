%define oname django-facebook-auth

%def_with python3

Name: python-module-%oname
Version: 3.6.3
Release: alt1.1
Summary: Authorisation app for Facebook API
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-auth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires south celery

%description
A stable Facebook authentication backend for Django >= 1.4.

Starting from version 3.6.0 Django 1.7 is supported.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A stable Facebook authentication backend for Django >= 1.4.

Starting from version 3.6.0 Django 1.7 is supported.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Authorisation app for Facebook API
Group: Development/Python3
%py3_requires south celery

%description -n python3-module-%oname
A stable Facebook authentication backend for Django >= 1.4.

Starting from version 3.6.0 Django 1.7 is supported.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A stable Facebook authentication backend for Django >= 1.4.

Starting from version 3.6.0 Django 1.7 is supported.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Initial build for Sisyphus

