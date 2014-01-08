%define mname exfat
Name: kernel-src-%mname
Version: 1.2.7
Release: alt1
Summary: Linux read/write kernel driver for the exFAT file system
Group: Development/Kernel
BuildArch: noarch
License: GPLv2
URL: https://github.com/rxrz/exfat-nofuse
Source: %mname-%version.tar
Patch: %mname-%version-%release.patch
Provides: kernel-source-%mname = %version-%release

BuildRequires: rpm-build-kernel

%description
Linux read/write kernel driver for the exFAT file system.
This package contains sources for the exFAT Linux kernel modules.


%prep
%setup -q -n %mname-%version
%patch -p1


%install
install -d -m 0755 %buildroot%kernel_src
tar -C .. -cJf %buildroot%kernel_src/%mname-%version.tar.xz %mname-%version


%files
%_usrsrc/kernel


%changelog
* Wed Jan 08 2014 Led <led@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Thu Nov 14 2013 Led <led@altlinux.ru> 1.2.6-alt2
- upstream fixes

* Tue Oct 08 2013 Led <led@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Sat Aug 17 2013 Led <led@altlinux.ru> 1.1.5-alt2
- upstream updates and fixes

* Sun Aug 11 2013 Led <led@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sun Jul 28 2013 Led <led@altlinux.ru> 1.1.3-alt3
- added module alias

* Sat Jul 13 2013 Led <led@altlinux.ru> 1.1.3-alt2
- add kernel 3.10 compatibility

* Sun Jun 30 2013 Led <led@altlinux.ru> 1.1.3-alt1
- 1.1.3
