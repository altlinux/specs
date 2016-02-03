%define module_name	mt7601u
%define module_version	2015.09.24
%define real_version	2015.09.24

Name: kernel-source-%module_name
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: Kernel module sources for MediaTek MT7601U Wi-Fi USB dongle
License: GPL
Group: Development/Kernel
Url: https://github.com/kuba-moo/mt7601u.git
Packager: Motsyo Gennadi <drool@altlinux.ru> 2015.09.24-alt1

Source0: %module_name-%real_version.tar.xz

ExclusiveArch: i586 x86_64
BuildPreReq: kernel-build-tools
BuildArch: noarch

%description
MediaTek MT7601U Wi-Fi USB dongle module sources for Linux kernel.

%prep
%setup -c
#__mv %module_name-%real_version %name-%version

%install
%__mkdir_p %kernel_srcdir
%__tar jcf %kernel_srcdir/%name-%version.tar.bz2 %module_name/

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Feb 03 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2015.09.24-alt1
- forward-port to sisyphus

* Sat Jan 30 2016 Motsyo Gennadi <drool@altlinux.ru> 2015.09.24-alt0.M70P.1
- initial build for ALT Linux 7
