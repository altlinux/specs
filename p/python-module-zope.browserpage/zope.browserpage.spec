%define oname zope.browserpage

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt3
Summary: ZCML directives for configuring browser views for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browserpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.pagetemplate zope.component zope.configuration
%py_requires zope.interface zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

%package -n python3-module-%oname
Summary: ZCML directives for configuring browser views for Zope
Group: Development/Python3
%py3_requires zope.pagetemplate zope.component zope.configuration
%py3_requires zope.interface zope.publisher zope.schema zope.security
%py3_requires zope.traversing

%description -n python3-module-%oname
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

%package -n python3-module-%oname-tests
Summary: Tests for zope.browserpage
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.browsermenu zope.testrunner

%description -n python3-module-%oname-tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

This package contains tests for zope.browserpage.

%package tests
Summary: Tests for zope.browserpage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.browsermenu zope.testrunner

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions.

This package contains tests for zope.browserpage.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt3
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.a1
- Version 4.1.0a1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.2-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.2-alt1
- Initial build for Sisyphus

