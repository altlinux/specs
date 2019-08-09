%define modulename Geraldo

Name: python-module-%modulename
Summary: Geraldo is a reports engine for Python and Django applications
Version: 0.4.17
Release: alt1
Group: Development/Python
License: LGPL
URL: http://www.geraldoreports.org
Source: %modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%description
Geraldo is a Python and Django pluggable application
that works with ReportLab to generate complex reports.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%changelog
* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.17-alt1
- Initial build for ALT
