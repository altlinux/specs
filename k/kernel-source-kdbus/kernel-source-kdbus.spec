Name: kernel-source-kdbus
Version: 20140919 
Release: alt1

Summary: in-kernel dbus implementation
License: GPL
Group: Development/Kernel
URL: https://github.com/gregkh/kdbus
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
In-kernel dbus implementation

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Sep 19 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140919-alt1
- first build

