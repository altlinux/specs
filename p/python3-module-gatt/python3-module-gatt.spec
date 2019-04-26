%define  modulename gatt

Name:    python3-module-%modulename
Version: 0.2.6
Release: alt1

Summary: Bluetooth GATT SDK for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/getsenic/gatt-python

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  gatt-python-%version.tar

%description
The Bluetooth GATT SDK for Python helps you implementing and
communicating with any Bluetooth Low Energy device that has a GATT
profile. As of now it supports:

- Discovering nearby Bluetooth Low Energy devices
- Connecting and disconnecting devices
- Implementing your custom GATT profile
- Accessing all GATT services
- Accessing all GATT characteristics
- Reading characteristic values
- Writing characteristic values
- Subscribing for characteristic value change notifications

%prep
%setup -n gatt-python-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/gattctl
%python3_sitelibdir/%modulename/
%python3_sitelibdir/gattctl.py
%python3_sitelibdir/__pycache__/gattctl.cpython*
%python3_sitelibdir/*.egg-info

%changelog
* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 0.2.6-alt1
- Initial build for Sisyphus.
