%define oname zope.thread

Name: python3-module-%oname
Version: 3.4
Release: alt4

Summary: Zope3 Thread-Local Storage
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.thread/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope


%description
This package is deprecated and exists soley for backward compatability.

%package tests
Summary: Tests for Zope3 Thread-Local Storage
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
This package is deprecated and exists soley for backward compatability.

This package contains tests for Zope3 Thread-Local Storage.

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.4-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.4-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt3.1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt3.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 3.4-alt3.1.1
- NMU: Use buildreq for BR.

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 3.4-alt3.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Initial build for Sisyphus

