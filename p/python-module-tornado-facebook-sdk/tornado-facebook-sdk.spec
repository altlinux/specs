%define oname tornado-facebook-sdk

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20121001.1
Summary: A tornado based facebook graph api wrapper
License: OSI
Group: Development/Python
Url: https://pypi.python.org/pypi/tornado-facebook-sdk/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pauloalem/tornado-facebook-sdk.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The tornado-facebook-sdk is a library that aims to ease the task of
writing non-blocking, server side, facebook social graph accessing code.
It's built using tornado. This makes tornado-facebook-sdk a perfect fit
if you're developing an application using tornado.

%package -n python3-module-%oname
Summary: A tornado based facebook graph api wrapper
Group: Development/Python3

%description -n python3-module-%oname
The tornado-facebook-sdk is a library that aims to ease the task of
writing non-blocking, server side, facebook social graph accessing code.
It's built using tornado. This makes tornado-facebook-sdk a perfect fit
if you're developing an application using tornado.

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

%files
%doc *.TXT *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.TXT *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20121001.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20121001
- Initial build for Sisyphus

