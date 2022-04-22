Name: kernel-source-rtl8192fu
Version: 5.8.6.2
Release: alt4.gitbfe289f

Summary: RTL8192FU driver for Linux kernel
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/kelebek333/rtl8192fu-dkms
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-kernel

%description
RTL8192FU driver for Linux kernel.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt4.gitbfe289f
- Fixed build for kernel 5.17.

* Wed Nov 17 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt3.git69c7bf8
- Upstream fix for kernel 5.15.

* Mon May 24 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt2.git4ac3c39
- Upstream fix for kernel 5.12.

* Fri Apr 09 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt1
- Initial build for Sisyphus.
