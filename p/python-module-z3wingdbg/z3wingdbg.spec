%define oname z3wingdbg
Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: Wing IDE debugger integration for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3wingdbg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

%package tests
Summary: Tests for Wing IDE debugger integration for Zope3
Group: Development/Python
Requires: %name = %version-%release

%description tests
Zope3 package providing debug integration with the Wing IDE, allowing
you to run Zope3 applications under the control of the Wing debugger.

This package contains tests for Wing IDE debugger integration for Zope3.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1.1
- Rebuild with Python-2.7

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

