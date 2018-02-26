%define oname z3c.xmlhttp
Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: XMLHttpRequest (XHR) javascript
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.xmlhttp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.publisher zope.viewlet

%description
This package provides an (XHR) XMLHttpRequest implementation which is
used as base javascript library for z3c.jsonrpcproxy. This library can
be used in other javascript projects if you need a XHR implementation.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

