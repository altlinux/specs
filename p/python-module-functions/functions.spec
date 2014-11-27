%define oname functions

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20141126
Summary: Functional programming in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/functions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/creese/functions.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Functional programming in Python.

%package -n python3-module-%oname
Summary: Functional programming in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Functional programming in Python.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141126
- Version 0.7.0

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20141116
- Initial build for Sisyphus

