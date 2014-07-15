%define oname apiclient

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt2

Summary: Framework for making good API client libraries using urllib3
License: MIT
Group: Development/Python

Url: https://pypi.python.org/pypi/apiclient/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%setup_python_module %oname

%description
Framework for making good API client libraries using urllib3.

%package -n python3-module-%oname
Summary: Framework for making good API client libraries using urllib3
Group: Development/Python3

%description -n python3-module-%oname
Framework for making good API client libraries using urllib3.

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

