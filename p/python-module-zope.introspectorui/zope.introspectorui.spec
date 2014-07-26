%define oname zope.introspectorui

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3
Summary: Views for the info objects from zope.introspector
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.introspectorui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope grokcore.component grokcore.view zope.interface
%py_requires zope.component zope.location zope.introspector
%py_requires z3c.autoinclude

%description
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

%package -n python3-module-%oname
Summary: Views for the info objects from zope.introspector
Group: Development/Python3
%py3_requires zope grokcore.component grokcore.view zope.interface
%py3_requires zope.component zope.location zope.introspector
%py3_requires z3c.autoinclude

%description -n python3-module-%oname
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

%package -n python3-module-%oname-tests
Summary: Tests for zope.introspectorui
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing z3c.testsetup
%py3_requires zope.securitypolicy

%description -n python3-module-%oname-tests
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

This package contains tests for zope.introspectorui.

%package tests
Summary: Tests for zope.introspectorui
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing z3c.testsetup
%py_requires zope.securitypolicy

%description tests
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

This package contains tests for zope.introspectorui.

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
* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

