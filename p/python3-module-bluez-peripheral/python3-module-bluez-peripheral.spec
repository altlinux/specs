%define _unpackaged_files_terminate_build 1
%define pypi_name bluez-peripheral
%define mod_name bluez_peripheral

Name: python3-module-%pypi_name
Version: 0.1.7
Release: alt1

Summary: A library for building BLE peripherals using GATT and bluez
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/bluez-peripheral/
Vcs: https://github.com/spacecheese/bluez_peripheral
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyproject-installer
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

Requires: python3-module-dbus-next

%description
A bluez-peripheral is a library for building Bluetooth Low Energy (BLE)
peripherals/servers using the Bluez (Linux) GATT API. It wraps the
org.bluez D-Bus interfaces (GattManager1, LEAdvertisingManager1,
AgentManager1) to register custom GATT services/characteristics and LE
advertisements without going through BlueZ's D-Bus API by hand.

%prep
%setup -q

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install
# Upstream's setup.cfg excludes the top-level "tests" package but not its
# "tests.gatt" subpackage (a bug in their `exclude = tests` find() filter),
# so the published wheel leaks tests/gatt/* into site-packages -- confirmed
# by inspecting the actual PyPI wheel, not specific to this build. Strip it
# so we don't ship someone else's test fixtures under a generic "tests"
# top-level name in a shared site-packages directory.
rm -rf %buildroot%python3_sitelibdir_noarch/tests

%check
# The test suite talks to a live org.bluez GATT/Advertising service over
# the system D-Bus (see tests/util.py: BusManager), which is not present
# in a build chroot -- there is no bluetoothd/hci adapter to register
# against.

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 06 2026 Ivan Alekseev <qwetwe@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus.
