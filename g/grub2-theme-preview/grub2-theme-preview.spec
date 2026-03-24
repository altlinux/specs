%define modulename grub2_theme_preview

Name:    grub2-theme-preview
Version: 2.9.1
Release: alt1

Summary: Preview a full GRUB 2.x theme (or just a background image) using KVM / QEMU

License: GPLv2+
Group:   Development/Python3
URL:     https://pypi.org/project/grub2-theme-preview
VCS:     https://github.com/hartwork/grub2-theme-preview

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: grub-common-extra
Requires: qemu-kvm-core
Requires: qemu-ui-gtk

%description
It takes a theme folder (or just a single picture), creates a temporary
bootable image using grub2-mkrescue and launches that image in a virtual machine
using KVM/QEMU, all without root privileges.

%prep
%setup

# So user should not define G2TP_GRUB_LIB variable
sed -i "s|/usr/lib/grub|%_libdir/grub|" grub2_theme_preview/__main__.py

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Tue Mar 24 2026 Grigory Ustinov <grenka@altlinux.org> 2.9.1-alt1
- Initial build for Sisyphus.
