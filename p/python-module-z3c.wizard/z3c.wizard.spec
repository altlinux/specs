%define oname z3c.wizard

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt2.1
Summary: Wizard based on z3c.form for for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.wizard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.form z3c.formui z3c.pagelet zope.browserpage
%py_requires zope.component zope.configuration zope.event
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package provides a form wizard concept based on z3c.form for Zope3.

%package -n python3-module-%oname
Summary: Wizard based on z3c.form for for Zope3
Group: Development/Python3
%py3_requires z3c.form z3c.formui z3c.pagelet zope.browserpage
%py3_requires zope.component zope.configuration zope.event
%py3_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py3_requires zope.location zope.publisher zope.schema zope.security
%py3_requires zope.traversing

%description -n python3-module-%oname
This package provides a form wizard concept based on z3c.form for Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.wizard
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.macro z3c.testing zope.app.pagetemplate
%py3_requires zope.app.testing zope.publisher zope.testing
%py3_requires zope.browserresource

%description -n python3-module-%oname-tests
This package provides a form wizard concept based on z3c.form for Zope3.

This package contains tests for z3c.wizard.

%package tests
Summary: Tests for z3c.wizard
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.macro z3c.testing zope.app.pagetemplate
%py_requires zope.app.testing zope.publisher zope.testing
%py_requires zope.browserresource

%description tests
This package provides a form wizard concept based on z3c.form for Zope3.

This package contains tests for z3c.wizard.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

