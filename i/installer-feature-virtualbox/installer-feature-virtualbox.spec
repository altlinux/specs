Name: installer-feature-virtualbox
Version: 0.1
Release: alt1

Summary: Add kvm.enable_virt_at_load=0 to kernel cmdline for Virtualbox support
License: GPL-2.0-or-later
Group: System/Kernel and hardware

Url: https://altlinux.org/Virtualbox
Source: %name-%version.tar

ExclusiveArch: x86_64

%description
%summary.
Required for Linux kernel >= 6.12.

%prep
%setup

%install
%makeinstall

%files
%_datadir/install2/preinstall.d/*

%changelog
* Tue Dec 17 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
