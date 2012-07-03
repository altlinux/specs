%define oname zope.proxy
Name: python-module-%oname
Version: 3.6.1
Release: alt2.1.1
Summary: Generic Transparent Proxies
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.proxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

%package tests
Summary: Tests for Generic Transparent Proxies
Group: Development/Python
Requires: %name = %version-%release

%description tests
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

This package contains tests for Generic Transparent Proxies.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_includedir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

