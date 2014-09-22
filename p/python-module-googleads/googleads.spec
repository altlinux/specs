%define oname googleads

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1.git20140903
Summary: Google Ads Python Client Library
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/googleads
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/googleads/googleads-python-lib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The googleads Python Client Libraries support the following products:

* AdWords API
* DoubleClick for Advertisers API
* DoubleClick for Publishers API

%package -n python3-module-%oname
Summary: Google Ads Python Client Library
Group: Development/Python3

%description -n python3-module-%oname
The googleads Python Client Libraries support the following products:

* AdWords API
* DoubleClick for Advertisers API
* DoubleClick for Publishers API

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
%doc ChangeLog *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20140903
- Initial build for Sisyphus

