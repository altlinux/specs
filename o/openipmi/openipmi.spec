%set_verify_elf_method unresolved=relaxed

Name: openipmi
Summary: %name - Library interface to IPMI
Version: 2.0.19
Release: alt1
License: LGPL
Url: http://openipmi.sourceforge.net
Group: System/Configuration/Hardware
Source: %name-%version-%release.tar
Patch: %name-%version-%release.patch

BuildRequires: libpopt-devel python-devel libnet-snmp-devel
BuildRequires: libncurses-devel libssl-devel tkinter swig
BuildRequires: glib2-devel tcl-devel

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

%package -n python-module-%name
Summary: Python interface for OpenIPMI
Group: System/Configuration/Hardware
Requires: lib%name = %version-%release

%description -n python-module-%name
A Python interface for OpenIPMI.

%package gui
Summary: GUI (in python) for OpenIPMI
Group: System/Configuration/Hardware
Requires: python-module-%name = %version-%release

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
%configure --disable-static
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

%files -n python-module-%name
%_libdir/python*/site-packages/*OpenIPMI.*
%doc swig/OpenIPMI.i

%files gui
%dir %_libdir/python*/site-packages/openipmigui
%_libdir/python*/site-packages/openipmigui/*
%_bindir/openipmigui

%files -n lib%name-devel
%_includedir/OpenIPMI
%_libdir/*.so
%_libdir/pkgconfig/*
%doc doc/IPMI.pdf

%files ui
%_bindir/ipmi_ui
%_bindir/ipmicmd
%_bindir/openipmicmd
%_bindir/ipmish
%_bindir/openipmish
%_bindir/solterm
%_bindir/rmcp_ping
%_man1dir/ipmi_ui.1*
%_man1dir/openipmicmd.1*
%_man1dir/openipmish.1*
%_man1dir/openipmigui.1*
%_man1dir/solterm.1*
%_man1dir/rmcp_ping.1*
%_man7dir/ipmi_cmdlang.7*
%_man7dir/openipmi_conparms.7*

%files lanserv
%_bindir/ipmilan
%_libdir/libIPMIlanserv.so.*
%_man8dir/ipmilan.8*

%changelog
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

