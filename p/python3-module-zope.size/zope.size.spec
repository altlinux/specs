%define oname zope.size

%def_with check

Name: python3-module-%oname
Version: 4.4
Release: alt1

Summary: Interfaces and simple adapter that give the size of an object
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.size
VCS: https://github.com/zopefoundation/zope.size

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.i18nmessageid
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.security
%endif

%description
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

%package tests
Summary: Tests for zope.size
Group: Development/Python3
Requires: %name = %EVR

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

%check
%tox_check

%files
%doc *.txt *.rst
%python3_sitelibdir/zope
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*


%changelog
* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

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

