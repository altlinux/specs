%define pypi_name requestsexceptions

Name: python3-module-%pypi_name
Version: 1.1.3
Release: alt2
Summary: Import exceptions from potentially bundled packages in requests
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 1.6

%description
The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult.  This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- Drop python2 support.

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- Initial packaging
