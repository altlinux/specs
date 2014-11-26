%define oname parse

%def_with python3

Name: python-module-%oname
Version: 1.6.5
Release: alt1.git20141117
Summary: parse() is the opposite of format()
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/parse
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/r1chardj0n3s/parse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Parse strings using a specification based on the Python format() syntax.

%package -n python3-module-%oname
Summary: parse() is the opposite of format()
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Parse strings using a specification based on the Python format() syntax.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
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
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1.git20141117
- Initial build for Sisyphus

