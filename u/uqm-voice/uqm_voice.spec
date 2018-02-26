%define rname uqm
%define what voice

Name: %rname-%what
Version: 0.6.0
Release: alt1

Group: Games/Adventure
Summary: %what data for %rname package
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch
Requires: %rname-bin >= %version

Source0: %rname-%version-%what.uqm

%description
This package contains %what data required for the %rname package.

Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.

%prep
%build
%install
mkdir -p %buildroot/%_gamesdatadir/%rname/content/packages
install -m 644 %SOURCE0 %buildroot/%_gamesdatadir/%rname/content/packages/%what.uqm


cat >>copyright << __EOF__
Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.
__EOF__

%files
%doc copyright
%_gamesdatadir/%rname/content/packages/%what.uqm

%changelog
* Mon Oct 15 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 0.6.0-alt1
- resurrected from orphaned
- new version: 0.6.0
- depends on uqm-bin rather than uqm-common

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt1
- new version

* Thu Nov 20 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt2
- fix description

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- initial spec
