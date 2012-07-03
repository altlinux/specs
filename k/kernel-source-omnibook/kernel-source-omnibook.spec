Name: kernel-source-omnibook
Version: 20090714 
Release: alt1

Summary: Kernel module for some Toshiba and HP laptops
License: GPL
Group: Development/Kernel
URL: http://omnibook.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This package is intended to provide Linux kernel support for HP OmniBook,
HP Pavilion, Toshiba Satellite, Tecra, Equium and Compal laptops.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090714-alt1
- updated from git 

* Sat Mar 22 2008 Igor Zubkov <icesik@altlinux.org> 0.0-alt1.r274
- build for Sisyphus


