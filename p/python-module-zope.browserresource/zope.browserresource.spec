%define oname zope.browserresource

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20141226
Summary: Browser resources implementation for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browserresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.configuration python-module-transaction
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-zope.i18n-tests
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.component-tests
BuildPreReq: python3-module-zope.configuration
BuildPreReq: python3-module-zope.contenttype
BuildPreReq: python3-module-zope.i18n-tests
BuildPreReq: python3-module-zope.interface python3-module-transaction
BuildPreReq: python3-module-zope.location
BuildPreReq: python3-module-zope.publisher
BuildPreReq: python3-module-zope.schema
BuildPreReq: python3-module-zope.traversing
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-zope.testrunner
%endif

%py_requires zope zope.component zope.configuration zope.contenttype
%py_requires zope.i18n zope.interface zope.location zope.publisher
%py_requires zope.schema zope.traversing

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

%package -n python3-module-%oname
Summary: Browser resources implementation for Zope
Group: Development/Python3
%py3_requires zope zope.component zope.configuration zope.contenttype
%py3_requires zope.i18n zope.interface zope.location zope.publisher
%py3_requires zope.schema zope.traversing

%description -n python3-module-%oname
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

%package -n python3-module-%oname-tests
Summary: Tests for zope.browserresource
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package contains tests for zope.browserresource.

%package tests
Summary: Tests for zope.browserresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package contains tests for zope.browserresource.

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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
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
* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20141226
- Version 4.1.1.dev0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1.dev0.git20141104
- Version 4.0.3.dev0
- Enabled testing

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt1
- Initial build for Sisyphus

