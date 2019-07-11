Name: kernel-source-rtl8192eu
Version: 5.2.19.1
Release: alt1

Summary: Realtek rtl8192eu official Linux driver
License: MIT
Group: Development/Kernel
URL: https://github.com/clnhub/rtl8192eu-linux
Packager: Dmitry Terekhin <jqt4@altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This driver is based on the (latest) official Realtek v5.2.19.1 driver
with fixes and improvements to support the latest kernels (up to 5.1).

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Jul 10 2019 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt1
- Initial build
