%set_verify_elf_method unresolved=relaxed

Name: openipmi
Summary: %name - Library interface to IPMI
Version: 2.0.36
Release: alt2
License: LGPL-2.1-or-later and GPL-2.0-or-later or BSD-3-Clause
VCS: https://git.code.sf.net/p/openipmi/code
Url: https://openipmi.sourceforge.io/
Group: System/Configuration/Hardware
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: libpopt-devel python3-devel libnet-snmp-devel rpm-build-python3
BuildRequires: libncurses-devel libssl-devel tkinter swig perl-devel
BuildRequires: glib2-devel tcl-devel libedit-devel libreadline-devel

%description
This package contains basic tools used with OpenIPMI.

%package -n lib%name
Summary: %name - Library interface to IPMI
Group: System/Configuration/Hardware

%description -n lib%name
This package contains a shared library implementation of IPMI.

%package -n lib%name-devel
Summary: Development files for OpenIPMI
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Contains additional files need for a developer to create applications
and/or middleware that depends on libOpenIPMI

%package perl
Summary: Perl interface for OpenIPMI
Group: System/Configuration/Hardware
Requires: lib%name = %version-%release

%description perl
A Perl interface for OpenIPMI.

%package -n python3-module-%name
Summary: Python interface for OpenIPMI
Group: System/Configuration/Hardware
Requires: lib%name = %version-%release

%description -n python3-module-%name
A Python interface for OpenIPMI.

%package gui
Summary: GUI (in python) for OpenIPMI
Group: System/Configuration/Hardware
Requires: python3-module-%name = %EVR
Requires: python3-modules-tkinter


%description gui
A GUI interface for OpenIPMI.  Written in python an requiring wxWidgets.

%package ui
Summary: User Interface (ui)
Group: System/Configuration/Hardware
Requires: lib%name = %version-%release

%description ui
This package contains a user interface

%package lanserv
Summary: Emulates an IPMI network listener
Group: System/Configuration/Hardware

%description lanserv
This package contains a network IPMI listener.

%prep
%setup
%patch0 -p1

%build
%autoreconf
export CFLAGS="-fPIC $RPM_OPT_FLAGS"
%configure --disable-static \
	   --with-tcl=yes \
	   --with-tk=yes \
	   --with-tkinter=yes \
	   --with-tclcflags='-I/usr/include' \
	   --with-pythoninstall=%python3_sitelibdir \
	   --with-python=%__python3
%make

%install
make DESTDIR=%buildroot install
install -d %buildroot%_initdir
install -d %buildroot%_sysconfdir/sysconfig
install ipmi.init %buildroot%_initdir/ipmi
install ipmi.sysconf %buildroot%_sysconfdir/sysconfig/ipmi

rm -f %buildroot%_libdir/libOpenIPMIglib12.*

%files
%doc COPYING COPYING.LIB FAQ INSTALL README README.Force
%doc README.MotorolaMXP CONFIGURING_FOR_LAN COPYING.BSD
%_initdir/ipmi
%_sysconfdir/sysconfig/ipmi

%files -n lib%name
%_libdir/libOpenIPMIcmdlang.so.*
%_libdir/libOpenIPMIglib.so.*
%_libdir/libOpenIPMItcl.so.*
%_libdir/libOpenIPMIposix.so.*
%_libdir/libOpenIPMIpthread.so.*
%_libdir/libOpenIPMI.so.*
%_libdir/libOpenIPMIutils.so.*
%_libdir/libOpenIPMIui.so.*

%files perl
%perl_vendor_archlib/OpenIPMI*
%perl_vendor_autolib/OpenIPMI
%doc swig/OpenIPMI.i swig/perl/sample swig/perl/ipmi_powerctl

