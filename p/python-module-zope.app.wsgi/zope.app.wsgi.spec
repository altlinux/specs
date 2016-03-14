%define oname zope.app.wsgi

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt2.a4.1.1
Summary: WSGI application for the zope.publisher
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.wsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.testrunner python-module-eggtestinfo
#BuildPreReq: python-module-zope.interface python-module-zope.exceptions
#BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.testrunner python3-module-eggtestinfo
#BuildPreReq: python3-module-zope.interface python3-module-zope.exceptions
#BuildPreReq: python3-module-six
%endif

Requires: python-module-ZODB3
%py_requires webtest ZConfig zope.app.appsetup zope.event
%py_requires zope.processlifetime zope.app.publication zope.interface
%py_requires zope.publisher zope.security zope.container zope.error
%py_requires zope.component zope.configuration zope.lifecycleevent
%py_requires zope.session zope.site zope.testbrowser zope.testing
%py_requires zope.traversing zope.app

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-unittest2 python-module-zope.exceptions python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-setuptools python3-module-unittest2 python3-module-zope python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.testing
BuildRequires: python-module-eggtestinfo python-module-zope.testrunner python3-module-eggtestinfo python3-module-html5lib python3-module-zope.testrunner rpm-build-python3

%description
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

%package -n python3-module-%oname
Summary: WSGI application for the zope.publisher
Group: Development/Python3
Requires: python3-module-ZODB3
%py3_requires webtest ZConfig zope.app.appsetup zope.event
%py3_requires zope.processlifetime zope.app.publication zope.interface
%py3_requires zope.publisher zope.security zope.container zope.error
%py3_requires zope.component zope.configuration zope.lifecycleevent
%py3_requires zope.session zope.site zope.testbrowser zope.testing
%py3_requires zope.traversing zope.app

%description -n python3-module-%oname
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.wsgi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.annotation zope.authentication zope.browserpage
%py3_requires zope.componentvocabulary zope.location zope.login
%py3_requires zope.password zope.principalregistry zope.securitypolicy

%description -n python3-module-%oname-tests
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

This package contains tests for zope.app.wsgi.

%package tests
Summary: Tests for zope.app.wsgi
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.authentication zope.browserpage
%py_requires zope.componentvocabulary zope.location zope.login
%py_requires zope.password zope.principalregistry zope.securitypolicy

%description tests
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

This package contains tests for zope.app.wsgi.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.a4.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.a4.1
- NMU: Use buildreq for BR.

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a4
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.0-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt3
- Disabled *.pth

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt2
- Added necessary requirements

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Initial build for Sisyphus

