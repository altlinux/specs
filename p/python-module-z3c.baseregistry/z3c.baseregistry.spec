%define oname z3c.baseregistry

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.1
Summary: Manage IComponents instances using Python code and ZCML
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.baseregistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.configuration zope.i18nmessageid
%py_requires zope.interface zope.schema zope.site zope.formlib
%py_requires zope.app.zcmlfiles

%description
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

%package -n python3-module-%oname
Summary: Manage IComponents instances using Python code and ZCML
Group: Development/Python3
%py3_requires zope.component zope.configuration zope.i18nmessageid
%py3_requires zope.interface zope.schema zope.site zope.formlib
%py3_requires zope.app.zcmlfiles

%description -n python3-module-%oname
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.baseregistry
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

This package contains tests for z3c.baseregistry.

%package tests
Summary: Tests for z3c.baseregistry
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

This package contains tests for z3c.baseregistry.

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
%exclude %python_sitelibdir/*/*/*tests*
%exclude %python_sitelibdir/*/*/*/*tests*

%files tests
%python_sitelibdir/*/*/*tests*
%python_sitelibdir/*/*/*/*tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*tests*
%exclude %python3_sitelibdir/*/*/*/*tests*
%exclude %python3_sitelibdir/*/*/*/*/*tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*tests*
%python3_sitelibdir/*/*/*/*tests*
%python3_sitelibdir/*/*/*/*/*tests*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excludes *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

