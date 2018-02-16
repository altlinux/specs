%define _unpackaged_files_terminate_build 1
%define oname zope.lifecycleevent

%def_with check

Name: python-module-%oname
Version: 4.2.0
Release: alt1%ubt

Summary: Object life-cycle events
License: ZPLv2.1
Group: Development/Python
# Source-git https://github.com/zopefoundation/zope.lifecycleevent.git
Url: http://pypi.python.org/pypi/zope.lifecycleevent

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.event
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.component-tests
BuildRequires: python-module-zope.configuration
BuildRequires: python-module-coverage
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-coverage
%endif

%py_requires zope.interface zope.event

%description
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

%package -n python3-module-%oname
Summary: Object life-cycle events (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
In Zope, events are used by components to inform each other about
relevant new objects and object modifications.

To keep all subscribers up to date it is indispensable that the life
cycle of an object is accompanied by various events.

%package -n python3-module-%oname-tests
Summary: Tests for zope.lifecycleevent (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.configuration zope.testrunner

%description -n python3-module-%oname-tests
This package contains tests for %oname

%package tests
Summary: Tests for zope.lifecycleevent
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component zope.configuration zope.testrunner zope.testing

%description tests
This package contains tests for %oname

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
coverage run -m zope.testrunner --test-path=src -vv

pushd ../python3
coverage3 run -m zope.testrunner --test-path=src -vv
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%changelog
* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1%ubt
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

