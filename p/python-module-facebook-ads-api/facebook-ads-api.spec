%define oname facebook-ads-api

%def_with python3

Name: python-module-%oname
Version: 0.1.52
Release: alt1.git20141125
Summary: Python client for the Facebook Ads API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook-ads-api/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/narrowcast/facebook-ads-api.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Python client for the Facebook Ads API.

%package -n python3-module-%oname
Summary: Python client for the Facebook Ads API
Group: Development/Python3

%description -n python3-module-%oname
Python client for the Facebook Ads API.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.52-alt1.git20141125
- Version 0.1.52

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.51-alt1.git20141024
- Version 0.1.51

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.46-alt1.git20140916
- Initial build for Sisyphus

