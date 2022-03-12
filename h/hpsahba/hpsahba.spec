Name: hpsahba
Version: 20210904
Release: alt1

Summary: Tool to enable/disable HBA mode on some HP Smart Array controllers

Group: System/Configuration/Hardware
License: GPLv2
Url: https://github.com/im-0/hpsahba

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/im-0/hpsahba.git
Source: %name-%version.tar

#BuildRequires: pandoc >= 2.9

BuildRequires: rpm-build-kernel

%define module_name     hpsa
%define module_version  %version

%description
hpsahba is able to enable or disable HBA mode on some HP Smart Array
controllers on which regular tools, like 'ssacli', reports HBA mode as not
supported.

%package -n dkms-hpsa
Summary: Patched hpsa DKMS package
Group: System/Configuration/Hardware
BuildArch: noarch

%description -n dkms-hpsa
Patched hpsa DKMS package.

Downloads and automatically patches hpsa driver from stable linux kernel tree.


%package -n kernel-source-%module_name
#Provides: kernel-source-%module_name-%module_version
Summary: %module_name module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%module_name
%module_name module sources for Linux kernel.

%prep
%setup
subst "s|/usr/lib/modules|/lib/modules|" contrib/dkms/Makefile

%build
%make_build

%install
install %name -D %buildroot%_sbindir/%name
install hpsahba.8 -m644 -D %buildroot%_man8dir/hpsahba.8

# dkms
mkdir -p %buildroot/usr/src/hpsa-dkms-1.0/
cp contrib/dkms/* %buildroot/usr/src/hpsa-dkms-1.0/
rm -f %buildroot/usr/src/hpsa-dkms-1.0/patch.sh

# kernel source
mkdir %module_name-%version/
cp contrib/dkms/* %module_name-%version/
rm -f %module_name-%version/patch.sh
mkdir -p %kernel_srcdir
tar jcf %kernel_srcdir/%module_name-%version.tar.bz2 %module_name-%version

%files
%doc README.md
%_sbindir/%name
%_man8dir/*

%files -n dkms-hpsa
/usr/src/hpsa-dkms-1.0/

%files -n kernel-source-%module_name
%attr(0644,root,root) %kernel_src/%module_name-%version.tar.bz2

%changelog
* Sun Mar 13 2022 Vitaly Lipatov <lav@altlinux.ru> 20210904-alt1
- new version (20210904) with rpmgs script

* Sun Aug 22 2021 Vitaly Lipatov <lav@altlinux.ru> 20201220-alt3
- BR: s/kernel-build-tools/rpm-build-kernel/

* Mon Apr 26 2021 Vitaly Lipatov <lav@altlinux.ru> 20201220-alt2
- don't use pandoc during build (too old on p9 and too complex to update)

* Mon Apr 26 2021 Vitaly Lipatov <lav@altlinux.ru> 20201220-alt1
- initial build for ALT Sisyphus
