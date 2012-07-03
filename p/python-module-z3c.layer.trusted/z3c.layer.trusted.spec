%define oname z3c.layer.trusted
Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: Trusted layer setup for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.trusted/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.publisher zope.app.publication zope.container
%py_requires z3c.layer.minimal

%description
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

%package tests
Summary: Tests for Trusted layer setup for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.testing zope.app.zcmlfiles
%py_requires z3c.layer.minimal

%description tests
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

This package contains tests for Trusted layer setup for Zope3.

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

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

