%define _unpackaged_files_terminate_build 1

Name: kernel-source-rtw88
Version: 0.0
Release: alt1.git.11d2944

Summary: Driver source code for Realtek RTL8814AU and RTL8814AE cards.
License: GPL-2.0
Group: Development/Kernel
Url: https://github.com/lwfinger/rtw88

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

BuildArch: noarch

%description
This package has v5 of the code, which is latest from Realtek by now.
This repository includes drivers for the following card:
Realtek 8852AE

%prep
%setup

%build

%install

tar xvf %SOURCE0
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Apr 01 2025 Paul Wolneykien <manowar@altlinux.org> 0.0-alt1.git.11d2944
- Initial build for Sisyphus.
