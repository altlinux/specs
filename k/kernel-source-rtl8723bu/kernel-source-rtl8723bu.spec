%define module_name rtl8723bu
%define git_rev 2cd9874

Name: kernel-source-%module_name
Version: 4.3.6.11
Release: alt4.git%git_rev

Summary: Driver for Realtek RTL8723BU Wireless Adapter with Hardware ID 0bda:b720
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/lwfinger/rtl8723bu

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
* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 4.3.6.11-alt4.git2cd9874
- Fixed build for kernel 5.17.

* Wed Nov 17 2021 Andrey Cherepanov <cas@altlinux.org> 4.3.6.11-alt3.gitd34603a
- Upstream fix for kernel 5.15.

* Fri Dec 18 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.6.11-alt2.git9ce1c38
- Fix builds with kernel 5.10.

* Sat Oct 31 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.6.11-alt1.gitce4490b
- Initial build for Sisyphus.
