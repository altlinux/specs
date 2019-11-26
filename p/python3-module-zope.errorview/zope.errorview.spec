%define oname zope.errorview

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Basic HTTP and Browser exception views
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.errorview/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope.component zope.interface zope.publisher zope.security


%description
Provides basic HTTP and Browser views for common exceptions.

%package tests
Summary: Tests for zope.errorview
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
Provides basic HTTP and Browser views for common exceptions.

This package contains tests for zope.errorview.

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

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
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

