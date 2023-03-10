%define _unpackaged_files_terminate_build 1

Name: kernel-source-rtw89
Version: 0.0
Release: alt3.git.fce040c

Summary: Driver source code for Realtek 8852AE, an 802.11ax device.
License: GPL-2.0
Group: Development/Kernel
Url: https://github.com/lwfinger/rtw89

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
* Fri Mar 10 2023 Anton Farygin <rider@altlinux.ru> 0.0-alt3.git.fce040c
- update to fce040c

* Fri Dec 30 2022 Anton Farygin <rider@altlinux.ru> 0.0-alt2.git.e834edf
- update to e834edf

* Fri Aug 13 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.0-alt1.git.250c6f4
- Initial build for Sisyphus
