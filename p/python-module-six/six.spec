%define oname six

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2
Summary: Python 2 and 3 compatibility utilities
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/six
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.

%if_with python3
%package -n python3-module-%oname
Summary: Python 2 and 3 compatibility utilities
Group: Development/Python3

%description -n python3-module-%oname
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.
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
%python3_build
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
%doc README documentation/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README documentation/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

