%define oname django-facebook
Name: python3-module-%oname
Version: 6.0.0
Release: alt1.git20140618.1
Summary: Facebook open graph API client in python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tschellenbach/Django-facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

%package tests
Summary: Tests for Facebook open graph API client in python
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip test

%description tests
Facebook open graph API client in python. Enables django applications to
register users using facebook. Fixes issues with the official but
unsupported Facebook python-sdk. Enables mobile facebook authentication.
Canvas page authentication for facebook applications. FQL access via the
server side api.

This package contains tests for Facebook open graph API client in
python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS *.rest
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.py
%exclude %python3_sitelibdir/*/__pycache__/tests.*
%exclude %python3_sitelibdir/*/test_utils

%files tests
%python3_sitelibdir/*/tests.py
%python3_sitelibdir/*/__pycache__/tests.*
%python3_sitelibdir/*/test_utils

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.0.0-alt1.git20140618.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.git20140618
- Initial build for Sisyphus

