%define oname zope.app.xmlrpcintrospection

%def_with python3

Name: python-module-%oname
Version: 3.5.1
Release: alt3.1
Summary: XML-RPC Method Introspection Support for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.xmlrpcintrospection/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.component zope.interface zope.publisher

%description
This Zope 3 package provides an XML-RPC introspection mechanism.

%package -n python3-module-%oname
Summary: XML-RPC Method Introspection Support for Zope 3
Group: Development/Python3
%py3_requires zope.app zope.component zope.interface zope.publisher

%description -n python3-module-%oname
This Zope 3 package provides an XML-RPC introspection mechanism.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.xmlrpcintrospection
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.site zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.login

%description -n python3-module-%oname-tests
This Zope 3 package provides an XML-RPC introspection mechanism.

This package contains tests for zope.app.xmlrpcintrospection.

%package tests
Summary: Tests for zope.app.xmlrpcintrospection
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.site zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.login

%description tests
This Zope 3 package provides an XML-RPC introspection mechanism.

This package contains tests for zope.app.xmlrpcintrospection.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

