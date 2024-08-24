%define module_name     88x2bu
%define module_version  5.13.1
%define git_rev         3c8f59b

Name: kernel-source-%module_name
Version: %module_version
Release: alt1.git%git_rev

Summary: Linux Driver for USB WiFi Adapters that are based on the RTL8812BU and RTL8822BU Chipsets
URL: https://github.com/morrownr/88x2bu-20210702
Group: Development/Kernel
License: GPL-2.0

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%package -n %module_name-conf
Summary: %module_name configuration
Group: System/Kernel and hardware

%description -n %module_name-conf
Allow easy access to specific driver options for %module_name

%prep
%setup -c

%install
mkdir -p %buildroot%_sysconfdir/modprobe.d
install -pm644 %name-%version/%module_name.conf %buildroot%_sysconfdir/modprobe.d/
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n %module_name-conf
%dir %_sysconfdir/modprobe.d
%config %_sysconfdir/modprobe.d/%module_name.conf

%changelog
* Sat Aug 24 2024 L.A. Kostis <lakostis@altlinux.ru> 5.13.1-alt1.git3c8f59b
- Switch to alternate driver (from morrownr).
- rtl%module_name->%module_name.

* Thu Sep 14 2023 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt6.gite1e98a4
- Fixed build for kernel 6.5.2.

* Sat Apr 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt5.gitc866ad2
- Fixed build for kernel 6.1.

* Sun Jan 23 2022 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt4.gite3339ad
- Upstream fix for kernel-5.15.

* Tue Apr 06 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt3.gitaac7c35
- Fix build with kernel-5.12.

* Fri Mar 05 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt2.gitba12c4f
- Set upstream source to https://github.com/cilynx/rtl88x2bu.
- Build from upstream commit.

* Sat Oct 24 2020 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt1
- Initial build for Sisyphus.
