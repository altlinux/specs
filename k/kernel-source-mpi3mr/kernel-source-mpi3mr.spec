%define module_name    mpi3mr
%define module_version 8.10.0.5.0

Name: kernel-source-%module_name
Version: %module_version
Release: alt1

Summary: Broadcom Limited Avenger MR8.10 Linux Driver
URL: https://docs.broadcom.com/docs/LINUX_DRIVER_8.10.0.5.0-1.zip
Group: Development/Kernel
License: GPL-2.0

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %module_name-%version-src.tar.gz
Source1: 8.10-%version-1_Linux_DRV_readme.txt
Source2: README.pdf

BuildRequires(pre): rpm-build-kernel

%description
Broadcom Limited Avenger MR8.10 Linux Driver.

Supported Controllers
* Avenger 9600-16e
* Avenger 9600-8i8e
* Avenger 9600-16i
* Avenger 9600-24i
* Avenger 9600w-16e
* Avenger 9620-16i
* Avenger 9660-16i
* Avenger 9670W-16i
* Avenger 9670-24i

%prep
%setup -c
mv %module_name %name-%version
cp -a %SOURCE1 %SOURCE2 %name-%version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Oct 18 2024 Andrey Cherepanov <cas@altlinux.org> 8.10.0.5.0-alt1
- Initial build for Sisyphus.
