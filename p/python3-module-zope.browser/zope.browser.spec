%define _unpackaged_files_terminate_build 1
%define oname zope.browser

%def_with check

Name: python3-module-%oname
Version: 2.3
Release: alt1

Summary: Shared Zope Toolkit browser components (Python3)
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.browser
#Git: https://github.com/zopefoundation/zope.browser.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.interface
%endif

%py3_requires zope

%description
This package provides shared browser components for the Zope Toolkit.

%package tests
Summary: Tests for %oname (Python3)
Group: Development/Python3
Requires: %name = %EVR

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
%exclude %python3_sitelibdir/zope/browser/tests.*
%exclude %python3_sitelibdir/zope/browser/*/tests.*

%files tests
%python3_sitelibdir/zope/browser/tests.*
%python3_sitelibdir/zope/browser/*/tests.*

%changelog
* Thu Dec 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.3-alt1
- NMU: 2.2.0 -> 2.3
- Remove python2 module build
- Remove ubt tags from changelog

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2
- NMU: remove ubt from release

* Wed Mar 07 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt3.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt3
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

