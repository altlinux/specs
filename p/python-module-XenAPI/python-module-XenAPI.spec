%define modulename XenAPI

Name: python-module-%modulename
Summary: XenAPI SDK
Version: 1.2
Release: alt1
Group: Development/Python
License: LGPL 2.1
URL: http://community.citrix.com/display/xs/Download+SDKs
Source: %modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%description
XenAPI SDK, for communication with Citrix XenServer and Xen Cloud Platform.
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

%changelog
* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial build for ALT
