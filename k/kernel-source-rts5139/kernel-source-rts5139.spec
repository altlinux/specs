# -*- rpm-spec -*-
%define module_name	rts5139
%define module_version  1.05
%define git fde2d2b

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: Realtek RTS5139/29 USB card reader driver
License: GPL-3
Group: Development/Kernel
Url: https://github.com/asymingt/rts5139.git
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
This is a temporary fix for RTS5129/RTS5139 USB MMC card reader on Linux 3.16+
kernels.

PLEASE USE THIS DRIVER ONLY IF YOU SEE ERRORS IN LOGS! Upstream rtsx_ should
work just fine.

%package -n %{module_name}-blacklist
Group: System/Kernel and hardware
Summary: Blacklist modules for correctly working module %{module_name}
BuildArch: noarch

%description -n %{module_name}-blacklist
Blacklist modules for correctly working module %{module_name}

%prep
%setup -c -q

%install
cat > blacklist-%{module_name}.conf << EOF
blacklist rtsx_usb_sdmmc
blacklist rtsx_usb_ms
blacklist rtsx_usb
EOF

install -m644 -pD blacklist-%{module_name}.conf %buildroot%_sysconfdir/modprobe.d/blacklist-%{module_name}.conf

mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %{module_name}-blacklist
%_sysconfdir/modprobe.d/blacklist-%{module_name}.conf

%changelog
* Mon Jun 17 2024 L.A. Kostis <lakostis@altlinux.ru> 1.05-alt1.gfde2d2b
- Initial build for ALTLinux.

