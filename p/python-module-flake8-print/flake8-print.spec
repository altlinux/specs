%define oname flake8-print

%def_without python3

Name: python-module-%oname
Version: 1.5.0
Release: alt1.git20141104
Summary: Print statement checker plugin for flake8
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/flake8-print/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/JBKahn/flake8-print.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8 python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8 python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides flake8_print

%description
Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.

%package -n python3-module-%oname
Summary: Print statement checker plugin for flake8
Group: Development/Python3
%py3_provides flake8_print

%description -n python3-module-%oname
Check for Print statements in python files.

This module provides a plugin for ``flake8``, the Python code checker.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141104
- Initial build for Sisyphus

