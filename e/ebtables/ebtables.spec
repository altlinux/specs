Name: ebtables
Version: 2.0.11
Release: alt2

Summary: A filtering tool for a bridging firewall
License: GPLv2
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
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/sbin
ln -sfvr %buildroot%_sbindir/ebtables-legacy %buildroot/sbin/ebtables
ln -sfvr %buildroot%_sbindir/ebtables-legacy-save %buildroot/sbin/ebtables-save
ln -sfvr %buildroot%_sbindir/ebtables-legacy-restore %buildroot/sbin/ebtables-restore

%files
%doc ChangeLog THANKS
%config %_sysconfdir/ethertypes
/sbin/ebtables*
%_sbindir/*
%_libdir/libebtc.so.*
%_man8dir/*

%changelog
* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.11-alt2
- fix path to ebtables-legacy in ebtables-save (closes: 41051)

* Mon Sep 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.11-alt1
- 2.0.11 released

* Thu Nov 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt4
- properly link ebtables-restore (closes: #32792)

* Tue Sep 06 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt3
- updated from git 4c3e5cd3dbae

* Tue Dec 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt2
- 2.0.10-4 released

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
