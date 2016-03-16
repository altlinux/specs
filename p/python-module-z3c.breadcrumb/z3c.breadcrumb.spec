%define oname z3c.breadcrumb

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: A pluggable breadcrumbs implementation based on adapters
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.breadcrumb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.interface zope.location
%py_requires zope.publisher zope.schema zope.traversing

%description
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

%package -n python3-module-%oname
Summary: A pluggable breadcrumbs implementation based on adapters
Group: Development/Python3
%py3_requires zope.component zope.interface zope.location
%py3_requires zope.publisher zope.schema zope.traversing

%description -n python3-module-%oname
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.breadcrumb
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.container

%description -n python3-module-%oname-tests
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

This package contains tests for z3c.breadcrumb.

%package tests
Summary: Tests for z3c.breadcrumb
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.container

%description tests
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

This package contains tests for z3c.breadcrumb.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

