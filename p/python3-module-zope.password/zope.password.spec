%define _unpackaged_files_terminate_build 1
%define oname zope.password

%def_with check

Name: python3-module-%oname
Version: 4.4
Release: alt1
Summary: Password encoding and checking utilities
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.password/
Vcs: https://github.com/zopefoundation/zope.password

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.security
%endif

BuildArch: noarch

%py3_requires zope zope.component zope.configuration zope.interface

%description
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

%package tests
Summary: Tests for zope.password
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.schema

%description tests
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

This package contains tests for zope.password.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/zope/password/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Mon Jun 06 2022 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt3
- Fix noarch crutch.
- Fix license.

* Thu Apr 02 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt2
- Fix tests by adding zope.security to BR:

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt1
- NMU: 4.2.0 -> 4.3.1
- Remove python2 module build

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

