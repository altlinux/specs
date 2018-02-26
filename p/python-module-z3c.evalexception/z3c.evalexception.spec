%define oname z3c.evalexception
Name: python-module-%oname
Version: 2.0
Release: alt2.1
Summary: Debugging middlewares for zope.publisher-based web applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.evalexception/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires paste zope.security

%description
z3c.evalexception provides two WSGI middlewares for debugging web
applications running on the zope.publisher object publishing framework
(e.g. Zope 3). Both middlewares will intercept an exception thrown by
the application and provide means for debugging.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

