# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.znanja1.git20120922.1.1.1
%define oname zc.thread

%def_with python3

Name: python-module-%oname
Version: 0.1.0
#Release: alt1.znanja1.git20120922.1
Summary: Thread-creation helper
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.thread/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/znanja/zc.thread.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-mock
BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-mock
BuildPreReq: python3-module-zope.testing
%endif

%py_provides %oname
%py_requires zc

%description
This package provides a very simple thread-creation API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This package provides a very simple thread-creation API.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Thread-creation helper
Group: Development/Python3
%py3_provides %oname
%py3_requires zc

%description -n python3-module-%oname
This package provides a very simple thread-creation API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides a very simple thread-creation API.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zc/*/tests.*

%files tests
%python_sitelibdir/zc/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.znanja1.git20120922
- Initial build for Sisyphus

