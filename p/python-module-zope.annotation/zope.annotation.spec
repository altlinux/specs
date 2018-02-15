%define _unpackaged_files_terminate_build 1
%define oname zope.annotation

%def_with check

Name: python-module-%oname
Version: 4.6.0
Release: alt1%ubt

Summary: Object annotation mechanism
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.annotation.git
Url: http://pypi.python.org/pypi/zope.annotation

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.component
BuildRequires: python-module-zope.location
BuildRequires: python-module-zope.proxy
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.location
BuildRequires: python3-module-zope.proxy

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-BTrees
BuildRequires: python-module-coverage
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-BTrees
BuildRequires: python3-module-coverage
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
%endif

%py_requires zope.interface zope.component zope.location zope.proxy

%description
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package -n python3-module-%oname
Summary: Object annotation mechanism
Group: Development/Python3

%description -n python3-module-%oname
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.testrunner

%description -n python3-module-%oname-tests
This package contains tests for %oname

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
This package contains tests for %oname

%prep
%setup
%patch0 -p1

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
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%python_sitelibdir_noarch:%python_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v

pushd ../python3
export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%changelog
* Thu Feb 15 2018 Stanislav Levin <slev@altlinux.org> 4.6.0-alt1%ubt
- 4.4.2 -> 4.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.4.2-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt1.dev0.git20150613
- Version 4.4.2.dev0
- Enabled check

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt3
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Avoid requirement on ZODB3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

