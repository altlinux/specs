%define _unpackaged_files_terminate_build 1
%define oname repoze.zcml

%def_with check

Name: python3-module-%oname
Version: 1.0
Release: alt2.b1.git20141211
Summary: Simplified ZCML directives, reduced dependencies
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.zcml
#Git: https://github.com/repoze/repoze.zcml.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-transaction
BuildRequires: python3-module-zope.component >= 3.5.0
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.testing
%endif

%py3_requires repoze zope.component zope.configuration

%description
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

%package tests
Summary: Tests for repoze.zcml
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

This package contains tests for repoze.zcml.

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
sed -i 's|python setup|python3 setup|g' tox.ini

tox.py3 --sitepackages -e py%{python_version_nodots python3} -v

%files
%doc *.txt docs/*.rst *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0-alt2.b1.git20141211
- NMU: Remove python2 module build
- Add unittests execution

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1.b1.git20141211.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.b1.git20141211.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.b1.git20141211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20141211
- Version 1.0b1

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20120325
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120325
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222
- Initial build for Sisyphus

