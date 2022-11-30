
Name: virt-firmware
Version: 1.6
Release: alt1
Summary: Tools for virtual machine firmware volumes
Group: Emulators
License: GPLv2
Url: https://gitlab.com/kraxel/virt-firmware
Vcs: https://gitlab.com/kraxel/virt-firmware.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel)

%description
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n python3-module-virt-firmware
Summary: Tools for virtual machine firmware volumes
Group: Development/Python3
Provides: %name = %EVR

%description -n python3-module-virt-firmware
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n python3-module-virt-firmware-peutils
Summary: %summary - peutils
Group: Development/Python3
Conflicts: python3-module-virt-firmware < 1.6

%description -n python3-module-virt-firmware-peutils
Some utilities to inspect efi (pe) binaries.

%package tests
Summary: %summary - test cases
Group: Development/Other
Requires: python3-module-virt-firmware
Requires: edk2-ovmf

%description tests
test cases

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

%files -n python3-module-virt-firmware
%doc README.md
%_bindir/host-efi-vars
%_bindir/virt-fw-dump
%_bindir/virt-fw-vars
%_bindir/virt-fw-sigdb
%_bindir/migrate-vars
%_man1dir/virt-*.1*
%python3_sitelibdir/virt/firmware
%python3_sitelibdir/virt_firmware-*

%files -n python3-module-virt-firmware-peutils
%python3_sitelibdir/virt/peutils
%_bindir/pe-dumpinfo
%_bindir/pe-listsigs
%_bindir/pe-addsigs

%files tests
%_datadir/%name/tests

%changelog
* Wed Nov 30 2022 Alexey Shabalin <shaba@altlinux.org> 1.6-alt1
- new version 1.6

* Fri Oct 21 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- new version 1.5

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.4-alt1
- new version 1.4

* Wed Aug 10 2022 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial package.

