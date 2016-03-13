%define oname zc.ngi

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt2.1
Summary: Network Gateway Interface
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.ngi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zope.interface

%description
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

%package -n python3-module-%oname
Summary: Network Gateway Interface
Group: Development/Python3
%py3_requires zc zope.interface

%description -n python3-module-%oname
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

%package -n python3-module-%oname-tests
Summary: Tests for Network Gateway Interface
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing manuel

%description -n python3-module-%oname-tests
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

This package contains tests for Network Gateway Interface.

%package tests
Summary: Tests for Network Gateway Interface
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing manuel

%description tests
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

This package contains tests for Network Gateway Interface.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0rel-alt1
- Version 2.0.0 (released)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0a6-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0a6-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0a6-alt1
- Initial build for Sisyphus

