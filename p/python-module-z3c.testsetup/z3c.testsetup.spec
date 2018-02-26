%define oname z3c.testsetup
Name: python-module-%oname
Version: 0.8.3
Release: alt2.1
Summary: Easier test setup for Zope 3 projects and other Python packages
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testsetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.testing martian zope.app.testing zope.app.zcmlfiles
%py_requires zope.component

%add_python_req_skip non_existing_package

%description
Setting up tests for Zope 3 projects sometimes tends to be cumbersome.
You often have to prepare complex things like test layers, setup
functions, teardown functions and much more. Often these steps have to
be done again and again. z3c.testsetup jumps in here, to support much
flatter test setups. The package supports normal Python unit tests and
doctests.

Doctests and test modules are found throughout a whole package and
registered with sensible, modifiable defaults. This saves a lot of
manual work!

See README.txt and the other .txt files in the src/z3c/testsetup
directory for API documentation. (Or further down this page when reading
this on pypi).

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus

