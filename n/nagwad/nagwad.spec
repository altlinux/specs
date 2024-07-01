%define _unpackaged_files_terminate_build 1
%define icinga_user icinga

Name: 	  nagwad
Version:  0.11.4
Release:  alt3

Summary:  System journal event scanner and handler
License:  GPLv3
Group:    Monitoring
Url: 	  http://git.altlinux.org/people/manowar/packages/nagwad.git

Source:   %name-%version.tar

BuildRequires: discount libaudit-devel

%description
Daemon that continuously reads the system journal and generates events
based on journal messages. The example configuration contains
templates to pass the events further to Icinga and Nagios.

%package service
Summary: System journal event scanner and handler
Group:   Monitoring

BuildArch: noarch

Provides: %name = %version-%release
Obsoletes: %name <= 0.9.12-alt2

Requires: systemd
Requires: %name-audit = %version-%release

Conflicts: integ <= 0.4.2-alt2

%description service
Daemon that continuously reads the system journal and generates events
based on journal messages. The example configuration contains
templates to pass the events further to Icinga and Nagios.

%package nagios
Summary: Nagios templates for a nagwad node
Group:   Monitoring

Requires: %name-service = %version-%release
Requires: nagios-nrpe >= 3.2.1-alt4

Obsoletes: %name-server
Conflicts: %name-server
Conflicts: nagios < 3.0.6-alt9

Obsoletes: %name-templates
Provides: nagwad-nagios-templates = %version

BuildArch: noarch

%description nagios
These are Nagios configuration templates for monitoring a nagwad-node.

%package icinga
Summary: Icinga-2 configuration for a standalone nagwad node
Group:   Monitoring
BuildArch: noarch
Requires: %name-service
Requires: icinga2-common
Provides: nagwad-icinga-templates = %version

%description icinga
These are Icinga-2 configuration templates for monitoring using
nagwad on a standalone Icinga 2 node.

%package icinga-master
Summary: Icinga-2 master node configuration to monitor nagwad nodes
Group:   Monitoring
BuildArch: noarch
Requires: %name-service
Requires: icinga2-common
Provides: nagwad-icinga-templates = %version

%description icinga-master
These are Icinga-2 configuration templates for a master node to
be automatically distributed to Icinga 2 agents.

%package icinga-agent
Summary: Icinga-2 agent/satellite node configuration to monitor nagwad nodes
Group:   Monitoring
BuildArch: noarch
Requires: %name-service
Requires: icinga2-common
Provides: nagwad-icinga-templates = %version

%description icinga-agent
These are Icinga-2 configuration templates for a agent/satellite node.

%package icinga-push
Summary: An event post-processing script to push check results to an Icinga-2 inctance
Group:   Monitoring
BuildArch: noarch
Requires: %name-service = %version-%release

%description icinga-push
An event post-processing script to push check results to an Icinga-2
inctance (so-called passive checks). It can work without an Icinga2
agent installed on the node.

%package nagstamon
Summary: Nagstamon actions for a nagwad node
Group:   Monitoring
Requires: xvt openssh-clients
Requires: %name-service = %version-%release
Requires: nsca-shell = %version-%release

Obsoletes: %name-actions <= 0.9.14-alt1
Provides: %name-actions = %version-%release

BuildArch: noarch

%description nagstamon
These are Nagstamon action commands suitable for a nagwad-node.

%package audit
Summary: Audit rules for a nagwad node
Group:   Monitoring
Requires: audit mk-syscall-rules

BuildArch: noarch

%description audit
Contains audit rules for the 'audit' facility of %{name}.

%package -n mk-syscall-rules
Summary: A tool to generate audit rules based on a configuration file
License:  GPLv3
Group:   Monitoring
Requires: which

%description -n mk-syscall-rules
Contains 'mk-syscall-rules' and 'aunormarch' utils.

%package -n nsca-shell
Summary: A shell which sends session typescript to a Nagios server
Group:   Monitoring
BuildArch: noarch

%description -n nsca-shell
A tool to record a typescript of a terminal session
and then send it to a Nagios monitoring server in order to keep
a log of operations with a particular host or service.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std unitdir=%_unitdir
mkdir -p %buildroot/var/log/nagwad
# Touch the file for %%ghost below.
touch %buildroot%_sysconfdir/audit/rules.d/50-nagwad-arch.rules

%pre service
getent group %name >/dev/null || %_sbindir/groupadd -r %name

if [ -e %_sysconfdir/nagwad/audit/audit.regexp ]; then
    cp -nv %_sysconfdir/nagwad/audit/audit.regexp \
       %_sysconfdir/nagwad/eperm.regexp ||:
fi
if [ -e %_sysconfdir/nagwad/audit.regexp ]; then
    cp -nv %_sysconfdir/nagwad/audit.regexp \
       %_sysconfdir/nagwad/eperm.regexp ||:
fi
if [ -e %_sysconfdir/nagwad/audit-rules.conf ]; then
    cp -nv %_sysconfdir/nagwad/audit-rules.conf \
       %_sysconfdir/nagwad/eperm-audit-rules.conf ||:
fi
if [ -e %_sysconfdir/nagwad/authdata/authdata.regexp ]; then
    cp -nv %_sysconfdir/nagwad/authdata/authdata.regexp \
       %_sysconfdir/nagwad/authdata.regexp ||:
fi
if [ -e %_sysconfdir/nagwad/device/device.regexp ]; then
    cp -nv %_sysconfdir/nagwad/device/device.regexp \
       %_sysconfdir/nagwad/device.regexp ||:
fi
if [ -e %_sysconfdir/nagwad/login/login.regexp ]; then
    cp -nv %_sysconfdir/nagwad/login/login.regexp \
       %_sysconfdir/nagwad/login.regexp ||:
fi

%post audit
_mk_syscall_rules_relax=
if [ $1 = 1 -a -d /.host -a -d /.in -a -d /.out ]; then
    _mk_syscall_rules_relax=1
fi
%_sbindir/mk-syscall-rules -v \
    ${_mk_syscall_rules_relax:+--relax} \
    -c %_sysconfdir/nagwad/eperm-audit-rules.conf

%post icinga
usermod -a -G %name %icinga_user

%post icinga-master
usermod -a -G %name %icinga_user

%post icinga-agent
usermod -a -G %name %icinga_user

%files service
%doc README.md README.html signal.md signal.html
%_sbindir/nagwad
%_man8dir/nagwad.8.*
%_unitdir/nagwad.*
%_libexecdir/nagios/plugins/*
%dir %_sysconfdir/nagwad
%config(noreplace) %_sysconfdir/nagwad/nagwad.conf
%config(noreplace) %_sysconfdir/nagwad/*.regexp
%config(noreplace) %_sysconfdir/nagwad/*.sed
%dir %_sysconfdir/nagwad/filter-event.d
%config(noreplace) %_sysconfdir/nagwad/filter-event.d/[0-9]*
%dir %_sysconfdir/nagwad/filter-event.d/eperm-skip.d
%config(noreplace) %_sysconfdir/nagwad/filter-event.d/eperm-skip.d/*.regexp
/var/log/nagwad

%files audit
%config(noreplace) %_sysconfdir/audit/rules.d/*-nagwad*-noarch.rules
%ghost %_sysconfdir/audit/rules.d/50-nagwad-arch.rules
%config(noreplace) %_sysconfdir/nagwad/eperm-audit-rules.conf

%files nagios
%config(noreplace) %_sysconfdir/nagios/templates/*nagwad*.cfg
%config(noreplace) %_sysconfdir/nagios/nrpe-commands/nagwad.cfg

%files icinga
%doc conf/icinga/nagwad.json
%config(noreplace) %_sysconfdir/icinga2/conf.d/nagwad.conf

%files icinga-master
%doc conf/icinga/nagwad.json
%config(noreplace) %_sysconfdir/icinga2/conf.d/nagwad-master.conf
%config(noreplace) %_sysconfdir/icinga2/zones.d/global-commands/*.conf

%files icinga-agent
%config(noreplace) %_sysconfdir/icinga2/conf.d/nagwad-agent.conf

%files icinga-push
%_sysconfdir/nagwad/process-event.d/10-push-icinga
%config(noreplace) %_sysconfdir/nagwad/process-event.d/push-icinga.conf

%files nagstamon
%config(noreplace) %_sysconfdir/nagstamon/actions/*.conf

%files -n mk-syscall-rules
%_bindir/aunormarch
%_sbindir/mk-syscall-rules

%files -n nsca-shell
%_bindir/nsca-shell

%changelog
* Mon Jul 01 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.4-alt3
- Fixed URL autodetection in 10-push-icinga.
- Fix: Make "nagwad-host" append to host groups.

* Thu Jun 27 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.3-alt3
- PATH-based invocation of journalctl (/bin or /usr/bin).
- Add --test mode (reading messages from standard input).
- Make Nagios template packages provide "nagwad-nagios-templates"
  virtual package.
- Make Icinga template packages provide "nagwad-icinga-templates"
  virtual package.
- Prefix nagwad checks with "nagwad_" in Nagios/NRPE templates.

* Mon Jun 24 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.2-alt3
- Fix: Require "icinga2-common" and "nagwad-service" to install
  Icinga 2 templates: add "icinga" user to group "nagwad".
- Fixed nagwad-icinga2 package description.

* Mon Jun 24 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.2-alt2
- Fixed build with %%_unitdir.

* Mon Jun 24 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.2-alt1
- Fix: Skip journal messages from nagwad itself.
- Fixed "10-push-icinga": Don't use a system USERNAME by accident.
- Fixed "10-eperm" post-filter: Don't expect and require a skip pattern
  file.

* Fri Jun 21 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.1-alt1
- Fixed "d-nagwad-status" UUID.

* Mon Jun 17 2024 Paul Wolneykien <manowar@altlinux.org> 0.11.0-alt1
- Added icinga-agent package (also without "check_nagwad" command in main conf).
- Fix: Use 4-space indentation for code blocks in the docs.
- Fix the docs: full-format HTML files.
- Add more doc info about the `10-eperm` post-filter.
- Generate README.html too.
- Add manual page: nagwad(8).
- Update description in the spec.
- Added administration utility subcommands to list, view and mark
  the events as fixed.
- signal.md: Mention `icinga2-usersyncd` service and
  `icinga2-register-host` script.
- Added more docs on nagwad in Russian (signal.md and HTML).
- Updated README (FIXED events and configuration).
- Fix: Default log user is now root, not nagios.
- Spell-check README.
- Fix documented output format of a filer.
- Updating documentation (English).
- Added "nagwad-status" to conf/nagios.
- Added "nagwad-status" service to Icinga templates.
- Make nagwad lock its PID-file.
- Write and delete PID-file only when PIDFILE is defined.
- Make check_nagwad without arguments to check for nagwad service
  itself.
- Make check_nagwad ignore FIXED events.
- Rename Icinga Director template services using the scheme "d-nagwad-<filter>".
- Rename Icinga template services using the scheme "nagwad-<filter>".
- Write logs to /var/log/nagwad/<BOOT_ID>.
- Simplify and speedup check for already registered events by using
  MD5 naming.
- Added icinga-push package with the post-processing script pushing
  events via Icinga 2 REST API.
- Run postprocess scripts from $CONFDIR/process-event.d/ dir.
- Move postprocessing filters to filter-event.d/.
- Speed-up processing by using the united sed script file.
- Clean up old logs if MAXAGE is set and is not 0.
- Read /etc/nagwad/nagwad.conf if exists.
- Fix nagwad.json: Assign "d-nagwad-service-set" for all
  "d-nagwad-nodes".
- Added icinga-master package with global commands.
- Make check_nagwad to return the newest event.
- Make unpackaged files terminate build.

* Thu Feb 15 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.5-alt1
- Fix: Added missing 'd-nagwad-nodes' host group.

* Wed Feb 14 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.4-alt1
- Fixed integalert.regexp: React to messages of different integalert
  profiles.
- signal.md: Fixed reference to `icinga2-doc`.

* Wed Feb 07 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.3-alt1
- Updated signal.md: host template names and new packages for
  installation.
- signal.md: Added a note about agent configuration in Icinga
  Director.
- Fix: Automatically added 'icinga' user to the 'nagwad' group
  ('nagwad-icinga' now depends on 'icinga2' package).
- Fix Icinga Director basket: added Icinga Agent settings.

* Tue Feb 06 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.2-alt2
- Fixed project URL.

* Tue Feb 06 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.2-alt1
- Fixed template name in signal.md.
- Fixed Icinga nagwad templates: run checks with agent (on local
  or remote hosts).

* Tue Feb 06 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.1-alt1
- Save copies of events to /run/nagwad/events.
- New version of signal.md documentation (Russian).
- Minor fix of login.sed.
- Package Icinga Director basket as a doc.
- Added nagwad Icinga Director basket in JSON format.
- Improved description of host group "nagwad-nodes".
- Improved display name: "Printing policy violation attempt".
- Rename 'audit' filter (and all related files) to 'eperm'.
- Remove deprecated 'osec' check.
- Added "nagwad-host" host template for Icinga.
- Fix: Don't copy README and signal.* manual to the `-nagios` package.
- Updated README.
- Monitor integrity of file access audit rules.
- Fixed audit.regexp: Only SYSCALL messages.
- Updated audit.regexp: Added nagwad- prefix.
- Skip access errors to /proc/1/environ by default.
- Added 10-audit post-process filter which skips events for
  particular files listed in audit-skip.d.
- Allow post-filters to add text to messages.
- Match each event with previously registered events and ignore
  duplicates.
- Support event post-processing filters in /etc/nagwad/filter-event.d.
- Process the journal starting from the current boot.
- Process the message with no leading whitespace by default.
- check_nagwad: Don't print minor accidental errors.

* Mon Jan 15 2024 Paul Wolneykien <manowar@altlinux.org> 0.10.0-alt1
- Reflect the event status in the name of the signal file and check
  signal files in order of severity.
- Make the signal files accessible by the members of 'nagwad' group.
- Fixed %%pre: %%pre service.
- /usr/sbin/nagwad: Source /etc/sysconfig/nagwad.
- Make check_nagwad support status lines + the default status
  command-line argument.
- Make nagwad support sed filters.
- Removed the obsolete check_osec NRPE plugin.
- Update the login.regexp to also support the 'pam_faillock' module.
- Update check plugins to report detailed OK and CRITICAL statuses.
- Extracted nsca-shell into the separate package.
- Make 'nagwad-icinga' and 'nagwad-nagstamon' depend on
  'nagwad-service'.
- Make 'nagwad-nagios' depend on 'nagios-nrpe'.
- Fix: Make 'nagwad-service' not depend on 'osec-cronjob' and
  'nagios-nrpe'.
- Make nagwad.service to restart on failure.
- Make nagwad.service want auditd.service.
- Rename 'nagwad-templates' to 'nagwad-nagios' and move nrpe-commands
  configuration to that package.
- Added configuration file for Icinga-2 (package %name-icinga).
- Rename package 'nagwad-actions' to 'nagwad-nagstamon'.
- Make nagwad-service conflict with obsoleted package integ <=
  0.4.2-alt2.
- Added configuration files for integalert.

* Mon Dec 25 2023 Paul Wolneykien <manowar@altlinux.org> 0.9.14-alt1
- Fix: Use "usergroup-change" key in audit rules (to match the nagwad
  filter key).

* Tue Sep 07 2021 Paul Wolneykien <manowar@altlinux.org> 0.9.13-alt3
- mk-syscall-rules: Add --relax option to relax on undetected arch.
- Run mk-syscall-rules in relaxed mode when installing the package
  in Hasher.
- Extract mk-syscall-rules into the separate package.

* Mon Sep 06 2021 Paul Wolneykien <manowar@altlinux.org> 0.9.13-alt2
- %name-audit: Explicitly require 'which' that isn't detected
  automatically as a requirement.

* Mon Sep 06 2021 Paul Wolneykien <manowar@altlinux.org> 0.9.13-alt1
- Replace static rules with a tool to generate architecture-dependent
  rules. Run it after the package is installed.

* Wed Aug 18 2021 Paul Wolneykien <manowar@altlinux.org> 0.9.12-alt3
- Fixed *-actions subpackage dependencies.
- Provide different set of audit rules on different arches.
- Document connection method selection in Nagstamon.
- Fix: Set server_address=0.0.0.0 in nrpe.cfg.

* Thu Aug 27 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.12-alt2
- Fix: Copy the old configuration files instead of moving them.

* Mon Aug 24 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.12-alt1
- Fixed the 'device' NRPE command.
- Fix: Really add print.regexp.

* Wed Aug 19 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.11-alt1
- Fixed locale in nagwad messages.
- Filter out "add_rule" events from auditd related to user and
  group changes but react to update and remove.
- Fixed missing while..done loop in the main process.

* Fri Jul 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.10-alt1
- Fix: Remove parentheses from the audit service description.

* Fri Jul 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.9-alt1
- Added print.regexp filter for CUPS operations.

* Thu Jul 23 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.8-alt1
- Configure audit to look for exec / open attempts to restricted
  files.
- Restore the "check_audit" NRPE check from v0.8-alt4.

* Tue Jul 21 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.7-alt1
- Fix/improve: Explicitly check for the signal file directory.
- Use universal "check_nagwad" script for typical nagwad NRPE checks.
- Make the nagwad.sh a simple service (ranamed to /usr/sbin/nagwad).
- Handle /etc/nagwad/*.regexp files automatically.

* Thu May 28 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.6-alt2
- Fixed documentation (signal.md):
  -- replace '.cnf' with '.cfg' (thx vercha@);
  -- added "nagstamon" package to the server list (thx nbr@).

* Fri May 22 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.6-alt1
- Use root@$ADDRESS$ for the Lock_host action.
- Produce and install signal.html.
- Updated the README.
- Added signal.md (and html) --- the manual in Russian.

* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.5-alt1
- Fixed quotation in NSCA shell action.
- Fixed OSEC regular expression for Nagwad.

* Wed Apr 22 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.4-alt2
- Switch to cronjob until timerunit patch is accepted by the OSEC's
  maintainer.

* Mon Apr 13 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.4-alt1
- Verbose descriptions in template checks.

* Mon Mar 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.3-alt1
- Conflicts with nagios < 3.0.6-alt9.
- Fixed nsca-shell missing show_usage().
- Added hostgroup "nagwad-nodes" and bind nagwad checks to it.

* Wed Feb 12 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt1
- Fix/improve: Force SSH to allocate a PTY.
- Fix/improve the nsca-shell: pass shell arguments after --rcfile.
- Fix/improve: Make the login.regexp react to an auth error from
  any service.

* Wed Feb 12 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- Added Nagstamon actions (package '%name-actions').
- Install /etc/... files with %%config(noreplace).
- Fixed check_authdata checker.
- Obsolete nagwad-server.
- Fix: Rename NRPE script: check_devices.

* Fri Feb 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt1
- Define the nagwad NRPE commands in the separate
  /etc/nagios/nrpe-commands/nagwad.cfg (requires nagios-nrpe >=
  3.2.1-alt4).
- Switch to /etc/nagwad and /var/log/nagwad directories.
- Moved osec timerunit to the osec SRC RPM.
- Use auditd to watch for /etc/passwd and group changes.
- Sanitized and modernized nagwad scripts.
- Added the wrapper command 'nsca-shell' for sending shell
  typescript to the Nagios server using the NSCA interface.

* Wed Jan 22 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt4
- build for sisyphus

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.7
- changed the behavour of osec's pipe to leave a log in /var/log

* Thu Aug 08 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.6
- added example  nagwad.sh

* Tue Apr 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8-alt3.M80C.5
- Updated provides for osec.

* Mon Mar 18 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.4
- osec now by default read-only on base, if READABLE= global var not set.

* Fri Jan 19 2018 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.3
- reduce of default dir list to check for osec

* Wed May 17 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.2
- switch to systemd in logging in c8

* Wed May 17 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt3%ubt
- fix permissions for /var/lib/osec

* Mon Apr 24 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt2%ubt
- move provides/conflicts for osec-timerunit from description

* Fri Apr 14 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt1%ubt
- extracted osec-timerunit package

* Fri Mar 31 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt4%ubt
- fix for dependences

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt3%ubt
- Change license to GPLv3,  dependencies added

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt2%ubt
- added universal build tag

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt1
- added osec timer and service for starting osec without cron.
Instructions for start is in signal.odt

* Thu Mar 02 2017 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- More mature version that checks 3 additional signals.

* Mon Feb 27 2017 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
 Initial release

