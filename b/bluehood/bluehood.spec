Name: bluehood
Version: 0.3.5
Release: alt1

Summary: Monitor your local neighbourhood's bluetooth activity
License: MIT
Group: Monitoring

Url: https://github.com/dannymcc/bluehood
Vcs: https://github.com/dannymcc/bluehood

Requires: python3-module-mac-vendor-lookup

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

%description
Bluetooth Neighborhood - Track BLE devices in your area and analyze traffic patterns.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%{name}-*

%changelog
* Sat Feb 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.3.5-alt1
- Initial build for ALT Linux.

