%define oname green

%def_with python3

Name: python-module-%oname
Version: 1.4.4
Release: alt1.git20140826
Summary: Clean, colorful test runner for Python unit tests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/green/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/CleanCut/green.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

%package -n python3-module-%oname
Summary: Clean, colorful test runner for Python unit tests
Group: Development/Python3

%description -n python3-module-%oname
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc CHANGELOG *.rst *.md *.txt example
%_bindir/%oname
%_bindir/%{oname}2*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst *.md *.txt example
%_bindir/%{oname}3*
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.git20140826
- Initial build for Sisyphus

