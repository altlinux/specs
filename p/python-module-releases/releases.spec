%define oname releases

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt2
Summary: A Sphinx extension for changelog manipulation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/releases/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

%package -n python3-module-%oname
Summary: A Sphinx extension for changelog manipulation
Group: Development/Python3

%description -n python3-module-%oname
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

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
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

