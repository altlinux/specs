Name: kernel-source-bcmdhd
Version: 101.10.591.52.27
Release: alt1

Summary: Source for BCMDHD module
License: GPLv2
Group: Development/Kernel

URL: https://github.com/armbian/bcmdhd-dkms
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

# https://github.com/armbian/bcmdhd-dkms/archive/refs/tags/%version-4/bcmdhd-dkms-%version-4.tar.gz
Source: bcmdhd-dkms-%version-4.tar

BuildArch: noarch

BuildRequires(pre): kernel-build-tools

%description
Source code for wireless adapters based on the Broadcom ap6xxx chipset.

%prep
%setup -c
%__mv bcmdhd-dkms-%version-4/src %name-%version

%install
%__mkdir_p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Mar 14 2025 Nazarov Denis <nenderus@altlinux.org> 101.10.591.52.27-alt1
- Initial build for ALT Linux
