Name: dahdi-mithraen
Version: 0.2
Release: alt1
Summary: Utilites for dahdi drivers
License: GPL
Group: System/Kernel and hardware

Url: http://sisyphus.ru/ru/srpm/Sisyphus/dahdi-mithraen

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Requires(pre): asterisk-user

Obsoletes: zaptel-seiros
Obsoletes: zaptel-mithraen

%description
%summary
%prep
%setup -q

%build
%make_build

%install
%makeinstall_std

%files
%attr(2711,root,_asterisk) %_sbindir/zt_exists
%attr(2711,root,_asterisk) %_sbindir/zt_testspeed
%attr(2711,root,_asterisk) %_sbindir/dahdi_exists
%attr(2711,root,_asterisk) %_sbindir/dahdi_testspeed

%changelog
* Fri Oct 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- remove old zaptel support

* Mon Sep 28 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- add Url tag

* Sun Sep 13 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

