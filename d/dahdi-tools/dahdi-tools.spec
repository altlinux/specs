Name: dahdi-tools
Summary: DAHDI tools for Digium hardware and Asterisk
Version: 2.6.0
Release: alt1
License: GPL
Group: System/Kernel and hardware
BuildRequires: dahdi-linux-headers gcc-c++ libncurses-devel libnewt-devel libpcap-devel libusb-compat-devel module-init-tools perl-Pod-Parser ppp-devel rpm-build-ruby wget
%define astattr %attr(4510,_asterisk,pbxadmin)
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires: firmware-dahdi
Obsoletes: zaptel
Obsoletes: zaptel-test
Requires(pre): asterisk-user
Url: http://downloads.asterisk.org/pub/telephony/dahdi-tools/
Patch1: dahdi.perl.patch
Patch2: dahdi.perl.fix.patch
Patch3: dahdi.build.patch
Source: dahdi-tools.tar

%package -n dahdi
Summary: DAHDI support virtual package
Group: System/Kernel and hardware
Requires(pre): asterisk-user
Requires: dahdi-udev
Requires: dahdi-tools
Requires: dahdi_diag
Requires: dahdi_tool
Requires: perl-Dahdi
Requires: gendahdiconf

%description -n dahdi
DAHDI support virtual package

%package -n dahdi-full
Summary: Virtual package that requires all DAHDI-related packages
Group: System/Kernel and hardware
Obsoletes: zaptel-full
Requires: dahdi
Requires: dahdi_diag
Requires: dahdi-full
Requires: dahdi_tool
Requires: dahdi-tools
Requires: gendahdiconf
Requires: perl-Dahdi
Requires: ppp-dahdi
Requires: dahdi-udev
Requires: dahdi-xpp

%description -n dahdi-full
Virtual package that requires all DAHDI-related packages

%package -n dahdi-xpp
Summary: utilites for xorcom hardware
Group: System/Kernel and hardware

%description -n dahdi-xpp
utilites for xorcom hardware

%package -n dahdi_diag
Summary: DAHDI diagnostic utility
Group: System/Kernel and hardware

%description -n dahdi_diag
DAHDI diagnostic utility

%package -n dahdi_tool
Summary: DAHDI tool shows status of Digium's interface cards
Group: System/Kernel and hardware
Obsoletes: zaptel-zttool

%description -n dahdi_tool
DAHDI tool shows status of Digium's interface cards

%package -n gendahdiconf
Summary: DAHDI autoconfiguration
Group: System/Kernel and hardware
Obsoletes: genzaptelconf
Requires(pre): asterisk-user

%description -n gendahdiconf
DAHDI autoconfiguration

%package -n libtonezone-dahdi-devel
Summary: DAHDI tonezone library for Asterisk
Group: System/Kernel and hardware
Conflicts: libtonezone-devel
Requires: libtonezone2 = %version-%release

%description -n libtonezone-dahdi-devel
DAHDI tonezone library for Asterisk

%package -n libtonezone-dahdi-devel-static
Summary: DAHDI tonezone library for Asterisk
Group: System/Kernel and hardware
Requires: libtonezone-dahdi-devel = %version-%release
Conflicts: libtonezone-static

%description -n libtonezone-dahdi-devel-static
DAHDI tonezone library for Asterisk

%package -n libtonezone2
Summary: Zaptel tonezone library for Asterisk
Group: System/Kernel and hardware
Obsoletes: libtonezone-dahdi

%description -n libtonezone2
Zaptel tonezone library for Asterisk

%package -n perl-Dahdi
Summary: Perl modules for DAHDI
Group: Development/Perl
BuildArch: noarch

%description -n perl-Dahdi
Perl modules for DAHDI


%package -n ppp-dahdi
Summary: DAHDI support for PPP
Group: System/Servers
Conflicts: ppp-zaptel

%description -n ppp-dahdi
DAHDI support for PPP

%description
Dahdi tools only


%prep
%setup -c
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build
%make_build -C ppp
%make_build dahdi_pcap

%install
%makeinstall_std
make -C ppp install DESTDIR=%buildroot
install -m755 -D dahdi.init %buildroot%_initdir//dahdi
install -m664 -D init.conf.sample %buildroot%_sysconfdir/dahdi/init.conf
install -m644 -D xpp/genconf_parameters %buildroot%_sysconfdir/dahdi/genconf_parameters
install -m755 dahdi_pcap %buildroot%_sbindir/dahdi_pcap
mkdir -p %buildroot%_initdir/modprobe.d
echo 'options wct4xxp t1e1override=0xff' >  %buildroot%_initdir/modprobe.d/dahdi

%preun -n dahdi
%preun_service dahdi

%post -n dahdi
%post_service dahdi

%files
%config(noreplace) %_initdir/modprobe.d/dahdi
%dir %attr(0770,_asterisk,pbxadmin) %_sysconfdir/dahdi
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/system.conf
%astattr %_sbindir/fxotune
%_man8dir/fxotune.8.*
%astattr %_sbindir/dahdi_cfg
%_man8dir/dahdi_cfg.8.*
%astattr %_sbindir/dahdi_monitor
%_man8dir/dahdi_monitor.8.*
%_sbindir/dahdi_registration
%_man8dir/dahdi_registration.8.*
%astattr %_sbindir/dahdi_scan
%_man8dir/dahdi_scan.8.*
%astattr %_sbindir/dahdi_speed
%astattr %_sbindir/dahdi_test
%_man8dir/dahdi_test.8.*
%astattr %_sbindir/sethdlc
%astattr %_sbindir/dahdi_pcap
%astattr %_sbindir/fxstest
%_man8dir/fxstest.8.*

