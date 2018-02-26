%define oname repoze.workflow
Name: python-module-%oname
Version: 0.5
Release: alt1.git20110223.1.1
Summary: Declarative state machine for content-lifecycle workflows
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.workflow
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.workflow.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze repoze.zcml zope.component zope.interface
%py_requires zope.configuration

%description
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

%package tests
Summary: Tests for repoze.workflow
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing repoze.sphinx.autointerface

%description tests
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

This package contains tests for repoze.workflow.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.git20110223.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110223.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110223
- Initial build for Sisyphus

