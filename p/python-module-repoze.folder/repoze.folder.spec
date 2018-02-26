%define oname repoze.folder
Name: python-module-%oname
Version: 0.6.2
Release: alt1.git20110225.1.1
Summary: Stripped-down ZODBcontainer implementation with object event support
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.folder
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.folder.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze ZODB3 zope.component zope.interface

%description
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

%package tests
Summary: Tests for repoze.folder
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx repoze.sphinx.autointerface zope.testing

%description tests
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

This package contains tests for repoze.folder.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110225
- Initial build for Sisyphus

