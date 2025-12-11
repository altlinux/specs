Name: kernel-source-bcmdhd
Version: 101.10.591.52.27
Release: alt3

Summary: Source for BCMDHD module
License: GPLv2
Group: Development/Kernel

URL: https://github.com/armbian/bcmdhd-dkms
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

# https://github.com/armbian/bcmdhd-dkms/archive/refs/tags/%version-4/bcmdhd-dkms-%version-5.tar.gz
Source0: bcmdhd-dkms-%version-5.tar

Source1: blacklist-bcmdhd.conf

BuildArch: noarch

BuildRequires(pre): kernel-build-tools

%description
Source code for wireless adapters based on the Broadcom ap6xxx chipset.

%package -n bcmdhd-blacklist
Summary: Blacklist modules for BCMDHD
Group: System/Kernel and hardware

%description -n bcmdhd-blacklist
Blacklist modules for correctly working module BCMDHD

%prep
%setup -c
%__mv bcmdhd-dkms-%version-5/src %name-%version

%install
%__mkdir_p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/modprobe.d/blacklist-bcmdhd.conf

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n bcmdhd-blacklist
%dir %_sysconfdir/modprobe.d
%config %_sysconfdir/modprobe.d/blacklist-bcmdhd.conf

%changelog
* Thu Dec 11 2025 Nazarov Denis <nenderus@altlinux.org> 101.10.591.52.27-alt3
- Update to 101.10.591.52.27-5

* Sat Mar 15 2025 Nazarov Denis <nenderus@altlinux.org> 101.10.591.52.27-alt2
- Add blacklist for correctly working module

* Fri Mar 14 2025 Nazarov Denis <nenderus@altlinux.org> 101.10.591.52.27-alt1
- Initial build for ALT Linux
