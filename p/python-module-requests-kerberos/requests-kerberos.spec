%define oname requests-kerberos

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20141114.1
Summary: A Kerberos authentication handler for python-requests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-kerberos/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/requests/requests-kerberos.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-requests
BuildPreReq: python-module-kerberos
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-requests
BuildPreReq: python3-module-kerberos
%endif

%py_provides requests_kerberos

%description
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%package -n python3-module-%oname
Summary: A Kerberos authentication handler for python-requests
Group: Development/Python3
%py3_provides requests_kerberos

%description -n python3-module-%oname
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20141114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20141114
- Initial build for Sisyphus

