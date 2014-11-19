%define oname termcolor

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20130510
Summary: ANSII Color formatting for output in terminal
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/termcolor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/edmund-huber/termcolor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
ANSII Color formatting for output in terminal.

%package -n python3-module-%oname
Summary: ANSII Color formatting for output in terminal
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
ANSII Color formatting for output in terminal.

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

%check
python %oname.py
%if_with python3
pushd ../python3
python3 %oname.py
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130510
- Initial build for Sisyphus

