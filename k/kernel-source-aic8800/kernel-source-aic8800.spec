%define _customdocdir %_defaultdocdir/%module_name

%define module_name aic8800
%define module_version 0.0.40.3a09
%define module_release alt1

Name: kernel-source-%module_name
Version: %module_version
Release: %module_release

Summary: %module_name kernel module

License: GPL-2.0-only
Group: Development/Kernel
URL: https://github.com/shenmintao/aic8800d80
VCS: https://github.com/shenmintao/aic8800d80

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar

Patch0: aic8800-%version-%release.patch

BuildArch: noarch

Provides: kernel-source-%module_name-%module_version

BuildRequires(pre): rpm-build-kernel

%description
Linux driver for AICSemi AIC8800DC, ID a69c:88de.

%package -n %module_name-kernel-conf
Group: System/Kernel and hardware
Summary: %module_name kernel modules configuration
BuildArch: noarch

%description -n %module_name-kernel-conf
Configuration for %module_name kernel modules.

%package -n %module_name-kernel-extras
Group: Development/Kernel
Summary: Additional files for %summary
BuildArch: noarch

%description -n %module_name-kernel-extras
Documentation and helper scripts for %summary.

%prep
%setup -c -q
pushd %name-%version
%patch0 -p1
cd drivers/aic8800/
sed -i '/\/sbin\/depmod/d' Makefile
popd

%install
install -m644 -pD %name-%version/aic.rules %buildroot%_udevrulesdir/aic.rules

mkdir -p %buildroot%_customdocdir
install -m644 -p %name-%version/README.md %buildroot%_customdocdir

mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %module_name-kernel-conf
%_udevrulesdir/aic.rules

%files -n %module_name-kernel-extras
%_customdocdir

%changelog
* Tue Jan 13 2026 Leontiy Volodin <lvol@altlinux.org> 0.0.40.3a09-alt1
- New version 0-40-g3a0945b.
- Switch to more actual upstream (ALT #57409).

* Thu Aug 28 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.4.b4e4-alt1
- Initial build for ALT Sisyphus (ALT #55709).