%files -n python3-module-%name
%python3_sitelibdir/*OpenIPMI.*
%python3_sitelibdir/__pycache__/*OpenIPMI.*
%doc swig/OpenIPMI.i

%files gui
%dir %python3_sitelibdir/openipmigui
%python3_sitelibdir/openipmigui/*
%_bindir/openipmigui

%files -n lib%name-devel
%_includedir/OpenIPMI
%_libdir/*.so
%_libdir/pkgconfig/*

%files ui
%_bindir/ipmi_ui
%_bindir/ipmicmd
%_bindir/openipmicmd
%_bindir/ipmish
%_bindir/openipmish
%_bindir/openipmi_eventd
%_bindir/solterm
%_bindir/rmcp_ping
%_man1dir/ipmi_ui.1*
%_man1dir/openipmi_eventd.1*
%_man1dir/openipmicmd.1*
%_man1dir/openipmish.1*
%_man1dir/openipmigui.1*
%_man1dir/solterm.1*
%_man1dir/rmcp_ping.1*
%_man7dir/ipmi_cmdlang.7*
%_man7dir/openipmi_conparms.7*

%files lanserv
%config(noreplace) %_sysconfdir/ipmi/ipmisim1.emu
%config(noreplace) %_sysconfdir/ipmi/lan.conf
%_bindir/ipmilan
%_bindir/ipmi_sim
%_bindir/sdrcomp
%_libdir/libIPMIlanserv.so.*
%_man8dir/ipmilan.8*
%_man1dir/ipmi_sim.1*
%_man5dir/ipmi_lan.5*
%_man5dir/ipmi_sim_cmd.5*



%changelog
* Mon Aug 05 2024 Anton Farygin <rider@altlinux.ru> 2.0.36-alt2
- gui: added python3-modules-tkinter dependency (closes: #35022)
- SPEC: added VCS and fixed URL tags
- SPEC: fixed License according SPDX

* Sat Aug 03 2024 Anton Farygin <rider@altlinux.ru> 2.0.36-alt1
- 2.0.35 -> 2.0.36

* Sun Jul 21 2024 Anton Farygin <rider@altlinux.ru> 2.0.35-alt1
- 2.0.33 -> 2.0.35

* Fri Nov 17 2023 Igor Vlasenko <viy@altlinux.org> 2.0.33-alt2
- NMU: link perl module with -lperl

* Wed Feb 01 2023 Anton Farygin <rider@altlinux.ru> 2.0.33-alt1
- 2.0.33

* Tue Jan 25 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.32-alt2
- NMU: fixed build with python3.10.

* Fri Dec 17 2021 Anton Farygin <rider@altlinux.ru> 2.0.32-alt1
- 2.0.32

* Wed Mar 03 2021 Anton Farygin <rider@altlinux.org> 2.0.31-alt1
- 2.0.31

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 2.0.29-alt1
- 2.0.29

* Tue Jan 14 2020 Anton Farygin <rider@altlinux.ru> 2.0.28-alt1
- 2.0.28

* Wed Oct 02 2019 Anton Farygin <rider@altlinux.ru> 2.0.27-alt1
- 2.0.27
- build with python3

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.25-alt3
- NMU: remove rpm-build-ubt from BR:

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 2.0.25-alt2
- rebuilt with libopenssl1.1

* Tue May 08 2018 Anton Farygin <rider@altlinux.ru> 2.0.25-alt1
- 2.0.25

* Tue Sep 19 2017 Anton Farygin <rider@altlinux.ru> 2.0.24-alt1
- new version

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.0.23-alt1
- new version

* Tue May 02 2017 Anton Farygin <rider@altlinux.ru> 2.0.22-alt1
- new version

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.0.21-alt1.1.1.1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.21-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.21-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.21-alt1.1
- rebuild with new perl 5.20.1

* Tue May 20 2014 Anton Farygin <rider@altlinux.ru> 2.0.21-alt1
- new version

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0.19-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.0.19-alt2
- rebuilt for perl-5.16

* Sat Dec 31 2011 Michael Shigorin <mike@altlinux.org> 2.0.19-alt1
- new version

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.18-alt1.2.1
- Rebuild with Python-2.7

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 2.0.18-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.18-alt1.1
- rebuilt with perl 5.12
- fixed build

* Mon Jun 28 2010 Anton Farygin <rider@altlinux.ru> 2.0.18-alt1
- new version

* Wed Mar 03 2010 Anton Farygin <rider@altlinux.ru> 2.0.16-alt3
- use lib%name requires in lib%name-devel package
- libOpenIPMIui.so.* moved to lib%name package

* Wed Feb 17 2010 Anton Farygin <rider@altlinux.ru> 2.0.16-alt2
- fixed build on x86_64

* Tue Jan 12 2010 Anton Farygin <rider@altlinux.ru> 2.0.16-alt1
- new version

* Wed Jul 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.11-alt1
- Initial build for ALT.

