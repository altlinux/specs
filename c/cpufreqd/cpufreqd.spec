%def_disable static
%def_enable acpi
%def_enable nforce2
%def_enable apm
%def_enable sensors
%def_enable pmu
%def_enable exec
%def_enable tau


Summary: CPU frequency scaling daemon
Name: cpufreqd
Version: 2.4.3
Release: alt2
Url: http://sourceforge.net/projects/cpufreqd/
License: GPLv2
Group: System/Kernel and hardware
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.init.alt
Source2: %name.service
Patch0: %name-%version-%release.patch

BuildRequires: gcc-c++ libcpufreq-devel libsysfs-devel
%{?_enable_sensors:BuildRequires: libsensors3-devel}
Requires: cpufrequtils

%description
Cpufreqd is meant to be a replacement of the speedstep applet you
can find on some other OS, it monitors battery level, AC state and
running programs and adjusts the frequency of the processor according to
a set of rules specified in the config file (see cpufreqd.conf (5)).

Cpufreqd 2 aims to become the next generation power management
daemon. It provides a common interface to enable system monitoring
and to take useful actions upon that.
Currently it is still centered on the CPUFreq kernel interface,
that means that running a CPUFreq capable kernel is still needed but
also that behaviour could be delegated to a plugin.

Note that the configuration file format is slightly incompatible
with the previous cpufreqd 1 but it's really easy to migrate (a
simple Perl script could do it, I'll try to prepare one soon).

%prep
%setup -q
%patch0 -p1

%build
%__aclocal
%__libtoolize -c -f
%__aclocal
%__autoconf
%__automake -a -c --foreign

%configure \
	%{subst_enable static} \
	%{subst_enable acpi} \
	%{subst_enable nforce2} \
	%{subst_enable apm} \
	%{subst_enable sensors} \
	%{subst_enable pmu} \
	%{subst_enable exec} \
	--enable-governor-parameters \
	%{subst_enable tau} \
	--libdir=%_libdir/%name
# libdir need only for plugins

%make_build

%install
%make DESTDIR=%buildroot install

install -d %buildroot{%_initdir,%systemd_unitdir}
install %SOURCE1 %buildroot%_initdir/%name
install %SOURCE2 %buildroot%systemd_unitdir/%name.service

# remove non-packaged files 
rm -f %buildroot%_libdir/%name/*.la

%post
%post_service cpufreqd

%preun
%preun_service cpufreqd

%files
%doc AUTHORS COPYING INSTALL README NEWS TODO ChangeLog
%_sbindir/*
%_bindir/*
%dir %_libdir/cpufreqd
%_libdir/cpufreqd/*.so
%attr(644,root,root) %config(noreplace) %_sysconfdir/%name.conf
%_initdir/%name
%systemd_unitdir/%name.service
%_mandir/man?/*

%changelog
* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt2
- fix for kernel >= 2.6.36
- add systemd service

* Mon Feb 21 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Wed Apr 21 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Tue Apr 13 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.4-alt2.git.e4bbd.1
- patch from bugzilla aplied (closes: #22923)

* Thu Feb 04 2010 Alexey Shabalin <shaba@altlinux.ru> 2.3.4-alt2.git.e4bbd
- git snapshot e4bbd57e6f201f90a91550b381e347f7a1b6fcd5

* Tue May 05 2009 Alexey Shabalin <shaba@altlinux.ru> 2.3.4-alt1
- 2.3.4
- build from git

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3
- fix work with two batteries(patch3)

* Mon Aug 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- move plugins from %_libdir to %_libdir/%name

* Tue Apr 24 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1
- clean spec
- add more programs to rule in cpufreqd.conf (patch1)
- fix restore maximum cpu (patch2)

* Tue Jan 10 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0 of the next generation verion
- remove two config files (only one for kernel-2.6)

* Mon Jun 27 2005 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt2
- fix init script (#7007)

* Tue May 24 2005 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- update 1.2.3 

* Mon Apr 25 2005 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- update cpufreqd-1.1.2 
- add two config files cpufregd.conf-2.4 and cpufreqd.conf-2.6
- autoselect config file for 2.4 or 2.6 kernel

* Sun Oct 03 2004 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 

* Mon Mar 15 2004 Alexey Shabalin <shaba@altlinux.ru> 1.1.2-alt1
- update cpufreqd-1.1.2 
- remove /etc/sysconfig/cpufreqd
- update init scripts 

* Wed Jan 07 2004 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- initial release

