Name: kernel-source-netup
Version: 0.0.1
Release: alt1

Summary: NetUP Universal Dual DVB-CI card module for Linux kernel
License: GPLv2
Group: Development/Kernel
URL: http://www.netup.tv/en-EN/netup-universal-dual-dvb-ci
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
Drivers for Universal card with two DVB-C, DVB-C2, DVB-T, DVB-T2,
DVB-S, DVB-S2 inputs and two Common Interface slots.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
mv %name-%version netup-%version
tar -cjf %kernel_srcdir/netup-%version.tar.bz2 netup-%version

%files
%attr(0644,root,root) %kernel_src/netup-%version.tar.bz2

%changelog
* Sat Mar 21 2015 Alexei Takaseev <taf@altlinux.org> 0.0.1-alt1
- Initial buld for ALT Linux

