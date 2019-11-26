%define oname repoze.workflow

Name: python3-module-%oname
Version: 1.0
Release: alt3

Summary: Declarative state machine for content-lifecycle workflows
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.workflow
# https://github.com/repoze/repoze.workflow.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze repoze.zcml zope.component zope.interface
%py3_requires zope.configuration


%description
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

%package tests
Summary: Tests for repoze.workflow
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing repoze.sphinx.autointerface

%description tests
repoze.workflow is a state machine and associated configuration system
useful for workflow-like applications.

This package contains tests for repoze.workflow.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

pushd ./repoze/workflow
install -p -m644 *.zcml \
	%buildroot%python3_sitelibdir/repoze/workflow/
install -p -m644 tests/fixtures/*.zcml \
	%buildroot%python3_sitelibdir/repoze/workflow/tests/fixtures/
popd

%files
%doc *.txt docs/*.rst *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt2.b1.git20141211.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.b1.git20141211.1.1
- (AUTO) subst_x86_64.

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

