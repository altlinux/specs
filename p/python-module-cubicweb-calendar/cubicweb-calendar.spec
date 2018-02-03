%define _unpackaged_files_terminate_build 1
%define oname cubicweb-calendar
Name: python-module-%oname
Version: 0.9.0
Release: alt1.1
Summary: calendar component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-calendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://hg.logilab.org/review/cubes/calendar
Source0: https://pypi.python.org/packages/d6/9d/34dff27c1d4f634a486174aabe246f5b159eaba73a991ffd33d9d424cb15/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-yams

Requires: cubicweb
%py_requires yams

%description
This cube models calendars with different types of days (working,
non-working, vacation, sick, etc) and time periods (from simple "Aug
31st 2009 to Sep 4th 2009" to repetitive ones like "July 14th").

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

