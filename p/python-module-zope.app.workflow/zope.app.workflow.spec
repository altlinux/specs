%define oname zope.app.workflow

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt4.1
Summary: Workflow Engine for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.component zope.container zope.interface
%py_requires zope.lifecycleevent zope.app.container zope.tales
%py_requires zope.security zope.schema zope.security zope.proxy
%py_requires zope.traversing zope.event zope.app.i18n zope.configuration
%py_requires zope.dublincore zope.app.pagetemplate zope.app.security
%py_requires zope.publisher zope.app.form

%description
This package provides the original implementation of a workflow engine
based on Zope 3. It has been superceeded by zope.wfmc and
hurry.workflow.

%package -n python3-module-%oname
Summary: Workflow Engine for Zope 3
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.component zope.container zope.interface
%py3_requires zope.lifecycleevent zope.app.container zope.tales
%py3_requires zope.security zope.schema zope.security zope.proxy
%py3_requires zope.traversing zope.event zope.app.i18n zope.configuration
%py3_requires zope.dublincore zope.app.pagetemplate zope.app.security
%py3_requires zope.publisher zope.app.form

%description -n python3-module-%oname
This package provides the original implementation of a workflow engine
based on Zope 3. It has been superceeded by zope.wfmc and
hurry.workflow.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.workflow
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.app.file
%py3_requires zope.app.folder zope.app.securitypolicy

%description -n python3-module-%oname-tests
This package provides the original implementation of a workflow engine
based on Zope 3. It has been superceeded by zope.wfmc and
hurry.workflow.

This package contains tests for zope.app.workflow.

%package tests
Summary: Tests for zope.app.workflow
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.app.file
%py_requires zope.app.folder zope.app.securitypolicy

%description tests
This package provides the original implementation of a workflow engine
based on Zope 3. It has been superceeded by zope.wfmc and
hurry.workflow.

This package contains tests for zope.app.workflow.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*
%python_sitelibdir/*/*/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Moved all tests into tests package

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

