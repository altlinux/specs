# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 

Name: alterator-datetime
Version: 4.9.2
Release: alt1

Summary: alterator module for date/time setup
License: GPL
Group: System/Configuration/Other

Requires: %name-functions = %EVR
Requires: alterator >= 5.2-alt1 alterator-sh-functions >= 0.6-alt5
Requires: alterator-service-functions >= 2.0.0-alt1
Requires: alterator-l10n >= 2.9.117-alt1
Requires: ntp-server glibc-timezones
Conflicts: alterator-lookout < 2.7
Conflicts: alterator-standalone < 7.4
Conflicts: alterator-browser-qt < 2.9.93
Conflicts: alterator-fbi < 5.17-alt3
Conflicts: alterator-lookout < 1.6-alt3
Conflicts: alterator-dhcp < 0.4-alt1

Source: %name-%version.tar

BuildRequires(pre): alterator >= 5.0
BuildRequires: alterator-fbi

BuildRequires: guile-devel

%define _unpackaged_files_terminate_build 1
%define _altdata_dir %_datadir/alterator
%add_findreq_skiplist %_datadir/install2/postinstall.d/*

%description
alterator module for date/time setup

%package functions
Summary: Helper functions for %name
Group: System/Base

%description functions
Helper functions for %name.

%prep
%setup

%build
%make_build

%check
%make_build check

%install
%makeinstall

%files
%_bindir/dumpisotab
%_sysconfdir/alterator/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_alterator_backend3dir/*
%_alterator_libdir/ui/*
%_alterator_libdir/type/*
%_datadir/install2/postinstall.d/*

%files functions
%_bindir/alterator-datetime-functions

%changelog
* Fri Oct 04 2024 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- datetime-functions: Don't allow duplicated translated names.

* Fri Aug 16 2024 Anton Midyukov <antohami@altlinux.org> 4.9.1-alt1
- postinstall.d/20-datetime.sh: disable ntp service, if ntp status is
  not enabled

* Fri Apr 12 2024 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- all: Use link timezones.
- datetime-functions: Move list_zone() to obsoleted functions.

* Mon Dec 25 2023 Andrey Cherepanov <cas@altlinux.org> 4.8.3-alt1
- defaultzones: add Asia/Tashkent for Uzbek locale

* Sun Dec 10 2023 Anton Midyukov <antohami@altlinux.org> 4.8.2-alt1
- alterator-datetime-functions: add get_utc_cmdline function

* Sun Dec 10 2023 Anton Midyukov <antohami@altlinux.org> 4.8.1-alt3
- Separate subpackage alterator-datetime-functions

* Wed Oct 11 2023 Michael Shigorin <mike@altlinux.org> 4.8.1-alt2
- E2K: move to guile22 too
- minor spec cleanup (see also ALT#46206)

* Fri Oct 14 2022 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- datetime-functions,postinstall: Replace egrep with grep -E.

* Fri Oct 14 2022 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- datetime-functions: Group old country* functions together.
- timezone: Rename 'Ok' button to 'Apply' (closes: #25311).
- datetime-functions: Don't use word 'region' for lang code.
- datetime-functions: Sort timezone list by name (closes: #42992).
- all: Change timezone interface (closes: #37913).

* Wed Sep 14 2022 Mikhail Efremov <sem@altlinux.org> 4.7.2-alt1
- test: Don't check timezones count.

* Tue May 24 2022 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- rearrange installer popup dialog widgets

* Wed Dec 29 2021 Anton Midyukov <antohami@altlinux.org> 4.7.0-alt1
- Unified the clock service control code (thanks manowar@)
- Made /etc/sysconfig/clock optional
- postinstall.d/20-datetime.sh: do not copy /etc/sysconfig/clock
  to systems without this config

* Thu Jul 08 2021 Anton Midyukov <antohami@altlinux.org> 4.6.8-alt1
- revert 4.6.7-alt1

* Wed Jul 07 2021 Anton Midyukov <antohami@altlinux.org> 4.6.7-alt1
- not require /etc/rc.d/init.d/clock, /etc/init.d/clock (closes: 40389)

* Tue Mar 23 2021 Ivan Razzhivin <underwit@altlinux.org> 4.6.6-alt1
- fix use of the server list in the installer

* Fri Mar 05 2021 Ivan Razzhivin <underwit@altlinux.org> 4.6.5-alt1
- add the ability to set several servers

* Wed Feb 24 2021 Ivan Razzhivin <underwit@altlinux.org> 4.6.4-alt1
- remove dependency on grub-common

* Thu Feb 18 2021 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- don't hardcode installer popup dialog size

* Mon Oct 26 2020 Ivan Razzhivin <underwit@altlinux.org> 4.6.2-alt1
- fix regular expression (closes: 39050)

* Fri Oct 09 2020 Ivan Razzhivin <underwit@altlinux.org> 4.6.1-alt1
- fix clocksource (closes: 39050)

* Fri Sep 11 2020 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- fix requires (closes: 38921)

* Fri Sep 04 2020 Ivan Razzhivin <underwit@altlinux.org> 4.6.0-alt1
- add the ability to select the clock source

* Wed May 13 2020 Mikhail Efremov <sem@altlinux.org> 4.5.0-alt1
- Check that supported ntp service is installed (closes: #38168).
- datetime-functions: Add numeric TZ to list_zone() output
  (closes: #20505).
- datetime-functions: Declare variable.

* Fri Jan 17 2020 Mikhail Efremov <sem@altlinux.org> 4.4.0-alt1
- datetime-functions: Unquote timezone string (closes: #35355).
- test: Update check-timezone.sh for zone1970.tab file.
- datetime-functions: Use zone1970.tab file (closes: #37741).

* Thu Aug 22 2019 Paul Wolneykien <manowar@altlinux.org> 4.3.1-alt1
- Run tests when building.
- Fix/improve: Protect the installer UI from runtime errors on
  country change.
- Added unit-test to check the "timezone" type.
- Fixed (type timezone): allow [_-] symbols and more than one "/".

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 4.3.0-alt1
- installer: Fix ntp status detection.
- installer: Don't use control directly.
- installer: Fix NTP service status in the installed system.

* Wed Mar 06 2019 Ivan Razzhivin <underwit@altlinux.org> 4.2.3-alt2
- Avoid possible script failure.

* Wed Mar 06 2019 Ivan Razzhivin <underwit@altlinux.org> 4.2.3-alt1
- Add chrony support to the postinstall script (ALT #36213).

* Tue Feb 12 2019 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Show localized date and time in installer (ALT #35985).

* Fri Oct 05 2018 Michael Shigorin <mike@altlinux.org> 4.2.1-alt1
- Avoid touching nonexistent service.

* Fri Aug 17 2018 Paul Wolneykien <manowar@altlinux.org> 4.2-alt1
- Use strict data type for the "zone" parameter.

* Wed Jul 18 2018 Michael Shigorin <mike@altlinux.org> 4.1-alt2
- support e2kv4 through %e2k macro (grenka@).

* Wed Jul 18 2018 Paul Wolneykien <manowar@altlinux.org> 4.1-alt1
- Use hostname-or-ip field type for NTP pool address.

* Tue Jan 16 2018 Paul Wolneykien <manowar@altlinux.org> 4.0-alt2
- Adapt for the E2K arch build.

* Fri May 05 2017 Mikhail Efremov <sem@altlinux.org> 4.0-alt1
- Update spec for guile22.
- functions: Ensure that guessed timezone is valid.
- functions: Don't use TLS  if ca-certificates not installed.
- functions: Wait 2 sec for geoip server.
- installer: Guess timezone only once.
- system: Use init_timezone().
- functions: Use shell_config_get() in read_zone().
- Add init_timezone() and use it.
- functions: Add get_timezone* functions.
- functions: Use argument in read_zone()/write_zone().
- functions: Use tzupdate.

* Fri Dec 23 2016 Denis Medvedev <nbr@altlinux.org> 3.0-alt1
- chrony support

* Tue Apr 21 2015 Mikhail Efremov <sem@altlinux.org> 2.6-alt1
- installer: Always set UTC/LOCAL in the /etc/adjtime.
- postinstall: Copy /etc/adjtime from installer too.
- functions: Add set_adjtime_utc() and is_adjtime_utc().

* Fri Mar 22 2013 Mikhail Efremov <sem@altlinux.org> 2.5-alt1
- Use alterator-service-functions (closes: #28688).

* Thu Feb 28 2013 Mikhail Efremov <sem@altlinux.org> 2.4-alt1
- Read real timezone from config file (closes: #28610).
- Drop unused variables.
- Remove all dynamically added entries from ntpd configs.

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3-alt1
- hackaround service clock sync (closes #28168)

* Tue Aug 23 2011 Mikhail Efremov <sem@altlinux.org> 2.2-alt5
- installer: Try to load rtc module.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 2.2-alt4
- installer: Fix datetime output (closes: #25957).

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt3
- small aufs hackaround: remove /etc/localtime before overwriting

* Wed Aug 05 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt2
- backend: fix confict between manual time setup and ntp

* Mon Aug 03 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- use workflow 'none'

* Wed Jun 10 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt3
- datetime-system backend: add 'date string' parameter

* Mon Apr 06 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- support ntp in postinstall.d script too

* Mon Apr 06 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- support both ntp and openntpd

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- more timezone defaults

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- fix installer interface

* Thu Feb 05 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- system version: fix popup size

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- full replacement of alterator-tzone

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- add support of alterator-dhcp

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- add special version (datetime + timezone) for control center

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- use help and translations directly from alterator-l10n
- use new form API

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- use form library

* Fri Oct 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt4
- fix help file

* Thu Oct 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt3
- backend: alterator_api_version=1
- remove /std/functions and with-translation
- little ui improvements
- use "value" attribute for datedit and timeedit.

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- improve type error messages

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- replace constraints with types

* Fri Aug 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- update help (cas@)
- remove <h1> and <title>

* Fri Jun 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- html: use dateedit widget
- remove hardcoded design

* Fri Jun 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- html: use timeedit widget

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- rename effect-init to init-effect

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- fix requires
- invert disable logic in scm version

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- use effect-disable

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2.1
- hotfix

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- remove pot-file
- use module.mak
- preliminary support for 'disable' effect

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- remove html-messages.mak
- join to common translation database
- use write_string_param

* Mon Apr 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- fix obsoletes (#15245)

* Fri Apr 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- update help

* Thu Apr 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- replace alterator-openntpd

* Tue Mar 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- remove template-*

* Sat Jan 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update to new help system

* Thu Oct 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- fix preinstall script (was error exit code when ntpd is not installed on target system)

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- Add Ukrainian translation to desktop file

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- Add installer hooks

* Mon Sep 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- overwrite both servers and pools

* Wed Aug 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4.1
- hotfix: reset qt clock value after save

* Wed Aug 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- move utc checkbox to tzone module

* Tue Jul 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- a separate step in installer now

* Fri Jun 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- fix menu translation

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add desktop file
- use std woo-list/name+label function

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2.2
- another code from installer (ntp light)
- add ui
- add help

* Thu Jun 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2.1
- more translations

* Thu May 31 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt2
- Fix: move scripts to the subdirectory.

* Fri May 25 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial release
