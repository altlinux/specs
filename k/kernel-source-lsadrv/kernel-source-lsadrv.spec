%define module_name lsadrv
%define module_version 2.0.1
%define module_release	alt5

%define module_source	%module_name-%module_version.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name modules sources for Hitachi StarBoard.
License: GPL
Group: Development/Kernel
URL: http://nixtech.ru/
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for Linux kernel.
This is usable for Hitachi StarBoard interactive whiteboard.
    FX-63/77(G)/82(WG) Wired
    FX-DUO-63/77/88W Wired
    FX-TRIO-77/77(S)/88W


%prep
%setup -n %module_name-%module_version

%install
%__mkdir_p %kernel_srcdir
cd ..
%__mv %module_name-%module_version kernel-source-%module_name-%module_version
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Sat Feb 5 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt5
- tar.xz replaceb by tar

* Sat Feb 5 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt4
- added provides section

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt3
- added interactive whiteboard to description

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt2
- changed packager to Kernel Maintainer Team

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt1
- initial build
