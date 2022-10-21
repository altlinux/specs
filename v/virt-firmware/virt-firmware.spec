
Name: virt-firmware
Version: 1.5
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

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-virt-firmware
%doc README.md
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Oct 21 2022 Alexey Shabalin <shaba@altlinux.org> 1.5-alt1
- new version 1.5

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.4-alt1
- new version 1.4

* Wed Aug 10 2022 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial package.

