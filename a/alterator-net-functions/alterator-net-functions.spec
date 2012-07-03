%define _altdata_dir %_datadir/alterator

Name: alterator-net-functions
Version: 1.1
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Requires: libshell >= 0.1.0-alt2 etcnet alterator-hw-functions

Provides: alterator-net-common = %version
Obsoletes: alterator-net-common

BuildArch: noarch

# for test
BuildRequires: alterator-hw-functions

Source: %name-%version.tar

Summary: helpers for etcnet administration
License: GPL
Group: System/Base
Requires: openssl

%description
helpers for etcnet administration

%prep
%setup -q

%build
%make check

%install
%makeinstall

%files
%_bindir/*
%_libexecdir/%name/

%changelog
* Thu Sep 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- add multiple interface addresses support

* Thu Sep 03 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- add ipv4addr_prefix_to_mask() (maskname replacement)
- remove obsolete functions:
   * faceinfo
   * ifcheckdhcp
   * ifcheckplug
   * ifcheckup
   * ifcheckwireless
   * ifdriver
   * iflist
   * ifread
   * iftabupdate

* Wed Sep 02 2009 Mikhail Efremov <sem@altlinux.org> 1.0-alt2
- fix ipv4addr_is_in_subnet().

* Wed Sep 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- add a new set of excellent functions for various ipv4address calculations (sem@)

* Thu Apr 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt4
- list_iface: skip ifaces with type=801 (wmaster0) (closes: #19866)

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- replace function chomp with shell_var_trim from modern libshell
- add read_iface_default_gw/write_iface_default_gw

* Fri Apr 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt2
- add comments in obsolete scripts

* Thu Apr 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt1
- list_iface: skip ifaces connected to a bridges

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt3
- improve iface_up and iface_down functions

* Fri Apr 10 2009 Mikhail Efremov <sem@altlinux.org> 0.8-alt2
- improve next_iface function
- improve read_iface_addr function (by inger@)

* Fri Apr 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- rename package to alterator-net-functions
- use alterator-hw-functions instead of old if* helpers
- if* helper functions are deprecated now

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- add functions to edit local resolv.conf

* Tue Mar 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add script to generate reverse dns zones

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- fix typo (by inger@)

* Mon Dec 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- add unit tests

* Mon Dec 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- resurrect read_iface_option behavior

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- s,ash,sh,

* Tue Oct 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- improve netname, add: netcheck, list_static_iface, read_iface_addr, write_iface_addr

* Thu Aug 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add functions: netname, list_iface, list_network

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add alterator-net-functions library

* Tue Jan 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- hal workaround: ignore device duplicates

* Mon Jan 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- add ifread utility

* Fri Jan 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- ifaceinfo: add support for pcmcia network cards

* Wed Nov 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- use hal

* Tue Oct 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add iftabupdate utility

* Thu Oct 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- simplify ifcheckup utility
- add maskname and ifaceinfo utilities

* Thu Jul 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
