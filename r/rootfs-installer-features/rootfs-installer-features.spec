
%define _unpackaged_files_terminate_build 1

Name: rootfs-installer-features
Version: 0.2
Release: alt1

Summary: Run installer features during install via rootfs
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator
#Requires: alterator-setup => 0.3.3
Conflicts: installer-common-stage2 livecd-installer-features

%description
%summary

%prep
%setup

%install
install -pDm644 -t %buildroot/%_sbindir scripts/install2-*-functions

mkdir -p %buildroot%_alterator_libdir
cp -a hooks %buildroot%_alterator_libdir/

%files
%_sbindir/install2-*-functions
%_alterator_libdir/hooks/*/*

%changelog
* Thu Dec 30 2021 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- install2-action-functions: do not require /etc/sysconfig/init (startup)

* Thu Dec 12 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- not requires alterator-setup

* Fri Dec 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1
- initial build
