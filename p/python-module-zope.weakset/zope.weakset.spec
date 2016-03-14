%define oname zope.weakset

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt3.1
Summary: Zope Object Database: object database and persistence
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.weakset/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope

%description
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

%package -n python3-module-%oname
Summary: Zope Object Database: object database and persistence
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

%package -n python3-module-%oname-tests
Summary: Tests for zope.weakset
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip __init__

%description -n python3-module-%oname-tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

This package contains tests for zope.weakset.

%package tests
Summary: Tests for zope.weakset
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip __init__

%description tests
The Zope Object Database provides an object-oriented database for Python
that provides a high-degree of transparency. Applications can take
advantage of object database features with few, if any, changes to
application logic. ZODB includes features such as a plugable storage
interface, rich transaction support, and undo.

This distribution includes the weakset module from ZODB.

This package contains tests for zope.weakset.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

