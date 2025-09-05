%define _unpackaged_files_terminate_build 1

Name: liquidctl
Version: 1.15.0
Release: alt0.2
Summary: Cross-platform tool and drivers for liquid coolers and other devices
Group: System/Configuration/Hardware

License: GPL-3.0
Url: https://github.com/liquidctl/liquidctl
Vcs: https://github.com/liquidctl/liquidctl
Source0: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel libusb-devel

Requires: python3-module-i2c-tools python3-module-hid-tools

BuildArch: noarch

%description
Cross-platform CLI and Python drivers for AIO liquid coolers and other devices

%package -n python3-module-%name
Summary: Python3 module for %name
Group: Development/Python3

%description -n python3-module-%name
Python3 module for %name

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -m 644 -pD %name.8 %buildroot%_man8dir/%name.8

%files
%doc README.md SECURITY.md CHANGELOG.md LICENSE.txt
%_bindir/%name
%_man8dir/%name.*

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}*dist-info

%changelog
* Fri Sep 05 2025 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt0.2
- added missing python3-module-hid-tools dependency (closes #55882).

* Sun Jun 01 2025 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt0.1
- Initial build for ALTLinux.

