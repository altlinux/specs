%define module_name txgbe

%define _customdocdir %_defaultdocdir/%module_name
%define _unpackaged_files_terminate_build 1

Name: kernel-source-%module_name
Version: 1.3.6.9
Release: alt1

Summary: Wangxun 10 Gigabit Ethernet driver
License: GPL-2.0
Group: Development/Kernel

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %module_name-%version.zip
Patch:  %module_name-%version-%release.patch

BuildRequires(pre): rpm-build-kernel
BuildRequires: /usr/bin/unzip

%description
Sources for Wangxun 10 Gigabit Ethernet driver from the vendor.


%package -n %module_name-extras
Group: Development/Kernel
Summary: Additional files for Wangxun 10 Gigabit Ethernet driver

%description -n %module_name-extras
Documentation and helper scripts for vendor's version
of  Wangxun 10 Gigabit Ethernet driver.


%prep
%setup -c
mv %module_name-%version %name-%version

pushd %name-%version 
%autopatch -p1
popd

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

mkdir -p %buildroot%_man7dir
cp %name-%version/txgbe.7 %buildroot%_man7dir/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %module_name-extras
%_man7dir/*
%doc %name-%version/release*.txt
%doc %name-%version/scripts/set_irq_affinity

%changelog
* Tue Mar 24 2026 Ivan A. Melnikov <iv@altlinux.org> 1.3.6.9-alt1
- 1.3.6.9
- linux 6.17+ compatibility

* Tue Jul 29 2025 Ivan A. Melnikov <iv@altlinux.org> 1.3.6.7-alt1
- initial build for ALT
