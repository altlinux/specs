%define oname requestsexceptions

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: Import exceptions from potentially bundled packages in requests

Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/requestsexceptions

Source: %oname-%version.tar
Source1: %oname.watch

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
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Build new version.

* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- Drop python2 support.

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- Initial packaging
