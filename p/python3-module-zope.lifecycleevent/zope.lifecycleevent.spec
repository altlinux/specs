%define _unpackaged_files_terminate_build 1
%define oname zope.lifecycleevent

%def_with check

Name: python3-module-%oname
Version: 4.3
Release: alt1

Summary: Object life-cycle events
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.lifecycleevent
#Git: https://github.com/zopefoundation/zope.lifecycleevent.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-coverage
%endif

%py3_requires zope

%description
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

%package tests
Summary: Tests for zope.lifecycleevent (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.configuration zope.testrunner

%description -n python3-module-%oname-tests
This package contains tests for %oname

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
coverage3 run -m zope.testrunner --test-path=src -vv

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
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3-alt1
- NMU: 4.2.0 -> 4.3
- Remove python2 module build
- Remove ubt tags from changelog

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2
- NMU: remove ubt from release

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1
- 4.1.1 -> 4.2.0

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20141229.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20141229.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20141229.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20141229
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.0-alt4.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

