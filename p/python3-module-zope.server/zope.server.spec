%define oname zope.server

%def_with check

Name: python3-module-%oname
Version: 4.0.2
Release: alt1
Summary: Zope Server (Web and FTP)
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.server/
#Git: https://github.com/zopefoundation/zope.server.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.publisher
BuildRequires: python3-module-paste
BuildRequires: python3-module-zope.component-tests
%endif

%py3_requires zope zope.interface zope.publisher zope.security

%description
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

%package tests
Summary: Tests for zope.server
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zope.i18n zope.component

%description tests
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

This package contains tests for zope.server.

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
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/zope-testrunner3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/zope-testrunner3\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/zope-testrunner3' tox.ini

sed -i 's|zope-testrunner |zope-testrunner3 |g' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests

%changelog
* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.0.2-alt1
- NMU: 3.9.0 -> 4.0.2
- Remove python2 module build
- Add unittests execution

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.9.0-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.0-alt2.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Version 3.9.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.5-alt1
- Version 3.8.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Initial build for Sisyphus

