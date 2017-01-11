%define _unpackaged_files_terminate_build 1
%define oname jsonrpcserver

%def_with python3
%def_without python2

Name: python-module-%oname
Version: 3.4.1
Release: alt1
Summary: JSON-RPC 2.0 server library
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonrpcserver
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/88/0c/ce3e6ab71cb5c03dd2ed24dd790a6be995b8021c83798c8e6a0ce8a19c34/%{oname}-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jsonschema python-module-flask
#BuildPreReq: python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jsonschema python3-module-flask
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-jinja2 python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-jsonschema python3-module-nose python3-module-pytest rpm-build-python3 time

%description
A JSON-RPC 2.0 server library for Python 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A JSON-RPC 2.0 server library for Python 3.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON-RPC 2.0 server library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A JSON-RPC 2.0 server library for Python 3.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A JSON-RPC 2.0 server library for Python 3.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
rm -fR build
py.test
%endif
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*_test.*

%files tests
%python_sitelibdir/*/*_test.*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/*_test.*
#exclude %python3_sitelibdir/*/*/*_test.*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*_test.*
#python3_sitelibdir/*/*/*_test.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.11-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1
- Version 1.0.11

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Version 1.0.6

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

