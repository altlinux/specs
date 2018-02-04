%define mname sphinxcontrib
%define oname %mname-cheeseshop
Name: python-module-%oname
Version: 0.2
Release: alt1.1
Summary: Sphinx extension cheeseshop
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-cheeseshop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %mname.cheeseshop
%py_requires %mname

%description
This extension adds directives for easy linking to Cheese Shop (Python
Package Index) packages.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

