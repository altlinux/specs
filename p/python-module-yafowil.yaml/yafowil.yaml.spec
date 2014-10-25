%define mname yafowil
%define oname %mname.yaml
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20140818
Summary: Parse widget trees from YAML
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yafowil.yaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/yafowil.yaml.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-%mname-tests
BuildPreReq: python-module-yaml

%py_provides %oname
%py_requires %mname

%description
YAFOWIL - YAML parser for widget trees.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires %mname.tests

%description tests
YAFOWIL - YAML parser for widget trees.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20140818
- Initial build for Sisyphus

