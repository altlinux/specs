%define _unpackaged_files_terminate_build 1
%define oname zope.copy

%def_with check

Name: python-module-%oname
Version: 4.1.0
Release: alt1%ubt

Summary: Pluggable object copying mechanism
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.copy.git
Url: http://pypi.python.org/pypi/zope.copy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-zope.location
BuildRequires: python-module-zope.component
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.location
BuildRequires: python3-module-zope.component
%endif

%py_requires zope.interface

%description
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package -n python3-module-%oname
Summary: Pluggable object copying mechanism
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.component
%py3_requires zope.location
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for zope.copy
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component
%py_requires zope.location
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
%exclude %python_sitelibdir/zope/copy/tests

%files tests
%python_sitelibdir/zope/copy/tests

%files -n python3-module-%oname
%doc LICENSE.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/copy/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/copy/tests

%changelog
* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1%ubt
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

