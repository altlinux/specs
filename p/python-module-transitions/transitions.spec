%define oname transitions

%def_with python3

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20150114.1.1
Summary: A lightweight, object-oriented Python state machine implementation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/transitions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tyarkoni/transitions.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
A lightweight, object-oriented finite state machine implementation in
Python.

%package -n python3-module-%oname
Summary: A lightweight, object-oriented Python state machine implementation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A lightweight, object-oriented finite state machine implementation in
Python.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1.git20150114.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20150114
- Initial build for Sisyphus

