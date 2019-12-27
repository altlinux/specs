%define _unpackaged_files_terminate_build 1
%define oname zope.authentication

%def_with check

Name: python3-module-%oname
Version: 4.4.0
Release: alt1

Summary: Definition of authentication basics for the Zope Framework
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.authentication/
#Git: https://github.com/zopefoundation/zope.authentication.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-BTrees
BuildRequires: python3-module-coverage
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component
%endif

%py3_requires zope zope.browser zope.component zope.i18nmessageid
%py3_requires zope.interface zope.schema zope.security

%description
This package provides a definition of authentication concepts for use in
Zope Framework.

%package tests
Summary: Tests for zope.authentication
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a definition of authentication concepts for use in
Zope Framework.

This package contains tests for zope.authentication.

%prep
%setup
%patch0 -p1

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
# FIXME: this is a hack to invoke /usr/bin/coverage3 from python3-module-coverage
# while tox.ini tries to invoke /usr/bin/coverage
# Is coverage{3} needed during package buildtime unittesting at all?
sed -i 's|coverage r|coverage3 r|g' tox.ini

# export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Thu Dec 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt1
- NMU: 4.2.1 -> 4.4.0
- Remove python2 module build
- Add unittests execution

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Dec 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

