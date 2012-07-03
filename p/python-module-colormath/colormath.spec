%define oname colormath

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt2.git20110928
Summary: Python module that abstracts common color math operations
License: GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/colormath
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gtaylor/python-colormath.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
This module implements a large number of different color operations such
as color space conversions, Delta E, and density to spectral.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 module that abstracts common color math operations
Group: Development/Python3

%description -n python3-module-%oname
This module implements a large number of different color operations such
as color space conversions, Delta E, and density to spectral.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt examples tests
%python3_sitelibdir/*
%endif

%changelog
* Sat May 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20110928
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20110928
- Initial build for Sisyphus

