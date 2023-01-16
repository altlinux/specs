%define module_name rtl8723du
%define git_rev efcaffb

Name: kernel-source-%module_name
Version: 5.13.4
Release: alt3.git%git_rev

Summary: Realtek RTL8723DU WiFi adapter driver
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/lwfinger/rtl8723du

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 5.13.4-alt3.gitefcaffb
- Support for kernel 6.1.

* Mon Aug 29 2022 Andrey Cherepanov <cas@altlinux.org> 5.13.4-alt2.gite0129ae
- Support for kernel 5.19+

* Thu Jun 23 2022 Andrey Cherepanov <cas@altlinux.org> 5.13.4-alt1.gitb3d0f89
- Initial build for Sisyphus.
