%define oname z3c.pagelet

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: Pagelets are way to specify a template without the O-wrap
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.template z3c.ptcompat zope.browserpage zope.component
%py_requires zope.configuration zope.contentprovider zope.interface
%py_requires zope.publisher zope.schema zope.security

%description
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

%package -n python3-module-%oname
Summary: Pagelets are way to specify a template without the O-wrap
Group: Development/Python3
%py3_requires z3c.template z3c.ptcompat zope.browserpage zope.component
%py3_requires zope.configuration zope.contentprovider zope.interface
%py3_requires zope.publisher zope.schema zope.security

%description -n python3-module-%oname
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.pagelet
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.form zope.testing zope.traversing
%py3_requires lxml z3c.pt z3c.ptcompat zope.formlib

%description -n python3-module-%oname-tests
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

This package contains tests for z3c.pagelet.

%package tests
Summary: Tests for z3c.pagelet
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.form zope.testing zope.traversing
%py_requires lxml z3c.pt z3c.ptcompat zope.formlib

%description tests
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

This package contains tests for z3c.pagelet.

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

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

