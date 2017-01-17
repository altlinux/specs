%define _unpackaged_files_terminate_build 1
%define oname wsrpc-tornado

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt1
Summary: WSRPC is WebSocket Remote procedure call for tornado and javascript
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/wsrpc-tornado/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mosquito/wsrpc.git
Source0: https://pypi.python.org/packages/c1/f0/4d263a27570697c05a9b0a89256e5d63dec55a8ed24519a3c9ae5e600886/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tornado
#BuildPreReq: python-tools-2to3
%endif

%py_provides wsrpc
%py_requires tornado

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-pycares python-module-pycurl python-module-pytest python-modules-wsgiref python3-module-pycares python3-module-pytest python3-module-zope rpm-build-python3 time

%description
Remote Procedure call through WebSocket between browser and tornado.

%package -n python3-module-%oname
Summary: WSRPC is WebSocket Remote procedure call for tornado and javascript
Group: Development/Python3
%py3_provides wsrpc
%py3_requires tornado

%description -n python3-module-%oname
Remote Procedure call through WebSocket between browser and tornado.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
cp -fR wsrpc/static %buildroot%python_sitelibdir/wsrpc/

%if_with python3
pushd ../python3
%python3_install
cp -fR wsrpc/static %buildroot%python3_sitelibdir/wsrpc/
popd
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20150119.1
- NMU: Use buildreq for BR.

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150119
- Initial build for Sisyphus

