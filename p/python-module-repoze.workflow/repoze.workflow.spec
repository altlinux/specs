%define oname repoze.workflow

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.b1.git20141211.1
Summary: Declarative state machine for content-lifecycle workflows
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.workflow
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.workflow.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze repoze.zcml zope.component zope.interface
%py_requires zope.configuration

%description
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

%package -n python3-module-%oname
Summary: Declarative state machine for content-lifecycle workflows
Group: Development/Python3
%py3_requires repoze repoze.zcml zope.component zope.interface
%py3_requires zope.configuration

%description -n python3-module-%oname
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.workflow
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing repoze.sphinx.autointerface

%description -n python3-module-%oname-tests
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

This package contains tests for repoze.workflow.

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
pushd repoze/workflow
install -p -m644 *.zcml \
	%buildroot%python_sitelibdir/repoze/workflow/
install -p -m644 tests/fixtures/*.zcml \
	%buildroot%python_sitelibdir/repoze/workflow/tests/fixtures/
popd

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd ../python3/repoze/workflow
install -p -m644 *.zcml \
	%buildroot%python3_sitelibdir/repoze/workflow/
install -p -m644 tests/fixtures/*.zcml \
	%buildroot%python3_sitelibdir/repoze/workflow/tests/fixtures/
popd
%endif

%files
%doc *.txt docs/*.rst *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.b1.git20141211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.b1.git20141211
- Added missing files

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20141211
- Version 1.0b1

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2.git20130926
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20130926
- New snapshot

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20130110
- Version 0.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.git20110223.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110223.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110223
- Initial build for Sisyphus

