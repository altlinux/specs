Name: kernel-source-qla2x00t
Version: 3.1.0
Release: alt1
Summary: FC QLogic Target Driver modules sources for Linux kernel
License: GPLv2
Group: Development/Kernel
URL: http://scst.sf.net
Source0: qla2x00t-%version.tar.bz2

BuildRequires: rpm-build-kernel
BuildArch: noarch

%description
This package contains FC QLogic Target Driver for 22xx/23xx/24xx/25xx/26xx Adapters modules sources for Linux kernel

%install
install -pD -m0644 %SOURCE0 %kernel_srcdir/qla2x00t-%version.tar.bz2

%files
%_usrsrc/kernel

%changelog
* Sun Oct 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release

