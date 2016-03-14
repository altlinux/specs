%define oname zope.app.tree

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt3.1
Summary: Static Tree Implementation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.tree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.container zope.component zope.interface
%py_requires zope.location zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

%package -n python3-module-%oname
Summary: Static Tree Implementation
Group: Development/Python3
%py3_requires zope.app zope.container zope.component zope.interface
%py3_requires zope.location zope.publisher zope.schema zope.security
%py3_requires zope.traversing

%description -n python3-module-%oname
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

%package -n python3-module-%oname-tests
Summary: Tests for Static Tree Implementation
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

This package contains tests for Static Tree Implementation.

%package tests
Summary: Tests for Static Tree Implementation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package was designed to be a light-weight and easy-to-use static
tree implementation. It allows the developer to quickly create trees
with nodes that can be opened and closed without the use of JavaScript.
The tree state can be retained over multiple sessions.

This package contains tests for Static Tree Implementation.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

