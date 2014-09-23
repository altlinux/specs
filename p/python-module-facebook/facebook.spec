%define oname facebook

%def_with python3

Name: python-module-%oname
Version: 2.3.14
Release: alt1.git20140409
Summary: Facebook API client for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jgorset/facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Conflicts: python-module-facebook-sdk

%description
Facebook makes it even easier to interact with Facebook's Graph API.

%package -n python3-module-%oname
Summary: Facebook API client for Python
Group: Development/Python3
Conflicts: python3-module-facebook-sdk

%description -n python3-module-%oname
Facebook makes it even easier to interact with Facebook's Graph API.

%prep
%setup

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
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.14-alt1.git20140409
- Initial build for Sisyphus

