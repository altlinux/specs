%define module_name yt6801
%define archive_name yt6801-linux-driver-%version

Name: kernel-source-%module_name
Version: 1.0.31
Release: alt2

Summary: Driver for Motorcomm YT6801 ethernet adapter
License: GPL-2.0
Group: Development/Kernel
URL: https://www.motor-comm.com/product/ethernet-control-chip

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %archive_name.tar
Patch1: yt6801-alt-6.18-compat.patch
Patch2: yt6801-alt-options.patch

BuildRequires(pre): rpm-build-kernel

%description
%summary.

%prep
%setup -c
pushd %archive_name
%autopatch -p2
popd

# this source package losely follows the original driver naming
# but for consistency with other kernel moudles we rename
# the directory here
mv %archive_name %name-%version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Mar 13 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.31-alt2
- fix building on 6.18
- enable debug output and moderating by default

* Fri Mar 13 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.31-alt1
- 1.0.31

* Mon Mar 17 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.29-alt1
- initial build for ALT
