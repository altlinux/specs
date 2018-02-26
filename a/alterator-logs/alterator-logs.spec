Name: alterator-logs
Version: 0.8
Release: alt4

Packager: Stanislav Ievlev <inger@altlinux.ru>

Summary: alterator module for system logs
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator >= 4.10-alt6
Requires: alterator-sh-functions >= 0.3-alt1
Requires: alterator-l10n >= 2.0-alt1

Conflicts: alterator-fbi < 5.20-alt3
Conflicts: alterator-lookout < 2.1-alt1

BuildPreReq: alterator >= 4.10-alt6

%description
System logs alterator module

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/*
%_sysconfdir/alterator/logs

%changelog
* Tue Feb 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt4
- use sh instead of buggy ash (it eats 0x81 from 0xD1 0x81)

* Tue Feb 16 2010 Mikhail Efremov <sem@altlinux.org> 0.8-alt3
- add alterator-net-iptables log definition.

* Sat Dec 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- don't print debug information

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- optimize log reading
- explicitly use ash
- improve design


* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6
- fix pagination (closes: #21709)

* Fri Sep 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt5
- add bacula log definition

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4
- remove log definition for ahttpd (closes: #19789)

* Wed Jul 29 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- add mail log definition (closes: #19788)

* Thu Jun 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- i18n fixes

* Tue Jun 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- UI:
  * improve first log selection
  * share callbacks between qt and html
- backend:
  * add ability to order logs
- default logs:
  * replace configd.log with alteratord.log

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- ui: ajax, new form library, show last log lines (closes: #17902)
- backend: alterator_api_version = 1

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- move html ui definitions from templates to ui directory
- use help and translations directly from alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt5
- rebuild with new l10n

* Mon Nov 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- build with new l10n (english help)

* Mon Nov 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- add ru help (by azol@)

* Fri Oct 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- use module.mak
- remove po files

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- replace alterator-read-desktop with alterator-dump-desktop

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- replace desktop.awk with alterator-read-desktop

* Thu May 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- html ui: add javascript
- add qt ui

* Wed May 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- improve skip

* Wed May 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- join to common translation database

* Wed May 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- view also rotated logs
- add ahttpd support

* Wed May 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- rewrite UI

* Sat Dec 01 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release
