%define modulename ovirt-engine-sdk

Name: python-module-%modulename
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.3.1
Release: alt1
Group: Development/Python
License: ASL 2.0
URL: http://ovirt.org
Source: %modulename-python-%version.tar.gz
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: libxml2-devel

%description
This package contains the Python 3 SDK for version 4 of the oVirt Engine
API.


%prep
%setup -n %modulename-python-%version

%build
%python_build

%install
%python_install

%files
%doc README.adoc
%doc examples
%python_sitelibdir/*

%changelog
* Thu Aug 08 2019 Alexey Shabalin <shaba@altlinux.org> 4.3.1-alt1
- Initial build for ALT

