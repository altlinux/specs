Name: python3-module-uart-devices
Version: 0.1.0
Release: alt1

Summary: UART Devices for Linux
License: MIT
Group: Development/Python
Url: https://pypi.org/bdraco/uart-devices

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/uart_devices
%python3_sitelibdir/uart_devices-%version.dist-info

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.0-alt1
- 0.1.0 released

