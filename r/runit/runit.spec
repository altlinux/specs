
Name: runit
Version: 2.2.0
Release: alt1

Group: System/Configuration/Boot and Init
Summary: System-wide service supervision
Url: http://smarden.org/runit/
License: BSD-3-clause

Source0: %name-%version.tar
Source1: runit.service
Source2: sv.bash-completion
Source3: %name.watch
Source4: upstream-signing-key.asc

# Most of these patches are from the Debian package
Patch1: runit-2.1.2-service-dir-alt.patch
Patch4: 0004-src-Makefile-don-t-use-static-to-link-runit-runit-ini.diff
Patch6: 0006-make-buildsystem-respect-CFLAGS.patch
Patch7: 0007-move-communication-files.patch
Patch8: 0008-emulate-sysv-runlevel-5.patch

%description
runit is a collection of tools to provide system-wide service supervision
and to manage services.  Contrary to sysv init, it not only cares about
starting and stopping services, but also supervises the service daemons
while they are running.  Amongst other things, it provides a reliable
interface to send signals to service daemons without the need for pid-files,
and a log facility with automatic log file rotation and disk space limits.

runit service supervision can run under sysv init or replace the init
system completely.  Complete init replacement needs to be done by hand.

%prep
%setup
%autopatch -p2
rm -fv doc/debian

%build
package/compile

%check
package/check

%install

mkdir -p -m0755 %buildroot%_sysconfdir/runit/service

# Install the binaries and the corresponding manual pages
for cmd in `cat package/commands`; do \
	case "$cmd" in \
		runsvchdir|utmpset) \
			install -D -m0755 compile/$cmd %buildroot%_sbindir/$cmd; \
			;; \
		runit-init|runit) \
			install -D -m0755 compile/$cmd %buildroot/sbin/$cmd; \
			;; \
		*)
			install -D -m0755 compile/$cmd %buildroot%_bindir/$cmd; \
			;; \
	esac; \
	install -D -m0755 man/$cmd.8 %buildroot/%_man8dir/$cmd.8; \
done

# Install the main startup scripts
install -D -m0755 etc/2 %buildroot%_sysconfdir/runit/2

# Install the systemd unit file
install -D -m0644 %SOURCE1 %buildroot%_unitdir/runit.service

# Install the bash-completion file
install -D -m0644 %SOURCE2 %buildroot%_sysconfdir/bash_completion.d/sv

%files
%doc doc
%dir %_sysconfdir/runit
%dir %_sysconfdir/runit/service
%_bindir/*
%_sbindir/*
/sbin/*
%_man8dir/*.8.*
%_sysconfdir/runit/2
%_unitdir/*
%_sysconfdir/bash_completion.d/*


%changelog
* Mon Dec 09 2024 Paul Wolneykien <manowar@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0.

* Thu Oct 18 2018 Paul Wolneykien <manowar@altlinux.org> 2.1.2-alt2
- Fix: Do not install the Debian-specific startup scripts.

* Wed Oct 17 2018 Paul Wolneykien <manowar@altlinux.org> 2.1.2-alt1
- Initial build for ALT.
