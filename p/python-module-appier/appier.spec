%define oname appier

%def_with python3

Name: python-module-%oname
Version: 0.8.25
Release: alt1.1
Summary: Appier Framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/appier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

%package tests
Summary: Tests for Appier Framework
Group: Development/Python
Requires: %name = %EVR

%description tests
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

This package contains tests for Appier Framework.

%package -n python3-module-%oname
Summary: Appier Framework
Group: Development/Python3

%description -n python3-module-%oname
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

%package -n python3-module-%oname-tests
Summary: Tests for Appier Framework
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

This package contains tests for Appier Framework.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.25-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.25-alt1
- Version 0.8.25

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.19-alt1
- Version 0.8.19

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.15-alt1
- Initial build for Sisyphus

