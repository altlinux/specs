# -*- rpm-spec -*-
%define module_name	ch341
%define module_version  1.0.0
%define git b3629c3

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: alt4.g%{git}
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

%prep
%setup -c -q

%install
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu Feb 20 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt4.gb3629c3
- Remove -blacklist (not needed since 5.17, closes #53159).

* Fri Dec 20 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt3.gb3629c3
- GIT b3629c3 (with kernel 6.11+ fixes).

* Mon Aug 12 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt2.g2e4bac9
- GIT 2e4bac9 (with kernel 6.9+ fixes).

* Thu Jun 20 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt1.g84b4b8c
- Initial build for ALTLinux.

