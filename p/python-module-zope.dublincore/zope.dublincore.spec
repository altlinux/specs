%define oname zope.dublincore

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 4.1.1
Release: alt1.1
Summary: Zope Dublin Core implementation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.dublincore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope pytz zope.component zope.datetime zope.interface
%py_requires zope.lifecycleevent zope.location zope.schema zope.security
%py_requires zope.annotation
%add_python_req_skip annotatableadapter

%description
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%package -n python3-module-%oname
Summary: Zope Dublin Core implementation
Group: Development/Python3
%py3_requires zope pytz zope.component zope.datetime zope.interface
%py3_requires zope.lifecycleevent zope.location zope.schema zope.security
%py3_requires zope.annotation
%add_python3_req_skip annotatableadapter

%description -n python3-module-%oname
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%package -n python3-module-%oname-tests
Summary: Tests for zope.dublincore
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.annotation zope.configuration
%py3_requires zope.testrunner

%description -n python3-module-%oname-tests
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

This package contains tests for zope.dublincore.

%package tests
Summary: Tests for zope.dublincore
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.annotation zope.configuration
%py_requires zope.testrunner

%description tests
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

This package contains tests for zope.dublincore.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.1-alt1
- Version 4.0.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Initial build for Sisyphus

