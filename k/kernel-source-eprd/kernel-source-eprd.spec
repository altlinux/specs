Name: kernel-source-eprd
Version: 0.5.0
Release: alt1

Summary: An eventually persistent ramdisk / disk cache
License: GNUv2
Group: Development/Kernel
URL: http://sourceforge.net/projects/eprd/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
An eventually persistent ramdisk / disk cache.
This project can be useful whenever one needs more IOPS
in a non critical environment. There is more to this
project though. I am working on a kernel based high
performance deduplicating block device. This project
will share code and ideas from EPRD as well as Lessfs.


%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Sep 02 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.0-alt1
- Inital build for ALT

