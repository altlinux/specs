%define oname z3c.dobbin

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt3.1
Summary: Relational object persistance framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.dobbin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface zope.schema zope.component zope.dottedname
%py_requires zope.configuration z3c.saconfig transaction monkey
%py_requires SQLAlchemy

%description
Dobbin is an object database implemented on top of SQLAlchemy. It's
designed to mimick the behavior of the Zope object database (ZODB) while
providing greater flexibility and control of the storage.

It supports strong typing with native SQL columns by utilizing the
declarative field definitions from zope.schema. Weak typing is supported
using the Python pickle protocol. Attributes are automatically persisted
with the exception of those starting with the characters "_v_" (volatile
attributes).

Tables to support the strongly typed attributes are created on-the-fly
with a 1:1 correspondence to interfaces with no inheritance (base
interface). As such, objects are modelled as a join between the
interfaces they implement plus a table that maintains object metadata
and weakly typed instance attributes.

%package -n python3-module-%oname
Summary: Relational object persistance framework
Group: Development/Python3
%py3_requires zope.interface zope.schema zope.component zope.dottedname
%py3_requires zope.configuration z3c.saconfig transaction monkey
%py3_requires SQLAlchemy

%description -n python3-module-%oname
Dobbin is an object database implemented on top of SQLAlchemy. It's
designed to mimick the behavior of the Zope object database (ZODB) while
providing greater flexibility and control of the storage.

It supports strong typing with native SQL columns by utilizing the
declarative field definitions from zope.schema. Weak typing is supported
using the Python pickle protocol. Attributes are automatically persisted
with the exception of those starting with the characters "_v_" (volatile
attributes).

Tables to support the strongly typed attributes are created on-the-fly
with a 1:1 correspondence to interfaces with no inheritance (base
interface). As such, objects are modelled as a join between the
interfaces they implement plus a table that maintains object metadata
and weakly typed instance attributes.

%package -n python3-module-%oname-tests
Summary: Tests for Relational object persistance framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Dobbin is an object database implemented on top of SQLAlchemy. It's
designed to mimick the behavior of the Zope object database (ZODB) while
providing greater flexibility and control of the storage.

This package contains tests for Relational object persistance framework.

%package tests
Summary: Tests for Relational object persistance framework
Group: Development/Python
Requires: %name = %version-%release

%description tests
Dobbin is an object database implemented on top of SQLAlchemy. It's
designed to mimick the behavior of the Zope object database (ZODB) while
providing greater flexibility and control of the storage.

This package contains tests for Relational object persistance framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added necesssary requirements
- Excludes *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

