Name: menu-devel
Version: 0.2.0
Release: alt3

Group: Development/Other
Summary: Deprecated package
License: GPL
URL: http://www.altlinux.org
BuildArch: noarch

%description
Deprecated package

%prep
%install
mkdir -p %buildroot/%_bindir/

%files

%changelog
* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3
- dropped freedesktop2menu.pl:
  after NMU on solarwolf done, no live package is using it.

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2
- dropped macros; 
- freedesktop2menu.pl is still called - can't drop yet

* Mon Apr 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- deprecate freedesktop2menu.pl; it produce only empty files now

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- new version
- remove kde-specific
- fix replace icon extension

* Tue Mar 09 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- initial spec
