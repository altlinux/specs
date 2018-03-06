%define _unpackaged_files_terminate_build 1
%define oname zope.location

%def_with check

Name: python-module-%oname
Version: 4.1.0
Release: alt1%ubt

Summary: Zope Location
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.location.git
Url: http://pypi.python.org/pypi/zope.location/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.schema
BuildRequires: python-module-zope.proxy
BuildRequires: python-module-zope.copy
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.configuration
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.proxy
BuildRequires: python3-module-zope.copy
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.configuration
%endif

%py_requires zope.interface
%py_requires zope.schema
%py_requires zope.proxy
%py_requires zope.configuration
%py_requires zope.component

%description
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname
Summary: Zope Location
Group: Development/Python3
%py3_requires zope.configuration
%py3_requires zope.component

%description -n python3-module-%oname
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Location
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for Zope Location
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.copy

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
%exclude %python_sitelibdir/zope/location/tests

%files tests
%python_sitelibdir/zope/location/tests

%files -n python3-module-%oname
%doc LICENSE.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/location/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/location/tests

%changelog
* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1%ubt
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.dev0.git20150128.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2.dev0.git20150128
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20141027
- New snapshot

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20140319
- Version 4.0.4dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Version 3.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

