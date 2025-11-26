%define pypi_name gs_usb
Name:    python3-module-%pypi_name
Version: 0.3.0
Release: alt1
Summary: Python Windows/Linux/Mac CAN driver based on usbfs or WinUSB WCID
License: MIT
URL:     https://pypi.org/project/gs-usb
VCS:     https://github.com/jxltom/gs_usb
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Group: Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Python Windows/Linux/Mac CAN driver based on usbfs or WinUSB WCID for
Geschwister Schneider USB/CAN devices, candleLight USB CAN interfaces,
CAN Debugger devices and other interfaces utilising the gs_usb driver.

%prep
%setup -n %name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README*
%python3_sitelibdir/gs_usb-%version.dist-info
%python3_sitelibdir/gs_usb

%changelog
* Fri Oct 24 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.3.0-alt1
- Initial build.
