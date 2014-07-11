%define oname crank

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1
Summary: Generalization of dispatch mechanism for use across frameworks
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/crank/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Generalization of dispatch mechanism for use across frameworks.

%package -n python3-module-%oname
Summary: Generalization of dispatch mechanism for use across frameworks
Group: Development/Python3

%description -n python3-module-%oname
Generalization of dispatch mechanism for use across frameworks.

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

