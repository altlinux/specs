%define oname django-oauth-tokens

%def_with python3

Name: python-module-%oname
Version: 0.3.12
Release: alt1.git20140721.1
Summary: Getting, refreshing and storing OAuth access_tokens for Django standalone applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-oauth-tokens/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ramusus/django-oauth-tokens.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires tyoi.oauth2

%description
Application for getting, storing and refreshing OAuth access_tokens for
Django standalone applications without user manipulations. Applications
also can imitate authorized requests on behalf of user.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip factories models

%description tests
Application for getting, storing and refreshing OAuth access_tokens for
Django standalone applications without user manipulations. Applications
also can imitate authorized requests on behalf of user.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Getting, refreshing and storing OAuth access_tokens for Django standalone applications
Group: Development/Python3
%py3_requires tyoi.oauth2

%description -n python3-module-%oname
Application for getting, storing and refreshing OAuth access_tokens for
Django standalone applications without user manipulations. Applications
also can imitate authorized requests on behalf of user.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Application for getting, storing and refreshing OAuth access_tokens for
Django standalone applications without user manipulations. Applications
also can imitate authorized requests on behalf of user.

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

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.12-alt1.git20140721.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.12-alt1.git20140721
- Initial build for Sisyphus

