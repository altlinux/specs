%define _unpackaged_files_terminate_build 1
%define oname django-facebook-users

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1
Summary: Django implementation for Facebook Graph API Users
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-users/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ramusus/django-facebook-users.git
Source0: https://pypi.python.org/packages/0c/fd/d2a767fba5ec2d0c5f6d26b3a3d0f33945c0a9bf4cf2690becbd6c4f81ce/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Application for interacting with Facebook Graph API Users objects using
Django model interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip models

%description tests
Application for interacting with Facebook Graph API Users objects using
Django model interface.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django implementation for Facebook Graph API Users
Group: Development/Python3

%description -n python3-module-%oname
Application for interacting with Facebook Graph API Users objects using
Django model interface.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip models

%description -n python3-module-%oname-tests
Application for interacting with Facebook Graph API Users objects using
Django model interface.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20130323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20130323
- Initial build for Sisyphus

