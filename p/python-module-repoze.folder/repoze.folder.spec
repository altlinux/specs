%define oname repoze.folder

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20141228.1
Summary: Stripped-down ZODBcontainer implementation with object event support
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.folder
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.folder.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze ZODB3 zope.component zope.interface

%description
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

%package -n python3-module-%oname
Summary: Stripped-down ZODBcontainer implementation with object event support
Group: Development/Python3
%py3_requires repoze ZODB3 zope.component zope.interface

%description -n python3-module-%oname
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.folder
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires sphinx zope.testing nose coverage

%description -n python3-module-%oname-tests
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

This package contains tests for repoze.folder.

%package tests
Summary: Tests for repoze.folder
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx zope.testing nose coverage

%description tests
``repoze.folder`` provides a barebones ZODB folder implementation with
object event support.  Folders have a dictionary-like interface and
emit "object events" on the addition and removal of objects when
certain methods of this interface are exercised.

This package contains tests for repoze.folder.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.git20141228.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141228
- Version 1.0

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2.git20120330
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20120330
- Version 0.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110225
- Initial build for Sisyphus

