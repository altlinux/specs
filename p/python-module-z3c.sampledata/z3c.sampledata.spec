%define oname z3c.sampledata

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: Sampledata Generator
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sampledata/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.authentication zope.component zope.i18nmessageid
%py_requires zope.interface zope.intid zope.lifecycleevent zope.schema
%py_requires zope.site zope.traversing zope.viewlet
%py_requires zope.app.pagetemplate zope.pluggableauth

%description
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

%package -n python3-module-%oname
Summary: Sampledata Generator
Group: Development/Python3
%py3_requires ZODB3 zope.authentication zope.component zope.i18nmessageid
%py3_requires zope.interface zope.intid zope.lifecycleevent zope.schema
%py3_requires zope.site zope.traversing zope.viewlet
%py3_requires zope.app.pagetemplate zope.pluggableauth

%description -n python3-module-%oname
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

%package -n python3-module-%oname-tests
Summary: Tests for Sampledata Generator
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles

%description -n python3-module-%oname-tests
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

This package contains tests for Sampledata Generator.

%package tests
Summary: Tests for Sampledata Generator
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles

%description tests
This package tries to do the best to support the development of sample
data generators. A sample data generator is a pluggable tool to create
data needed for tests.

This package contains tests for Sampledata Generator.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

