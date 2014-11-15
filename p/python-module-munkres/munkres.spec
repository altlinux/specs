%define oname munkres

%def_with python3

Name: python-module-%oname
Version: 1.0.6
Release: alt1.git20131103
Summary: Munkres algorithm for the Assignment Problem
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/munkres/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bmc/munkres.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
The Munkres module provides an implementation of the Munkres algorithm
(also called the Hungarian algorithm or the Kuhn-Munkres algorithm),
useful for solving the Assignment Problem.

%package -n python3-module-%oname
Summary: Munkres algorithm for the Assignment Problem
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The Munkres module provides an implementation of the Munkres algorithm
(also called the Hungarian algorithm or the Kuhn-Munkres algorithm),
useful for solving the Assignment Problem.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The Munkres module provides an implementation of the Munkres algorithm
(also called the Hungarian algorithm or the Kuhn-Munkres algorithm),
useful for solving the Assignment Problem.

This package contains documentation for %oname.

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

epydoc %oname

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python %oname.py
%if_with python3
pushd ../python3
python3 %oname.py
popd
%endif

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%files docs
%doc html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20131103
- Initial build for Sisyphus

