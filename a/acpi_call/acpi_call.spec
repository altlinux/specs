Name: acpi_call
Version: 0.1
Release: alt3

Summary: scripts for disabling discrete GPU on some laptops
License: GPL
Group: System/Kernel and hardware

URL: https://github.com/mkottman/acpi_call

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This package is intended to provide Linux kernel support for
power control of nvidia gpu on Optimus' enabled laptops.

%package -n kernel-source-%name
Summary: %name kernel module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
sources for building %name kernel module

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
install -pD -m755 examples/*.sh %buildroot%_datadir/%name

mkdir -p %kernel_srcdir
cd ..
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%doc README.md
%_datadir/%name

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Oct 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- build with kernel 3.17 fixed

* Tue Jul 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- updated from github/mkottman/acpi_call

* Fri Apr 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1
- initial build
