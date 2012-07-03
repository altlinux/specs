%define oname zope.wfmc
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Workflow-Management Coalition Workflow Engine
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.wfmc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component ZODB3 zope.cachedescriptors

%description
This package provides an implementation of a Workflow-Management
Coalition (WFMC) workflow engine. The engine is provided as a collection
of workflow process components. Workflow processes can be defined in
Python or via the XML Process-Definition Language, XPDL.

%package tests
Summary: Tests for zope.wfmc
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides an implementation of a Workflow-Management
Coalition (WFMC) workflow engine. The engine is provided as a collection
of workflow process components. Workflow processes can be defined in
Python or via the XML Process-Definition Language, XPDL.

This package contains tests for zope.wfmc.

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
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

