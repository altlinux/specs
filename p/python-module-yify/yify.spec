%define oname yify

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20140630
Summary: A Python module to get yify-torrents.com content from their API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Yify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tistaharahap/yify-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-requests
%endif

%py_provides %oname

%description
Yify provides a Python interface to interact with Yify Torrent's API.

%package -n python3-module-%oname
Summary: A Python module to get yify-torrents.com content from their API 
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Yify provides a Python interface to interact with Yify Torrent's API.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140630
- Initial build for Sisyphus

