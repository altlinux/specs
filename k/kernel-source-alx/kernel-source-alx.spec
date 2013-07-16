Name: kernel-source-alx
Version: 20130405
Release: alt2

Summary: alx Ethernet driver
License: GPL
Group: Development/Kernel
URL: http://sourceforge.net/projects/ipt-netflow/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
The alx driver provide support for:
* AR8161 Gigabit Ethernet
* AR8162 Fast Ethernet
* QCA8171 Gigabit Ethernet
* QCA8172 Fast Ethernet


%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
mv %name-%version alx-%version
tar -cjf %kernel_srcdir/alx-%version.tar.bz2 alx-%version

%files
%attr(0644,root,root) %kernel_src/alx-%version.tar.bz2

%changelog
* Tue Jul 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130405-alt2
- merge github/hauke/kernel-3.10-fixes

* Tue May 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130405-alt1
- build as separate module 

