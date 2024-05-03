
Name: virt-firmware
Version: 24.4
Release: alt1
Summary: Tools for virtual machine firmware volumes
Group: Emulators
License: GPL-2.0-only
Url: https://gitlab.com/kraxel/virt-firmware
Vcs: https://gitlab.com/kraxel/virt-firmware.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-systemd
BuildRequires: python3(setuptools) python3(wheel) python3(cryptography)

%description
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n python3-module-virt-firmware
Summary: Tools for virtual machine firmware volumes
Group: Development/Python3
Provides: %name = %EVR
Provides: python3-module-virt-firmware-peutils = %EVR
Obsoletes: python3-module-virt-firmware-peutils < %EVR

%description -n python3-module-virt-firmware
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package tests
Summary: %summary - test cases
Group: Development/Other
Requires: python3-module-virt-firmware
Requires: edk2-ovmf

%description tests
test cases

%package -n uki-direct
Group: System/Base
Summary: %summary - manage UKI kernels.
Provides: ukidirect = %EVR
Requires: python3-module-virt-firmware
Conflicts: systemd < 254

%description -n uki-direct
kernel-install plugin and systemd unit to manage automatic
UKI (unified kernel image) updates.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install
# manpages
install -m 755 -d %buildroot%_man1dir
install -m 644 man/*.1 %buildroot%_man1dir

# tests
mkdir -p %buildroot%_datadir/%name
cp -ar tests %buildroot%_datadir/%name

# uki-direct
install -m 755 -d %buildroot%_unitdir
install -m 755 -d %buildroot%prefix/lib/kernel/install.d
install -m 644 systemd/kernel-bootcfg-boot-successful.service %buildroot%_unitdir
install -m 755 systemd/99-uki-uefi-setup.install %buildroot%prefix/lib/kernel/install.d

%post -n uki-direct
%post_systemd kernel-bootcfg-boot-successful.service

%preun -n uki-direct
%preun_systemd kernel-bootcfg-boot-successful.service

%files -n python3-module-virt-firmware
%doc README.md
%_bindir/*
%_man1dir/*.1*
%python3_sitelibdir/*

%files tests
%_datadir/%name/tests

%files -n uki-direct
%_unitdir/kernel-bootcfg-boot-successful.service
%prefix/lib/kernel/install.d/99-uki-uefi-setup.install

%changelog
* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 24.4-alt1
- New version 24.4.

* Thu Jan 25 2024 Alexey Shabalin <shaba@altlinux.org> 24.1.1-alt1
- new version 24.1.1
- merge python3-module-virt-firmware-peutils to python3-module-virt-firmware
- add uki-direct package

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.8-alt1
- new version 1.8

* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 1.6-alt1
- new version 1.6

* Fri Oct 21 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- new version 1.5

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.4-alt1
- new version 1.4

* Wed Aug 10 2022 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial package.

