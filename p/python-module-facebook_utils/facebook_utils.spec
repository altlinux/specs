%define oname facebook_utils

%def_with python3

Name: python-module-%oname
Version: 0.20.3
Release: alt1.git20140717.1
Summary: Simple utilites for facebook integration
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook_utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jvanasco/facebook_utils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A collection of utilities for integrating user accounts with
Facebook.com.

Right now this handles oauth and graph operations.

%package -n python3-module-%oname
Summary: Simple utilites for facebook integration
Group: Development/Python3

%description -n python3-module-%oname
A collection of utilities for integrating user accounts with
Facebook.com.

Right now this handles oauth and graph operations.

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
%doc *.txt *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20.3-alt1.git20140717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20.3-alt1.git20140717
- Initial build for Sisyphus

