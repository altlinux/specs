%define oname cubicweb-workorder
Name: python-module-%oname
Version: 0.11.2
Release: alt1.1
Summary: workorder component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-workorder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-iprogress

Requires: cubicweb python-module-cubicweb-iprogress

%description
This cube for models Orders and WorkOrders (an order can be split into
several workorders).

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
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1
- Initial build for Sisyphus

