%define module_name rtl8821cu
%define git_rev f1bc7e8

Name: kernel-source-%module_name
Version: 5.4.1
Release: alt3.git%git_rev

Summary: Realtek RTL8811CU/RTL8821CU USB wifi adapter driver
Group: Development/Kernel
License: GPL-2.0
URL: https://github.com/brektrou/rtl8821CU

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
# https://github.com/brektrou/rtl8821CU/pull/134
Patch: kernel-5.12-support.patch

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%prep
%setup -c
%patch -p1 -d %name-%version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon May 24 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt3.gitf1bc7e8
- Upstream support of kernel 5.12.

* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2.gitdeff094
- Upstream support of kernel 5.10.

* Fri Oct 30 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1.git45a8b43
- Initial build for Sisyphus.
