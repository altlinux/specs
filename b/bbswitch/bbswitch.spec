Name: bbswitch
Version: 0.4.1
Release: alt1

Summary: kernel support for power management of nVidia GPU on Optimus enabled laptops.
License: GPL
Group: System/Kernel and hardware

URL: https://github.com/Bumblebee-Project/bbswitch.git

Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
%name is a kernel module which automatically detects the required ACPI calls
for two kinds of Optimus laptops. It has been verified to work with "real"
Optimus and "legacy" Optimus laptops (at least, that is how I call them). The
machines on which these tests has performed are:

- Clevo B7130 - GT 425M ("real" Optimus, Lekensteyns laptop)
- Dell Vostro 3500 - GT 310M ("legacy" Optimus, Samsagax' laptop)

(note: there is no need to add more supported laptops here as the universal
calls should work for every laptop model supporting either Optimus calls)

It's preferred over manually hacking with the acpi_call module because it can
detect the correct handle preceding _DSM and has some built-in safeguards.

%package -n kernel-source-%name
Summary: %name kernel module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Sources for building %name kernel module

%prep
%setup

%install
mkdir -p %kernel_srcdir
cd ..
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2
%doc NEWS README.md

%changelog
* Tue Jan 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus

