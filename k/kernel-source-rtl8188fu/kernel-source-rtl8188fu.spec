%define module_name rtl8188fu
%define git_rev dfe0a50

Name: kernel-source-%module_name
Version: 1.0
Release: alt4.git%git_rev

Summary: Realtek 8188F USB WiFi adapter driver
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/brektrou/rtl8821CU

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
* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt4.gitdfe0a50
- Fixed build for kernel 5.18.

* Wed Nov 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt3.gite9b34e3
- Upstream support of kernel 5.15.

* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2.git21813e9
- Upstream support of kernel 5.10.

* Fri Oct 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1.gitb01ebdf
- Initial build for Sisyphus.
