Name: ebtables
Version: 2.0.10
Release: alt1

Summary: A filtering tool for a bridging firewall
License: GPL
Group: System/Kernel and hardware

Url: http://ebtables.sourceforge.net

Source: %name-%version-%release.tar

%description
The ebtables program is a filtering tool for a bridging firewall.
The filtering is focussed on the Link Layer Ethernet frame fields.
Apart from filtering, it also gives the ability to alter the
Ethernet MAC addresses and implement a brouter.

%prep
%setup

%build
make CFLAGS="%optflags" LIBDIR=/%_lib/ebtables

%install
%make_install install \
    DESTDIR=%buildroot \
    LIBDIR=/%_lib/ebtables \
    BINDIR=/sbin MANDIR=%_mandir
mv %buildroot/%_lib/ebtables/libebtc.so %buildroot/%_lib/libebtc.so.0.0.0

%post
%post_service ebtables

%preun
%preun_service ebtables

%files
%doc ChangeLog THANKS

%config %_sysconfdir/ethertypes
%config(noreplace) %_sysconfdir/sysconfig/ebtables

%_initdir/ebtables

/%_lib/libebtc.so.*
/%_lib/ebtables
 
/sbin/*

%_man8dir/*

%changelog
* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt1
- 2.0.10-2 released

* Tue Mar  9 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.9-alt1
- 2.0.9-2 released

* Sat Nov 15 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt1
- 2.0.8 released

* Fri Oct 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.0.6-alt2
- Added patch from Debian to make ebtables compile with gcc-4 (Debian bug
  #288975)
- Dropped unneeded ebtables-2.0.6-gcc34.patch

* Fri Aug 12 2005 Victor Forsyuk <force@altlinux.ru> 2.0.6-alt1
- Initial build.
