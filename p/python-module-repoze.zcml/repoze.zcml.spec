%define oname repoze.zcml
Name: python-module-%oname
Version: 0.5
Release: alt1.git20110222.1.1
Summary: Simplified ZCML directives, reduced dependencies
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.zcml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.zcml.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze zope.component zope.configuration

%description
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

%package tests
Summary: Tests for repoze.zcml
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

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
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222
- Initial build for Sisyphus

