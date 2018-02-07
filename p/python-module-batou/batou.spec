%define oname batou
Name: python-module-%oname
Version: 1.0
Release: alt1.b31.1
Summary: Automating multi-host, multi-environment software builds and deployments
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/batou/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-jinja2
BuildPreReq: python-module-requests python-module-execnet
BuildPreReq: python-module-mock
BuildPreReq: python-module-pytest

%py_provides %oname
%py_requires jinja2 requests execnet

%description
batou is a multi-(component|host|environment|...) deployment utility.

Deployments are described in a model using "components" and can be
deployed locally and remotely. Models are written as Python code.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock

%description tests
batou is a multi-(component|host|environment|...) deployment utility.

Deployments are described in a model using "components" and can be
deployed locally and remotely. Models are written as Python code.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt README
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/example

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/example

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.b31.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b31
- Initial build for Sisyphus

