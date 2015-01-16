%define _altdata_dir %_datadir/alterator

Name: alterator-snort
Version: 0.5.1
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for snort administration
Packager: Mikhail Efremov <sem@altlinux.org>
Source: %name-%version.tar

Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: alterator-service-functions
Requires: snort barnyard2-mysql snort-rules
Requires: oinkmaster wget
Requires: alterator-l10n >= 2.8-alt4
Requires: fail2ban >= 0.8.13

BuildPreReq: alterator >= 4.10-alt8
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for snort administration.

%prep
%setup -q

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot/%_sysconfdir/cron.d/
touch %buildroot/%_sysconfdir/cron.d/%name
touch %buildroot/%_sysconfdir/cron.d/%name-notifications
mkdir -p %buildroot/%_sysconfdir/sysconfig/
touch %buildroot/%_sysconfdir/sysconfig/%name
mkdir -p %buildroot/%_datadir/alterator-snort/
install -m644 tools/base_conf.php %buildroot/%_datadir/alterator-snort/

%files
%_altdata_dir/applications/*
%_altdata_dir/desktop-directories/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_libexecdir/%name/
%ghost %_sysconfdir/cron.d/%name
%ghost %_sysconfdir/cron.d/%name-notifications
%_sysconfdir/sysconfig/%name
%_datadir/alterator-snort
%_datadir/alterator-snort/base_conf.php

%changelog
* Fri Jan 16 2015 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Rename BASE page to 'Advanced statistics'.

* Mon Dec 22 2014 Andriy Stepanov <stanv@altlinux.ru> 0.5.0-alt1
- Fix actions on rules lists.
- Add status for snort & barnyard2 on each page
- Do correct start/reload and notify

* Thu Dec 18 2014 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Drop "Reset" button.
- reset-snort-db.sh: Use sysplog_alert barnyard2 plugin.
- base_conf.php: Fix font path.

* Wed Dec 17 2014 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Move /snort module to /snort/statistics.
- snort-email-notification.sh: Dont't try to ctreate table.
- Drop upper menu from module.
- Use separate desktop files for module components.

* Mon Dec 15 2014 Mikhail Efremov <sem@altlinux.org> 0.3.8-alt1
- Use https for BASE.

* Fri Dec 12 2014 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Only use UTC if it configured in the barnyard2.conf.
- Install snort-email-notification.sh script.

* Thu Dec 11 2014 Andriy Stepanov <stanv@altlinux.ru> 0.3.6-alt1
- Update test manual. Added 'complete reset' capability.

* Wed Dec 10 2014 Andriy Stepanov <stanv@altlinux.ru> 0.3.5-alt2
- Add test manual.

* Mon Oct 13 2014 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Ensure that fail2ban is enabled.

* Tue Aug 19 2014 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Add reference to BASE web interface.
- Changes for BASE-1.4.5-alt7.
- Don't expose password in the UI.

* Tue Jul 22 2014 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Use alterator-service-functions.
- reset-snort-db.sh: Fix password setup.

* Wed Jul 16 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt2
- Require snort.

* Mon Jun 30 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.2-alt1
- Grant UPDATE,DELETE for all database

* Fri Jun 27 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.1-alt2
- Add Req: fail2ban

* Wed Jun 25 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.1-alt1
- Mod reset-snort-db.sh

* Wed Jun 25 2014 Timur Aitov <timonbl4@altlinux.org> 0.3.0-alt1
- Add notifications page
- Add ban and banned page
- Add base page
- Add configuration page
- Mod rules page

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 0.2.5-alt1
- Fix download rules by oinkcode

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 0.2.4-alt2
- Remove Req: MySQL-server, MySQL-client

* Mon Feb 18 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.4-alt1
- Get password for mysql from barnyard config

* Fri Jan 25 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.3-alt3
- Add barnyard2-mysql requires (instead snort-mysql)

* Thu Dec 23 2010 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt2
- Add wget requires (for oinkmaster).

* Wed Dec 22 2010 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Use user 'snort' for access to mysql database.

* Fri Dec 11 2009 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- require alterator-l10n.
- change desktop entry category.

* Thu Nov 05 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- use timestamp in UTC.
- disable 'auto_update' checkbox if no url selected.

* Tue Nov 03 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- package cron file as ghost.

* Mon Nov 02 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- added 'Custom URL' field.
- use '-U' option for oinkmaster.
- added cron settings.

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- enable mysqld service when snort started.
- reset-snort-db.sh: added 'host=localhost' to output plugin
  configuration.

* Thu Oct 22 2009 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- UI improved.
- fix typo.
- reset-snort-db.sh: fix return code.

* Tue Oct 20 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- script reset-snort-db.sh is added.
- fix enabled/disabled state displaying.
- fix snortd restart.
- skip 'on' value in details list.

* Mon Oct 19 2009 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- initial release



