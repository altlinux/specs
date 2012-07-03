%define oname zc.recipe.testrunner
Name: python-module-%oname
Version: 1.4.0
Release: alt2.1
Summary: ZC Buildout recipe for creating test runners
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.testrunner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.recipe zc.buildout zope.testrunner z3c.recipe.scripts
%py_requires zope.testing

%description
This recipe generates zope.testing test-runner scripts for testing a
collection of eggs. The eggs must already be installed (using the
zc.recipe.egg recipe).

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

