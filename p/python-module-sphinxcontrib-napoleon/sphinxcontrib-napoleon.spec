%define mname sphinxcontrib
%define oname %mname-napoleon

%def_disable check

Name: python-module-%oname
Version: 0.2.11
Release: alt1.1
Summary: Sphinx "napoleon" extension
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-napoleon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-nose
BuildPreReq: python-module-sphinx python-module-docutils
BuildPreReq: python-module-Paver python-module-coverage
BuildPreReq: python-module-flake8 python-module-mock

%py_provides %mname.napoleon
%py_requires %mname

%description
Sphinx "napoleon" extension.

%prep
%setup

rm -fR *.egg-info

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc CHANGES *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.11-alt1
- Version 0.2.11

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus

