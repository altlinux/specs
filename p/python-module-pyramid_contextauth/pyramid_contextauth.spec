%define oname pyramid_contextauth

%def_with python3

Name: python-module-%oname
Version: 0.7.3
Release: alt1.git20140826
Summary: Pyramid security extension to register multiple contexts based authentication policies
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_contextauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hadrien/pyramid_contextauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-d2to1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPReReq: python3-module-d2to1
%endif

%description
A simple pyramid extension to register contexts based authentication
policy. Introspectables for policies registered are added to
configuration and will appear in debugtoolbar with their associated
contexts.

%package -n python3-module-%oname
Summary: Pyramid security extension to register multiple contexts based authentication policies
Group: Development/Python3

%description -n python3-module-%oname
A simple pyramid extension to register contexts based authentication
policy. Introspectables for policies registered are added to
configuration and will appear in debugtoolbar with their associated
contexts.

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
%doc *.rst example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20140826
- Initial build for Sisyphus

