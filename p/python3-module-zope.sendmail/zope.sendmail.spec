%define _unpackaged_files_terminate_build 1
%define pypi_name zope.sendmail

%def_with check

Name: python3-module-%pypi_name
Version: 5.3
Release: alt1
Summary: Zope sendmail
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.sendmail/
Vcs: https://github.com/zopefoundation/zope.sendmail.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-transaction
%endif

%py3_requires zope transaction zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.component zope.configuration

%description
zope.sendmail is a package for email sending from Zope 3 applications.

%package tests
Summary: Tests for Zope sendmail
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.security zope.component

%description tests
zope.sendmail is a package for email sending from Zope 3 applications.

This package contains tests for Zope sendmail.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -v

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/zope/sendmail/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 5.3-alt1
- New version 5.3.

* Fri Sep 24 2021 Nikolai Kostrigin <nickel@altlinux.org> 5.2-alt1
- 5.0 -> 5.2

* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0.2 -> 5.0
- Remove python2 module build
- Rearrange unittests execution

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev0.git20150613
- Version 4.0.2.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

