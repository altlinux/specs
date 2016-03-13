%define oname zc.resourcelibrary

%def_with python3

Name: python-module-%oname
Version: 1.3.4
Release: alt2.1
Summary: Post-rendering Resource Inclusion
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.resourcelibrary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zope.app.pagetemplate zope.app.publication
%py_requires zope.browserresource zope.component zope.configuration
%py_requires zope.interface zope.publisher zope.security zope.tales
%py_requires zope.traversing

%description
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

%package -n python3-module-%oname
Summary: Post-rendering Resource Inclusion
Group: Development/Python3
%py3_requires zc zope.app.pagetemplate zope.app.publication
%py3_requires zope.browserresource zope.component zope.configuration
%py3_requires zope.interface zope.publisher zope.security zope.tales
%py3_requires zope.traversing

%description -n python3-module-%oname
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

%package -n python3-module-%oname-tests
Summary: Tests for Post-rendering Resource Inclusion
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.authentication zope.app.securitypolicy
%py3_requires zope.app.testing zope.app.zcmlfiles zope.pagetemplate
%py3_requires zope.securitypolicy zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

This package contains tests for Post-rendering Resource Inclusion.

%package tests
Summary: Tests for Post-rendering Resource Inclusion
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.authentication zope.app.securitypolicy
%py_requires zope.app.testing zope.app.zcmlfiles zope.pagetemplate
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
The resource library is a Zope 3 extension that is designed to make the
inclusion of JavaScript, CSS, and other resources easy, cache-friendly,
and component-friendly.

This package contains tests for Post-rendering Resource Inclusion.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Version 1.3.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus

