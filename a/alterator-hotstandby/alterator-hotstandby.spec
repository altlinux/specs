%define _altdata_dir %_datadir/alterator

Name: alterator-hotstandby
Version: 0.3.5
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for hot standby server
Packager: Mikhail Efremov <sem@altlinux.org>
Source: %name-%version.tar

Requires: alterator >= 4.12-alt1 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: heartbeat
Requires: csync2 >= 1.34-alt5
Requires: incron
Requires: hostinfo
Requires: alterator-net-functions >= 1.0-alt2
Requires: alterator-l10n >= 2.9-alt3

Conflicts: alterator-heartbeat

BuildPreReq: alterator >= 4.12-alt1
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for hot standby server

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_altdata_dir/type/*
%dir  %_sysconfdir/alterator/hotstandby
%config(noreplace) %_sysconfdir/alterator/hotstandby/*
%_localstatedir/%name/
%_libexecdir/%name/
%_sysconfdir/ha.d/resource.d/*

%changelog
* Fri Apr 16 2010 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- set DNS in dhcpd config.
- ahs_ifupdown_externals: fix exit on error.

* Thu Dec 17 2009 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- copy external ifaces configuration from main node to reserve node.
- fix is_enabled().

* Fri Dec 04 2009 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt2
- add alterator-l10n require.

* Fri Nov 06 2009 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- use csync2_period variable in ahs.cfg.
- compare deadtime and initdead.
- fix error message.
- fix double colon in field label.
- check intervals fields.
- ahs_csync2: fix ahs_csync2_periodic start.

* Fri Nov 06 2009 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- fix deadtimes defaults.

* Thu Nov 05 2009 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- ahs_csync2_periodic: avoid infinite 'at' spawn.

* Tue Nov 03 2009 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- remove 'Send configuration' button.
- added ahs_csync2_periodic script.
- UI: rename 'Resource' -> 'Service', 'Communication' ->
  'Administrative'.
- use openssl md5 for heartbeat key creation.
- fix desktop file.
- keepalive, initdead and deadtime parameters in UI.

* Fri Oct 02 2009 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- use '--urandom' csync2 option.
- Skip ifaces without configuration.
- fix typo in function name.
- fix possession directories.

* Wed Sep 30 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- call menu-reset-item on commit changes.
- use printf instead of echo -e.

* Fri Sep 25 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- remove unused variables.
- add more checks.
- backup/restore main node configs on reserve node.
- fix reserve node restart.
- Always display hostname of another node, not your own.

* Thu Sep 24 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- UI improved.
- config.list: fix configs paths.
- reset csync2 database when hot standby enabled.
- buckup/restore configs on reserve node.
- fix ahs_ifupdown_externals exit status if iface already up.
- make_incrontab(): allow '*' in the end of config path.
- show/hide alterator modules.
- fix heartbeat config path.
- Don't write duplicate strings in incrontab.

* Tue Sep 22 2009 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1
- incron requires is added.
- config.list: add more configs.
- services.list: incrond is added.
- make_incrontab implement.
- ahs_csync2: synchronize configs when started.
- read only first address on interface.
- added actions for csync2.
- up external ifaces when hotstandby switched to off.

* Fri Sep 18 2009 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- initial release

