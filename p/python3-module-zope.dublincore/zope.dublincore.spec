%define oname zope.dublincore

Name: python3-module-%oname
Epoch: 1
Version: 4.1.1
Release: alt2

Summary: Zope Dublin Core implementation
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.dublincore/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires zope pytz zope.component zope.datetime zope.interface
%py3_requires zope.lifecycleevent zope.location zope.schema zope.security
%py3_requires zope.annotation
%add_python3_req_skip annotatableadapter


%description
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%package tests
Summary: Tests for zope.dublincore
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zope.annotation zope.configuration
%py3_requires zope.testrunner

%description tests
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

This package contains tests for zope.dublincore.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

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
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*


%changelog
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

