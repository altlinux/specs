# $Id: separator.spec,v 1.26 2005/08/05 09:54:10 rider Exp $

Name: 	livecd
Version: 0.2.1
Release: alt1
Summary: Scripts for autoconfiguring livecd on startup
Summary(ru_RU.KOI8-R): Утилиты для автоматической настройки livecd при загрузке
License: GPL
Group: Development/Other
BuildArch: noarch
URL: http://www.altlinux.com/

Source: %name-%version.tar.bz2

%description
 Scripts for autoconfiguring livecd on startup

%prep
%setup -q

%build

%install
%makeinstall DESTDIR=%buildroot

%files
%dir %_sysconfdir/%name
%_sysconfdir/%name/*
%_sysconfdir/sysconfig/*
%_sysconfdir/rc.d/init.d/%name

%post 
%post_service %name
# hotplug must be enabled ;-(
/sbin/chkconfig --add %name

%preun
%preun_service %name

%changelog
* Tue Oct 11 2005 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- fixed English keyboard variant for ru,uk,be (for Guile support)

* Wed Aug 24 2005 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- added presets for tt_RU, uk_UA and be_BY locales

* Tue Aug 09 2005 Anton Farygin <rider@altlinux.ru> 0.1.0-alt1
- first build
