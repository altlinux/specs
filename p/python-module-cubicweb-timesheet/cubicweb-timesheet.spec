%define _unpackaged_files_terminate_build 1
%define oname cubicweb-timesheet
Name: python-module-%oname
Version: 0.15.2
Release: alt1
Summary: Record who did what and when for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-timesheet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/38/8d/d6982d4d20d5e81aa521fcbadfef7e0201b861781fd6d6a32e252eab3bb4/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-calendar
BuildPreReq: python-module-cubicweb-workorder

Requires: cubicweb python-module-cubicweb-calendar
Requires: python-module-cubicweb-workorder

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.15.2-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus

