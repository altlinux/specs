#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: dahdi-tools
Summary: DAHDI tools for Digium hardware and Asterisk
Version: 2.10.2
Release: alt2
License: GPL
Group: System/Kernel and hardware
BuildRequires: dahdi-linux-headers gcc-c++ libncurses-devel libnewt-devel libpcap-devel libusb-compat-devel module-init-tools perl-Pod-Parser ppp-devel wget
%define astattr %attr(4510,_asterisk,pbxadmin)
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires: firmware-dahdi
Obsoletes: zaptel
Obsoletes: zaptel-test
Requires(pre): asterisk-user
Url: http://downloads.asterisk.org/pub/telephony/dahdi-tools/
Requires: libtonezone2 = %version-%release
Requires: perl-Dahdi = %version-%release
Patch1: dahdi.perl.patch
Patch2: dahdi.perl.fix.patch
Patch3: dahdi.build.patch
Patch4: %name-%version-%release.patch
Source: dahdi-tools.tar
Source2: %name.watch

%package -n dahdi
Summary: DAHDI support virtual package
Group: System/Kernel and hardware
Requires(pre): asterisk-user
Requires: dahdi-udev
Requires: dahdi-xpp = %version-%release
Requires: dahdi-tools = %version-%release
Requires: dahdi_diag = %version-%release
Requires: dahdi_tool = %version-%release
Requires: perl-Dahdi = %version-%release
Requires: gendahdiconf = %version-%release

%description -n dahdi
DAHDI support virtual package

%package -n dahdi-full
Summary: Virtual package that requires all DAHDI-related packages
Group: System/Kernel and hardware
Obsoletes: zaptel-full
Requires: dahdi = %version-%release
Requires: dahdi_diag = %version-%release
Requires: dahdi_tool = %version-%release
Requires: dahdi-tools = %version-%release
Requires: gendahdiconf = %version-%release
Requires: perl-Dahdi = %version-%release
Requires: ppp-dahdi = %version-%release
Requires: dahdi-xpp = %version-%release
Requires: dahdi-udev

%description -n dahdi-full
Virtual package that requires all DAHDI-related packages

%package -n dahdi-xpp
Summary: utilites for xorcom hardware
Group: System/Kernel and hardware
Requires: dahdi = %version-%release
Requires: perl-Dahdi = %version-%release

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
Requires: perl-Dahdi = %version-%release

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
%patch4 -p1
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%add_optflags -Wno-error=unused-const-variable
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
mkdir -p %buildroot%_udevrulesdir/
mv %buildroot%_sysconfdir/udev/rules.d/* %buildroot%_udevrulesdir/

%preun -n dahdi
%preun_service dahdi

%post -n dahdi
%post_service dahdi

%files
%dir %attr(0770,_asterisk,pbxadmin) %_sysconfdir/dahdi
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/system.conf
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/assigned-spans.conf.sample
%attr(0664,root,pbxadmin) %config(noreplace) %_sysconfdir/dahdi/span-types.conf.sample
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
%astattr %_sbindir/dahdi_span_assignments
%_man8dir/dahdi_span_assignments.8.*
%astattr %_sbindir/dahdi_span_types
%_man8dir/dahdi_span_types.8.*
%astattr %_sbindir/dahdi_waitfor_span_assignments
%_man8dir/dahdi_waitfor_span_assignments.8.*
%dir %_datadir/dahdi
%dir %_datadir/dahdi/span_config.d
%dir %_datadir/dahdi/handle_device.d
%_datadir/dahdi/dahdi_auto_assign_compat
%_datadir/dahdi/dahdi_handle_device
%_datadir/dahdi/dahdi_span_config
%_datadir/dahdi/handle_device.d/10-span-types
%_datadir/dahdi/handle_device.d/20-span-assignments
%_datadir/dahdi/span_config.d/10-dahdi-cfg
%_datadir/dahdi/span_config.d/20-fxotune
%_datadir/dahdi/span_config.d/50-asterisk

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
%_man8dir/astribank_allow.8.*
%_sbindir/astribank_hexload
%_man8dir/astribank_hexload.8.*
%_sbindir/astribank_tool
%_man8dir/astribank_tool.8.*
%_sbindir/astribank_is_starting
%_man8dir/astribank_is_starting.8.*
%_sbindir/twinstar
%_man8dir/twinstar.8.*
%_udevrulesdir/xpp.rules

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
* Tue Feb 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.2-alt2
- Fixed build with new toolchain.

* Wed Aug 26 2015 Denis Smirnov <mithraen@altlinux.ru> 2.10.2-alt1
- new version 2.10.2

* Thu Feb 19 2015 Denis Smirnov <mithraen@altlinux.ru> 2.10.1-alt1
- new version 2.10.1

* Wed Sep 24 2014 Denis Smirnov <mithraen@altlinux.ru> 2.10.0.1-alt1
- new version 2.10.0.1

* Sun Aug 17 2014 Denis Smirnov <mithraen@altlinux.ru> 2.10.0-alt2
- repocop fix for udev-files-in-etc

* Fri Aug 15 2014 Denis Smirnov <mithraen@altlinux.ru> 2.10.0-alt1
- new version 2.10.0

* Fri Aug 15 2014 Denis Smirnov <mithraen@altlinux.ru> 2.9.2-alt1
- new version 2.9.2

* Sun Jun 30 2013 Denis Smirnov <mithraen@altlinux.ru> 2.7.0-alt1
- new version 2.7.0

* Tue May 14 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.2-alt3
- add condstop target to initscript

* Sat Apr 20 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.2-alt2
- add condrestart target to initscript

* Fri Apr 19 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.2-alt1
- new version 2.6.2

* Sat Feb 02 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.1-alt3
- remove unused config with options for wct4xxp

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 2.6.1-alt2
- fix requires (add version in subpackage requires)

* Thu Oct 18 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fix build

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

