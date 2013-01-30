Name: kernel-source-r8168
Version: 8.035.00
Release: alt2

Summary: Source for RTL8168 driver
License: GPLv2+
Group: Development/Kernel

URL: http://www.realtek.com/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: r8168-%version.tar.bz2
Source1: blacklist-r8168.conf

BuildArch: noarch

BuildPreReq: kernel-build-tools

Provides: kernel-source-rtl8168
Obsoletes: kernel-source-rtl8168

%description
RTL8168 is the Linux device driver released for RealTek RTL8168B/8111B,
RTL8168C/8111C, RTL8168CP/8111CP, RTL8168D/8111D, and RTL8168DP/8111DP
Gigabit Ethernet controllers with PCI-Express interface.

%package -n r8168-blacklist
Summary: Blacklist modules for r8168
Group: System/Kernel and hardware

%description -n r8168-blacklist
Blacklist modules for correctly working module r8168

%prep
%setup -c
mv r8168-%version %name-%version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/modprobe.d/blacklist-r8168.conf

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n r8168-blacklist
%config %_sysconfdir/modprobe.d/blacklist-r8168.conf

%changelog
* Wed Jan 30 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt2
- Add subpackage for correctly working

* Tue Jan 29 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt1
- Version 8.035.00

* Fri Dec 02 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt1
- Version 8.027.00

* Sat Oct 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.026.00-alt1
- Version 8.026.00

* Fri Aug 26 2011 Nazarov Denis <nenderus@altlinux.org> 8.025.00-alt1
- Version 8.025.00

* Mon May 30 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt0.M60T.1
- Build for branch t6

* Sun May 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt1
- Version 8.024.00

* Sat Apr 23 2011 Nazarov Denis <nenderus@altlinux.org> 8.023.00-alt1
- Version 8.023.00

* Sun Mar 27 2011 Nazarov Denis <nenderus@altlinux.org> 8.022.00-alt1
- Version 8.022.00

* Mon Jan 31 2011 Nazarov Denis <nenderus@altlinux.org> 8.021.00-alt1
- Version 8.021.00

* Mon Jan 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.020.00-alt1
- Initial build for ALT Linux



