Name:     integrity-notifier
Version:  0.7.1
Release:  alt1

Summary:  Integrity event notifier
License:  GPLv2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/integrity-notifier.git

Packager: Denis Medvedev <nbr@altlinux.org>
BuildArch: noarch

Source:   %name-%version.tar

%description
Integrity violations happen when a user starts a damaged program.
This script notifies users and optionally administrators about that.

%prep
%setup

%build
%make_build

%install
%makeinstall_std bindir=%_bindir sbindir=%_sbindir sysconfdir=%_sysconfdir datadir=%_datadir unitdir=%_unitdir libdir=%_libdir prefix=%_prefix controldir=%_controldir mandir=%_mandir
mkdir -p -m 0755 %buildroot%_logdir/integrityd

%files
%doc README.en README
%_sbindir/*
%dir %_sysconfdir/integrity
%config(noreplace) %_sysconfdir/integrity/*
%config(noreplace) %_unitdir/integrity-notifier.service
%config(noreplace) %_unitdir/integrity-scanner.service
%dir %_logdir/integrityd
%_bindir/*
%config(noreplace) %_sysconfdir/xdg/autostart/*

%changelog
* Wed May 22 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.1-alt1
- Switch to multilog(8) for log rotation.

* Mon May 20 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt1
- Updated README.
- Fix: Don't send duplicate notifications for the same user if the
  user is on the 'also' list.
- Limit notifications by UID >= 500 by default.
- Place configuration in /etc/integrity/notify.conf.
- Fix: Filter out possible warning of 'id' command.

* Wed Oct 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.2-alt1
- Move the log config to /etc/integrity. Create the log dir on demand.

* Wed May 29 2019 Denis Medvedev <nbr@altlinux.org> 0.6.1-alt4
- build to c8.1

* Tue May 28 2019 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt3
- Fix: Require /bin/tai64n.

* Sat May 25 2019 Denis Medvedev <nbr@altlinux.org> 0.6.1-alt2
- READMEs updated.

* Mon Apr 29 2019 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Improve: Use the separate desktop message config file with title
  and message.
- Ignore comments in /etc/integrity/also.
- Fix: Line-buffered grep.
- Fix: Don't collapse on an unknown UID.
- Compare timestamps with the program start time (that's against possible
  dupes).

* Fri Apr 26 2019 Paul Wolneykien <manowar@altlinux.org> 0.6-alt1
- Added desktop notifier.
- Precise timestamps in the records.
- Reworked system notifier service.
- Separate scanner service.

* Fri Mar 15 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt2
- fixed service and real_notifier is a configurable thing now.

* Tue Mar 12 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
- Initial release.
