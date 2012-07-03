%define oname z3c.formjsdemo
Name: python-module-%oname
Version: 0.3.1
Release: alt3.1
Summary: A set of demo applications for ``z3c.formjs``
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formjsdemo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires jquery.javascript jquery.layer z3c.form
%py_requires z3c.formdemo z3c.formjs z3c.formui z3c.layer z3c.pagelet
%py_requires z3c.template z3c.viewlet z3c.zrtresource zope.viewlet
%py_requires zope.session

%description
This package is going to show off the different features of the
``z3c.formjs`` package.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt3
- Removed setuptools from requirements

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

