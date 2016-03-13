%define oname requests-facebook

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20140225.1
Summary: A Python Library to interface with Facebook Graph API
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/michaelhelmick/requests-facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Requests-Facebook is a Python library to help interface with Facebook
Graph API using the awesome requests library by @kennethreitz.

%package -n python3-module-%oname
Summary: A Python Library to interface with Facebook Graph API
Group: Development/Python3

%description -n python3-module-%oname
Requests-Facebook is a Python library to help interface with Facebook
Graph API using the awesome requests library by @kennethreitz.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140225
- Initial build for Sisyphus

