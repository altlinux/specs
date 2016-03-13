%define oname z3c.sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt3.1
Summary: A SQLAlchemy wrapper for Zope 2 and Zope 3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires SQLAlchemy zope.sqlalchemy zope.component zope.interface
%py_requires zope.testing zope.schema

%description
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

%package -n python3-module-%oname
Summary: A SQLAlchemy wrapper for Zope 2 and Zope 3
Group: Development/Python3
%py3_requires SQLAlchemy zope.sqlalchemy zope.component zope.interface
%py3_requires zope.testing zope.schema

%description -n python3-module-%oname
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.sqlalchemy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

This package contains tests for z3c.sqlalchemy.

%package tests
Summary: Tests for z3c.sqlalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite zope.testing

%description tests
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

This package contains tests for z3c.sqlalchemy.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

