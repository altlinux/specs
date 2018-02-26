
%define rname uqm
%define what content
Name: %rname-%what
Version: 0.6.0
Release: alt1

Group: Games/Adventure
Summary: Game data for %rname package
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch

Obsoletes: %rname-game
Requires: %rname-common

Source0: %rname-%version-%what.uqm

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

%description
This package contains %what data required for the %rname package.

Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.

%prep
%setup -c -T

%install
mkdir -p %buildroot/%_gamesdatadir/%rname/content/packages
install -m0644 %SOURCE0 %buildroot/%_gamesdatadir/%rname/content/packages/%what.uqm

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
* Thu Apr 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt1
- new version

* Thu Nov 20 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt2
- fix description

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- initial spec
