%define module_name rtl8188eu
%define git_rev 163badb

Name: kernel-source-%module_name
Version: 5.13.3
Release: alt1.git%git_rev

Summary: Realtek RTL8188EU Wireless Lan Driver for Linux
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/ivanovborislav/rtl8188eu

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
* Tue May 16 2023 Andrey Cherepanov <cas@altlinux.org> 5.13.3-alt1.git163badb
- Initial build for Sisyphus.
