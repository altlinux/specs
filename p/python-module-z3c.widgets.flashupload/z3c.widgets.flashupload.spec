%define oname z3c.widgets.flashupload

%def_with python3

Name: python-module-%oname
Version: 1.0c1
Release: alt4.1
Summary: Zope Flash Upload Widget
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.widgets.flashupload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.event zope.filerepresentation
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.security zope.traversing zope.app.cache
%py_requires zope.app.component zope.app.container zope.app.pagetemplate
Requires: python-module-z3c.widgets = %EVR

%description
A Zope specific flash upload widget.

%package -n python3-module-%oname
Summary: Zope Flash Upload Widget
Group: Development/Python3
%py3_requires zope.component zope.event zope.filerepresentation
%py3_requires zope.i18nmessageid zope.interface zope.publisher
%py3_requires zope.security zope.traversing zope.app.cache
%py3_requires zope.app.component zope.app.container zope.app.pagetemplate
Requires: python3-module-z3c.widgets = %EVR

%description -n python3-module-%oname
A Zope specific flash upload widget.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Flash Upload Widget
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.app.testing

%description -n python3-module-%oname-tests
A Zope specific flash upload widget.

This package contains tests for Zope Flash Upload Widget.

%package tests
Summary: Tests for Zope Flash Upload Widget
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing

%description tests
A Zope specific flash upload widget.

This package contains tests for Zope Flash Upload Widget.

%package -n python-module-z3c.widgets
Summary: Core package of z3c.widgets
Group: Development/Python

%description -n python-module-z3c.widgets
This package contains core package of z3c.widgets.

%package -n python3-module-z3c.widgets
Summary: Core package of z3c.widgets
Group: Development/Python3

%description -n python3-module-z3c.widgets
This package contains core package of z3c.widgets.

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
touch %buildroot%python_sitelibdir/z3c/widgets/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/widgets/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/z3c/widgets/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.widgets
%python_sitelibdir/z3c/widgets/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/z3c/widgets/__init__.py
%exclude %python3_sitelibdir/z3c/widgets/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-z3c.widgets
%python3_sitelibdir/z3c/widgets/__init__.py
%python3_sitelibdir/z3c/widgets/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0c1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt4
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt3
- Added python-module-z3c.widgets

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0c1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt2
- Added necesssary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c1-alt1
- Initial build for Sisyphus

