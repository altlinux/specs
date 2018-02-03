%define oname cubicweb-treeview
Name: python-module-%oname
Version: 0.1.1
Release: alt1.1
Summary: Tree-building adapters, widgets, views
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-treeview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-cubicweb
BuildPreReq: python-module-logilab-constraint

Requires: cubicweb

%description
Tree-building adapters, widgets.

This cube replace the Cubicweb treeview functionalities.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

