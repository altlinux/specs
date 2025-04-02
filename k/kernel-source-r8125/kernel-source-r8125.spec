Name: kernel-source-r8125
Version: 9.015.00
Release: alt1
Summary: Source for the r8125 driver
License: GPL
Group: Development/Kernel
URL: https://www.realtek.com/Download/List?cate_id=584
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: r8125-%version.tar

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
2.5G Ethernet LINUX driver r8125

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 r8125-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Apr 01 2025 Paul Wolneykien <manowar@altlinux.org> 9.015.00-alt1
- Updated up to v9.015.00.

* Fri Jul 14 2023 Valery Inozemtsev <shrek@altlinux.ru> 9.011.01-alt1
- 9.011.01

* Mon Oct 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.003.05-alt1
- initial release

