%define oname zope.dublincore

%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 4.3.0
Release: alt1

Summary: Zope Dublin Core implementation
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.dublincore/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-persistent
BuildRequires: python3-module-pytz
BuildRequires: python3-module-zope.annotation
BuildRequires: python3-module-zope.datetime
BuildRequires: python3-module-zope.lifecycleevent
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-repoze
BuildRequires: python3-module-repoze.sphinx
BuildRequires: python3-module-repoze.sphinx.autointerface
%endif

%description
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%package tests
Summary: Tests for zope.dublincore
Group: Development/Python3
Requires: %name = %EVR

%description tests
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

This package contains tests for zope.dublincore.

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
%python3_sitelibdir/zope/dublincore
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/dublincore/tests
%exclude %python3_sitelibdir/zope/dublincore/browser/tests

%files tests
%python3_sitelibdir/zope/dublincore/tests
%python3_sitelibdir/zope/dublincore/browser/tests


%changelog
* Tue Mar 07 2023 Anton Vyatkin <toni@altlinux.org> 1:4.3.0-alt1
- new version 4.3.0

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.1.1-alt2
- disable python2

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1:4.1.1-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.1-alt1
- Version 4.0.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Initial build for Sisyphus

