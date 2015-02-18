%define oname cubicweb-slickgrid
Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Table view rendered using the SlickGrid javascript library
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-slickgrid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

Requires: cubicweb

%description
SlickGrid is an advanced JavaScript grid/spreadsheet component.

This view accepts any non-empty rset. It uses introspection on the
result set to compute column names and the proper way to display the
cells.

It is highly configuration and accepts the same wealth of option than
cubicweb.web.view.tableview.RsetTableView.

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
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

