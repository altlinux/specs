%define pypi_name zope.errorview

# Depends on zope.browserpage which has been deleted from repo
%def_without check

Name: python3-module-%pypi_name
Version: 2.0
Release: alt1

Summary: Basic HTTP and Browser exception views
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.errorview
Vcs: https://github.com/zopefoundation/zope.errorview

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.i18n
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-zope.authentication
BuildRequires: python3-module-zope.browser
%endif

%description
Provides basic HTTP and Browser views for common exceptions.

%package tests
Summary: Tests for zope.errorview
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
Provides basic HTTP and Browser views for common exceptions.

This package contains tests for zope.errorview.

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
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.rst
%python3_sitelibdir/zope/errorview
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 2.0-alt1
- New version 2.0.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1
- version updated to 1.2.0
- python2 disabled

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.11-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt2.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Version 0.11

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Initial build for Sisyphus

