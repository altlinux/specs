%define oname zope.size

Name: python3-module-%oname
Version: 4.1.0
Release: alt2

Summary: Interfaces and simple adapter that give the size of an object
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.size/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope zope.interface zope.i18nmessageid


%description
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

%package tests
Summary: Tests for zope.size
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

This package contains tests for zope.size.

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
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

