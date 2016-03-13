%define oname z3c.formui

%def_with python3

Name: python-module-%oname
Version: 3.0.0
Release: alt2.a2.1
Summary: A set of initial UI components for z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.form z3c.macro z3c.template zope.component
%py_requires zope.publisher zope.viewlet

%description
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

%package -n python3-module-%oname
Summary: A set of initial UI components for z3c.form
Group: Development/Python3
%py3_requires z3c.form z3c.macro z3c.template zope.component
%py3_requires zope.publisher zope.viewlet

%description -n python3-module-%oname
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.formui
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.form

%description -n python3-module-%oname-tests
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

This package contains tests for z3c.formui.

%package tests
Summary: Tests for z3c.formui
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.form

%description tests
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

This package contains tests for z3c.formui.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.a2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.a2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.a2
- Version 3.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus

