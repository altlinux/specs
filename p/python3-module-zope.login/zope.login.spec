%define oname zope.login

%def_with check

Name: python3-module-%oname
Version: 2.2
Release: alt1

Summary: Login helpers for zope.publisher / authentication
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.login
VCS: https://github.com/zopefoundation/zope.login

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.authentication
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.testing
%endif

%description
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

%package tests
Summary: Tests for zope.login
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

This package contains tests for zope.login.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%tox_check

%files
%doc *.txt *.rst
%python3_sitelibdir/zope
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 2.2-alt1
- New version 2.2.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Version 2.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

