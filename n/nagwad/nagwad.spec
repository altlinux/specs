Name: 	  nagwad
Version:  0.9.13
Release:  alt3

Summary:  Nagios watch daemon
License:  GPLv3
Group:    Monitoring
Url: 	  http://git.altlinux.org/people/nbr/packages/nagwad.git


Source:   %name-%version.tar

BuildRequires: discount libaudit-devel

%description
Daemon that listens to journald and generates alerts based on journal messages
Example configuration works with alterator-ports-access. It provides Nagios
alerts when unauthorized USB devices are inserted.

%package service
Summary: Nagios watch daemon
Group:   Monitoring

BuildArch: noarch

Provides: %name = %version-%release
Obsoletes: %name <= 0.9.12-alt2

Requires: systemd
Requires: osec-cronjob
Requires: nagios-nrpe >= 3.2.1-alt4
Requires: %name-audit = %version-%release

%description service
Daemon that listens to journald and generates alerts based on journal messages
Example configuration works with alterator-ports-access. It provides Nagios
alerts when unauthorized USB devices are inserted.

%package templates
Summary: Nagios templates for a nagwad node
Group:   Monitoring
Obsoletes: %name-server
Conflicts: %name-server
Conflicts: nagios < 3.0.6-alt9

BuildArch: noarch

%description templates
These are Nagios configuration templates for monitoring a nagwad-node.

%package actions
Summary: Nagstamon actions for a nagwad node
Group:   Monitoring
Requires: xvt openssh-clients

BuildArch: noarch

%description actions
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

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/var/log/nagwad
# Touch the file for %%ghost below.
touch %buildroot%_sysconfdir/audit/rules.d/50-nagwad-arch.rules

%pre
if [ -e %_sysconfdir/nagwad/audit/audit.regexp ]; then
    cp -nv %_sysconfdir/nagwad/audit/audit.regexp \
       %_sysconfdir/nagwad/audit.regexp ||:
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
if [ -e %_sysconfdir/nagwad/osec/osec.regexp ]; then
    cp -nv %_sysconfdir/nagwad/osec/osec.regexp \
       %_sysconfdir/nagwad/osec.regexp ||:
fi

%post audit
_mk_syscall_rules_relax=
if [ $1 = 1 -a -d /.host -a -d /.in -a -d /.out ]; then
    _mk_syscall_rules_relax=1
fi
%_sbindir/mk-syscall-rules -v \
                           ${_mk_syscall_rules_relax:+--relax} \
                           -c %_sysconfdir/nagwad/audit-rules.conf

%files service
%doc README.md signal.html signal.md
%_bindir/nsca-shell
%_sbindir/nagwad
%_unitdir/nagwad.*
%_libexecdir/nagios/plugins/*
%dir %_sysconfdir/nagwad
%config(noreplace) %_sysconfdir/nagwad/*.regexp
%config(noreplace) %_sysconfdir/nagios/nrpe-commands/nagwad.cfg
/var/log/nagwad

%files audit
%config(noreplace) %_sysconfdir/audit/rules.d/*-nagwad*-noarch.rules
%ghost %_sysconfdir/audit/rules.d/50-nagwad-arch.rules
%config(noreplace) %_sysconfdir/nagwad/audit-rules.conf

%files templates
%doc README.md signal.html signal.md
%config(noreplace) %_sysconfdir/nagios/templates/*nagwad*.cfg

%files actions
%config(noreplace) %_sysconfdir/nagstamon/actions/*.conf

%files -n mk-syscall-rules
%_bindir/aunormarch
%_sbindir/mk-syscall-rules

%changelog
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

