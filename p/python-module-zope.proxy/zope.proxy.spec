%define _unpackaged_files_terminate_build 1
%define oname zope.proxy

%def_with python3

Name: python-module-%oname
Version: 4.2.0
Release: alt1
Summary: Generic Transparent Proxies
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.proxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d3/3f/6137793109bdc27cfa2d1331c2c57f2a1081dd7e2ff872b3967c1a937d9c/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

%package -n python3-module-%oname
Summary: Generic Transparent Proxies
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

%package -n python3-module-%oname-tests
Summary: Tests for Generic Transparent Proxies
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

This package contains tests for Generic Transparent Proxies.

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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc *.txt *.rst docs/*.rst
%_includedir/*
%if_with python3
%exclude %_includedir/python3*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%_includedir/python3*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.6-alt1
- Version 4.1.6

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1
- Version 4.1.4
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

