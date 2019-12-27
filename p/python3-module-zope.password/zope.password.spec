%define _unpackaged_files_terminate_build 1
%define oname zope.password

%def_with check

Name: python3-module-%oname
Version: 4.3.1
Release: alt1
Summary: Password encoding and checking utilities
License: ZPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.password/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-coverage
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
%endif

%py3_requires zope zope.component zope.configuration zope.interface

%description
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

%package tests
Summary: Tests for zope.password
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.schema

%description tests
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

This package contains tests for zope.password.

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

%check
# FIXME: this is a hack to invoke /usr/bin/coverage3 from python3-module-coverage
# while tox.ini tries to invoke /usr/bin/coverage
# Is coverage{3} needed during package buildtime unittesting at all?
sed -i 's|coverage r|coverage3 r|g' tox.ini
sed -i 's|zope-testrunner|zope-testrunner3|g' tox.ini
sed -i 's|sphinx-build|py3_sphinx-build|g' tox.ini

export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt1
- NMU: 4.2.0 -> 4.3.1
- Remove python2 module build

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

