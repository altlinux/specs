%define _unpackaged_files_terminate_build 1
%define oname appier

Name: python-module-%oname
Version: 1.18.25
Release: alt1

Summary: Appier Framework

License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/appier/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

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

%build
%python3_build_debug

%install
%python3_install

%files -n python3-module-%oname
%doc PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.18.25-alt1
- new version 1.18.25 (with rpmrb script)
- python3 only (uses yield from)

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1
- automated PyPI update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.25-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.25-alt1
- Version 0.8.25

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.19-alt1
- Version 0.8.19

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.15-alt1
- Initial build for Sisyphus

