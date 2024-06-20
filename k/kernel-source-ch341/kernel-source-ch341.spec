# -*- rpm-spec -*-
%define module_name	ch341
%define module_version  1.0.0
%define git 84b4b8c

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt1.g%{git}
Provides: kernel-source-%module_name-%module_version
Summary: CH341 linux drivers for I2C / SPI and GPIO mode
License: GPLv2
Group: Development/Kernel
Url: https://github.com/frank-zago/ch341-i2c-spi-gpio
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
WinChipHead CH341 linux driver for I2C, SPI and GPIO mode

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
blacklist %{module_name}
EOF

install -m644 -pD blacklist-%{module_name}.conf %buildroot%_sysconfdir/modprobe.d/blacklist-%{module_name}.conf

mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %{module_name}-blacklist
%_sysconfdir/modprobe.d/blacklist-%{module_name}.conf

%changelog
* Thu Jun 20 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt1.g84b4b8c
- Initial build for ALTLinux.

