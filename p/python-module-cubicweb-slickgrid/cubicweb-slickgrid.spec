%define _unpackaged_files_terminate_build 1
%define oname cubicweb-slickgrid
Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Table view rendered using the SlickGrid javascript library
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-slickgrid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/35/45/213861e2788f63f0aed9322d68f6fe5267acba7a05ac32dc638a3d0bc62d/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
SlickGrid is an advanced JavaScript grid/spreadsheet component.

This view accepts any non-empty rset. It uses introspection on the
result set to compute column names and the proper way to display the
cells.

It is highly configuration and accepts the same wealth of option than
cubicweb.web.view.tableview.RsetTableView.

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

