%define _unpackaged_files_terminate_build 1
%define oname cubicweb-timesheet
Name: python-module-%oname
Version: 0.15.2
Release: alt2.1
Summary: Record who did what and when for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-timesheet/

Source: %{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-module-setuptools cubicweb
BuildRequires: python-module-cubicweb-calendar
BuildRequires: python-module-cubicweb-workorder
BuildRequires: python-module-cubicweb-rqlcontroller

Requires: cubicweb python-module-cubicweb-calendar
Requires: python-module-cubicweb-workorder
Requires: python-module-cubicweb-rqlcontroller

%description
This cube is for tracking resource availability and usage (persons and
their daily activities, meeting rooms and their occupancy, etc.).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.2-alt2
- Updated dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.15.2-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus

