%define git %nil
%define _unpackaged_files_terminate_build 1
%def_with test

Name: liquidctl
Version: 1.16.0
Release: alt1
Summary: Cross-platform tool and drivers for liquid coolers and other devices
Group: System/Configuration/Hardware

License: GPL-3.0
Url: https://github.com/liquidctl/liquidctl
Vcs: https://github.com/liquidctl/liquidctl
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel libusb-devel
%if_with test
BuildRequires: python3-module-pytest python3-module-pyusb python3-module-pillow python3-module-colorlog
BuildRequires: python3-module-cython-hidapi python3-module-crcmod python3-module-i2c-tools python3-module-docopt
%endif

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
%patch -p1

%build
%pyproject_build

%install
%pyproject_install
install -m 644 -pD %name.8 %buildroot%_man8dir/%name.8

%if_with test
%check
export XDG_RUNTIME_DIR=%buildroot/.test_rundir \
%pyproject_run_pytest
%endif

%files
%doc README.md SECURITY.md CHANGELOG.md LICENSE.txt
%_bindir/%name
%_man8dir/%name.*

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}*dist-info

%changelog
* Wed Mar 18 2026 L.A. Kostis <lakostis@altlinux.ru> 1.16.0-alt1
- 1.16.0.

* Mon Feb 02 2026 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt0.3.gd6568b1
- Update to v1.15.0-60-gd6568b1.
- Enable tests.

* Fri Sep 05 2025 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt0.2
- added missing python3-module-hid-tools dependency (closes #55882).

* Sun Jun 01 2025 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt0.1
- Initial build for ALTLinux.
