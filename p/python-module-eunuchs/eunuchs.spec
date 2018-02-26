%define oname eunuchs
Name: python-module-eunuchs
Version: 20080310
Release: alt1.1.1
Summary: Missing manly parts of UNIX API for Python
License: LGPL
Group: Development/Python
Url: http://eagain.net/talks/eunuchs/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel

%description
Missing manly parts of UNIX API for Python.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc examples debian/changelog
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20080310-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20080310-alt1.1
- Rebuild with Python-2.7

* Tue Sep 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080310-alt1
- Initial build for Sisyphus

