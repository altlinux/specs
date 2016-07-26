Name: wmvolman
Version: 2.0.1
Release: alt2_6

Summary: Window Maker Volume Manager
License: GPLv2+
Group: Graphical desktop/Window Maker

Url: http://github.com/raorn/%{name}
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf-common automake-common glib2-devel libgio libgio-devel libudisks2-devel libudisks2-gir-devel libdockapp-devel libX11-devel
Source44: import.info

%description
wmVolMan is a small volume manager for Window Maker. For now
it only displays and allows mounting and unmounting removable
media and hotpluggable devices that are added to or removed
from the system.

%prep
%setup -q

%build
autoreconf -fisv
%configure
make %{?_smp_mflags}

%install
%{makeinstall_std}

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/wmvolman
%{_datadir}/wmvolman

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- Sisyphus build by request of mike@

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- initial fc import

* Mon Oct 04 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt1
- [1.0]
 + Rewritten from HAL to UDisks
 + New icons for BlueRay and HD DVD media

* Thu Jan 03 2008 Sir Raorn <raorn@altlinux.ru> 0.9-alt1
- [0.9]
 + Gracefully handle DBus and Hal restarts

* Sun Sep 16 2007 Sir Raorn <raorn@altlinux.ru> 0.8-alt1
- [0.8]
 + "Device busy" indicator
- License set to GPLv2

* Tue Aug 29 2006 Sir Raorn <raorn@altlinux.ru> 0.7-alt1
- [0.7]
 + Added README, described HAL properties and theming
 + Added CD-audio and "unknown" CD icons
 + Added support for memory cards (CF/MS/SD/MMC/SM)
 + Fixed and improved icon fallback

* Sat Jul 15 2006 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt2
- GIT snapshot v0.6.1-g8dbe9c2
 + Fixed dvd_plus_r/rw drive type detection
 + Added CF/MS/SD/MMC/SM cards icons

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- Fixed fdi location

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.6-alt1
- Built for Sisyphus

