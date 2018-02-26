%define oname zope.app.workflow
Name: python-module-%oname
Version: 3.5.0
Release: alt3.1
Summary: Workflow Engine for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Moved all tests into tests package

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

