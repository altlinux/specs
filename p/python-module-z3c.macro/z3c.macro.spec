%define oname z3c.macro

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: Simpler definition of ZPT macros
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.macro/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.configuration zope.interface
%py_requires zope.pagetemplate zope.publisher zope.schema zope.tales
%py_requires z3c.ptcompat

%description
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

%package -n python3-module-%oname
Summary: Simpler definition of ZPT macros
Group: Development/Python3
%py3_requires zope.component zope.configuration zope.interface
%py3_requires zope.pagetemplate zope.publisher zope.schema zope.tales
%py3_requires z3c.ptcompat

%description -n python3-module-%oname
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

%package -n python3-module-%oname-tests
Summary: Tests for Simpler definition of ZPT macros
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.template z3c.pt lxml zope.browserpage zope.app.testing
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

This package contains tests for Simpler definition of ZPT macros.

%package tests
Summary: Tests for Simpler definition of ZPT macros
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.template z3c.pt lxml zope.browserpage zope.app.testing
%py_requires zope.testing

%description tests
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

This package contains tests for Simpler definition of ZPT macros.

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

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

