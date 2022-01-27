%define modulename ovirt-engine-sdk

Name: python3-module-%modulename
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.5.0
Release: alt1
Group: Development/Python3
License: Apache-2.0
URL: http://ovirt.org
Source: %modulename-python-%version.tar.gz
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: libxml2-devel

%description
This package contains the Python 3 SDK for version 4 of the oVirt Engine
API.


%prep
%setup -c -n %modulename-python-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.adoc
%doc examples
%python3_sitelibdir/*

%changelog
* Thu Jan 27 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.5.0-alt1
- update to 4.5.0

* Mon Aug 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.4.14-alt1
- update to 4.4.14

* Mon Jun 28 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.4.13-alt1
- update to 4.4.13

* Fri May 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.4.12-alt1
- update to 4.4.12

* Mon Mar 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 4.4.10-alt1
- update to 4.4.10

* Wed Aug 14 2019 Andrew A. Vasilyev <andy@altlinux.org> 4.3.3-alt1
- update to 4.3.3

* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 4.3.1-alt1
- Initial build for ALT
