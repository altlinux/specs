%define _unpackaged_files_terminate_build 1
%define oname zope.browsermenu

%def_with check

Name: python-module-%oname
Version: 4.3.0
Release: alt1%ubt

Summary: Browser menu implementation for Zope
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.browsermenu.git
Url: http://pypi.python.org/pypi/zope.browsermenu

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.publisher
BuildRequires: python-module-zope.pagetemplate
BuildRequires: python-module-zope.component-tests
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-zope.pagetemplate
BuildRequires: python3-module-zope.component-tests
%endif

%py_requires zope.browser
%py_requires zope.component
%py_requires zope.configuration
%py_requires zope.i18nmessageid
%py_requires zope.interface
%py_requires zope.pagetemplate
%py_requires zope.publisher
%py_requires zope.schema
%py_requires zope.security
%py_requires zope.traversing

%description
This package provides an implementation of browser menus and ZCML
directives for configuring them.

%package -n python3-module-%oname
Summary: Browser menu implementation for Zope
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package provides an implementation of browser menus and ZCML
directives for configuring them.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This package contains tests for %oname.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
export PYTHONPATH=src
zope-testrunner --test-path=src -vv

pushd ../python3
zope-testrunner3 --test-path=src -vv
popd

%files
%doc LICENSE.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/browsermenu/tests

%files tests
%python_sitelibdir/zope/browsermenu/tests

%files -n python3-module-%oname
%doc LICENSE.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/browsermenu/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/browsermenu/tests

%changelog
* Wed Mar 07 2018 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1%ubt
- 4.1.1 -> 4.3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Enabled check

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt3
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.a1
- Version 4.1.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus

