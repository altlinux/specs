%define _unpackaged_files_terminate_build 1
%define oname zope.copy

%def_with check

Name: python3-module-%oname
Version: 4.2
Release: alt3

Summary: Pluggable object copying mechanism
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.copy
#Git: https://github.com/zopefoundation/zope.copy.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.location
BuildRequires: python3-module-zope.component
%endif

%py3_requires zope

%description
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.component
%py3_requires zope.location
%py3_requires zope.testing

%description tests
This package contains tests for %oname.

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
export PYTHONPATH=src
zope-testrunner3 --test-path=src -vv

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/copy/tests

%files tests
%python3_sitelibdir/zope/copy/tests

%changelog
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.2-alt3
- NMU: remove python2 module build

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.2-alt1
- new version 4.2

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.3 -> 4.1.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

