%define oname zope.sendmail

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1
Summary: Zope sendmail
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.sendmail/
#Git: https://github.com/zopefoundation/zope.sendmail.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-transaction
BuildRequires: python3-module-zope.i18nmessageid
BuildRequires: python3-module-zope.schema
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.component-tests
%endif

%py3_requires zope transaction zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.component zope.configuration

%description
zope.sendmail is a package for email sending from Zope 3 applications.

%package tests
Summary: Tests for Zope sendmail
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.security zope.component

%description tests
zope.sendmail is a package for email sending from Zope 3 applications.

This package contains tests for Zope sendmail.

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

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
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0.2 -> 5.0
- Remove python2 module build
- Rearrange unittests execution

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev0.git20150613
- Version 4.0.2.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

