%define oname lxc

Name: python3-module-%oname
Version: 5.0.0
Release: alt1.1

Summary: This repository provides python3 bindings for the LXC container API.

License: LGPLv2+
Group: Development/Python3
URL: https://pypi.org/project/lxc
VCS: https://github.com/lxc/python3-lxc

Source: %name-%version.tar

BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-wheel
BuildRequires:  lxc-devel
BuildRequires:  gcc

%description
Linux Resource Containers provide process and resource isolation
without the overhead of full virtualization. The python3-module-lxc 
package contains the Python3 binding for LXC.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md examples COPYING
%python3_sitelibdir/%oname
%python3_sitelibdir/_lxc.abi3.so
%python3_sitelibdir/python3_lxc-%version.dist-info

%changelog
* Mon Jul 06 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 5.0.0-alt1.1
- NMU: pack *.abi3.so extension module instead of *.cpython-*.so

* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Thu Nov 05 2020 Alexandr Antonov <aas@altlinux.org> 3.0.4-alt2
- fix url for *.spec

* Tue Nov 03 2020 Alexandr Antonov <aas@altlinux.org> 3.0.4-alt1
- initial build for ALT