%files -n dahdi
%dir %attr(0770,_asterisk,pbxadmin) %_sysconfdir/dahdi
%_initdir/dahdi
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/init.conf
%doc init.conf.sample

%files -n dahdi-full

%files -n dahdi-xpp
%_sysconfdir/hotplug/usb/xpp_fxloader
%_sysconfdir/hotplug/usb/xpp_fxloader.usermap
%_datadir/dahdi/xpp_fxloader
%_datadir/dahdi/astribank_hook
%_datadir/dahdi/waitfor_xpds
%_sbindir/xpp_blink
%_man8dir/xpp_blink.8.*
%_sbindir/xpp_sync
%_man8dir/xpp_sync.8.*
%_sbindir/astribank_allow
%_man8dir/astribank_allow.8.gz
%_sbindir/astribank_hexload
%_man8dir/astribank_hexload.8.gz
%_sbindir/astribank_tool
%_man8dir/astribank_tool.8.gz
%_sbindir/fpga_load
%_man8dir/fpga_load.8.gz
%_sbindir/astribank_is_starting
%_man8dir/astribank_is_starting.8.gz
%_sbindir/twinstar
%_man8dir/twinstar.8.gz

%files -n dahdi_diag
%astattr %_sbindir/dahdi_diag
%_man8dir/dahdi_diag.8.*

%files -n dahdi_tool
%astattr %_sbindir/dahdi_tool
%astattr %_sbindir/dahdi_maint
%_man8dir/dahdi_tool.8.*
%_man8dir/dahdi_maint.8.*

%files -n gendahdiconf
%_sbindir/dahdi_genconf
%_man8dir/dahdi_genconf.8.*
%_sbindir/dahdi_hardware
%_man8dir/dahdi_hardware.8.*
%_sbindir/lsdahdi
%_man8dir/lsdahdi.8.*
%dir %attr(0770,_asterisk,pbxadmin) %_sysconfdir/dahdi
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/genconf_parameters
%doc xpp/genconf_parameters

%files -n libtonezone-dahdi-devel
%_libdir/libtonezone.so
%dir %_includedir/dahdi
%_includedir/dahdi/tonezone.h

%files -n libtonezone-dahdi-devel-static
%_libdir/libtonezone.a

%files -n libtonezone2
%_libdir/libtonezone.so.2
%_libdir/libtonezone.so.2.0
%exclude %_libdir/libtonezone.so.1
%exclude %_libdir/libtonezone.so.1.0

%files -n perl-Dahdi
%perl_vendor_privlib/D*

%files -n ppp-dahdi
%_libdir/pppd/*/*.so

%changelog
* Mon Feb 13 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt1
- 2.6.0
- add dahdi_pcap

* Wed Oct 26 2011 Denis Smirnov <mithraen@altlinux.ru> 2.5.0.2-alt1
- 2.5.0.2

* Sun Apr 03 2011 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt5
- select E1 mode by default for wct4xxp

* Sat Jan 22 2011 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt4
- add requires to firmware

* Tue Nov 30 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Nov 30 2010 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt3
- fix build

* Wed May 12 2010 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt2
- fix dahdi start without OpenVZ (ALT #23452)

* Sun Apr 18 2010 Denis Smirnov <mithraen@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sun Mar 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Thu Jan 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt2
- fix dahdi-xpp

* Thu Jan 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Fri Oct 23 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt18
- not start dahdi service in VE

* Sat Oct 03 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt17
- users in 'pbxadmin' group can use dahdi_tool and some other utils

* Sat Oct 03 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt16
- add requires(pre) to asterisk-user

* Wed Sep 30 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt15
- ppp-dahdi: add conflicts to ppp-zaptel and fix description

* Thu Sep 17 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt14
- Add config samples to %doc

* Wed Sep 16 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt13
- Add some more xpp utilites.
- Add config for gendahdiconf.
- correct initscript install.
- remove libtonezone1 subpackage.

* Mon Sep 14 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt12
- add initscript

* Sat Sep 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt11
- move Xorcom-related utilites to separate package
- some more Obsoletes to zaptel-related packages
- add dahdi-full package

* Sat Sep 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt10
- add Obsoletes: zaptel

* Sat Sep 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt9
- add gendahdiconf subpackage
- add libtonezone1 subpackage

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt8
- add Url tag

* Thu Aug 06 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt7
- remove libtonezone1 subpackage

* Thu Aug 06 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt6
- add obsoletes

* Tue Jul 28 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt5
- split libtonezone-dahdi to libtonezone1/2 subpackages

* Thu Jul 23 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt4
- add requires to dahdi-udev

* Sun Jul 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt3
- next try to fix ppp plugin

* Sun Jul 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt2
- fix ppp plugin

* Sat Jul 11 2009 Denis Smirnov <mithraen@altlinux.ru> 2.2.0-alt1
- first build for Sisyphus

