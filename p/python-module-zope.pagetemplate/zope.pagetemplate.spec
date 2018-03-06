%define _unpackaged_files_terminate_build 1
%define oname zope.pagetemplate

%def_with check

Name: python-module-%oname
Version: 4.3.0
Release: alt1%ubt

Summary: Zope Page Templates
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.pagetemplate.git
Url: http://pypi.python.org/pypi/zope.pagetemplate

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.component-tests
BuildRequires: python-module-zope.proxy
BuildRequires: python-module-zope.security
BuildRequires: python-module-zope.tal
BuildRequires: python-module-zope.tales
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.traversing
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.proxy
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.tal
BuildRequires: python3-module-zope.tales
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.traversing
%endif

%py_requires zope.interface
%py_requires zope.component
%py_requires zope.tales
%py_requires zope.tal
%py_requires zope.i18n
%py_requires zope.i18nmessageid
%py_requires zope.traversing

%description
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

%package -n python3-module-%oname
Summary: Zope Page Templates
Group: Development/Python3

%description -n python3-module-%oname
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

%package -n python3-module-%oname-tests
Summary: Tests for Page Templates
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.proxy
%py3_requires zope.security

%description -n python3-module-%oname-tests
This package contains tests for Page Templates.

%package tests
Summary: Tests for Page Templates
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.proxy
%py_requires zope.security
%py_requires zope.testing

%description tests
This package contains tests for Page Templates.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/pagetemplate/tests

%files tests
%python_sitelibdir/zope/pagetemplate/tests

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/pagetemplate/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/pagetemplate/tests

%changelog
* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1%ubt
- 4.2.1 -> 4.3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.2.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1
- Enabled check

* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Added necessary requirements

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

