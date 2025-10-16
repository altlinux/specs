Name: kexec-tools
Version: 2.0.32
Release: alt1

Summary: Load one kernel from another
License: GPLv2
Group: System/Kernel and hardware
Provides: /sbin/kexec

Source: %name-%version.tar

BuildRequires: libzstd-devel zlib-devel

%description
/sbin/kexec is a user space utiltity for loading another kernel
and asking the currently running kernel to do something with it.
A currently running kernel may be asked to start the loaded
kernel on reboot, or to start the loaded kernel after it panics.

The panic case is useful for having an intact kernel for writing
crash dumps.  But other uses may be imagined.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
rm -vf %buildroot%_libdir/kexec-tools/kexec_test

%files
%doc AUTHORS COPYING
%_sbindir/kexec
%_sbindir/vmcore-dmesg
%_man8dir/kexec.8*
%_man8dir/vmcore-dmesg.8*

%changelog
* Thu Oct 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.32-alt1
- 2.0.32 released

* Tue Apr 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.31-alt1
- 2.0.31 released

* Mon Dec 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.30-alt1
- 2.0.30 released

* Thu Jul 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.29-alt1
- 2.0.29 released

* Mon Jan 15 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.28-alt1
- 2.0.28 released

* Mon Aug 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.27-alt1
- 2.0.27 released

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.26-alt1
- 2.0.26 released

* Mon Aug 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.25-alt1
- 2.0.25 released

* Mon Apr 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.24-alt1
- 2.0.24 released

* Fri Nov 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.23-alt1
- 2.0.23 released

* Fri Jul 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.22-alt1
- 2.0.22 released

* Thu Dec 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.21-alt1
- 2.0.21 released

* Thu Jul 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.20-alt1
- 2.0.20 released

* Mon Mar 04 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.19-alt1
- 2.0.19 released

* Thu Nov 01 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.18-alt1
- 2.0.18 released

* Thu Apr 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.17-alt1
- 2.0.17 released

* Mon Nov 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.16-alt1
- 2.0.16 released

* Fri Jun 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.15-alt1
- 2.0.15 released

* Tue Dec 20 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.14-alt1
- 2.0.14 released

* Fri Apr 15 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.12-alt1
- 2.0.12 released

* Mon Nov 09 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.11-alt1
- 2.0.11 released

* Thu Jul 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt1
- 2.0.10 released

* Thu Feb 12 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.9-alt1
- 2.0.9 released

* Mon Jun 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.7-alt1
- 2.0.7 released

* Thu Mar 06 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- 2.0.6 released

* Wed Feb 05 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.5-alt1
- 2.0.5 released

* Thu Mar 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1
- 2.0.4 released

* Fri Jan 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt0.1
- 2.0.4-rc1

* Thu Apr 26 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Thu Mar 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Sep 14 2009 Michail Yakushin <silicium@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon Apr 21 2008 Michail Yakushin <silicium@altlinux.ru> 2.0-alt1
- intial build for ALT

* Tue Dec 16 2004 Eric Biederman <ebiederman@lnxi.com>
- kexec-tools initialy packaged as an rpm.
