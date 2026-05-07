Summary: Automatically logout users by idle timeouts
Name: timeoutd
Version: 1.5.4
Release: alt1
License: GPL
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>
Url: https://github.com/wolneykien/timeoutd.git
Source: %name-%version.tar

BuildRequires: libX11-devel libXScrnSaver-devel libXext-devel libsystemd-devel

%description
timeoutd scans /var/run/utmp every minute and checks /etc/timeouts for an entry which matches a restricted user, based on:
 - The current day and time
 - The tty that the user is currently logged in on
 - The user's login ID
 - Any primary or secondary groups the user is in
timeoutd can restrict local users, X11-users and users via telnet/SSH for a maximum of their session, max. day, idle or no login at all.
timeoutd is also able to restrict users running X.

%prep
%setup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -DWITH_SYSTEMD"

%install
%makeinstall_std unitdir=%_unitdir
mkdir -p %buildroot%_sysconfdir/%name/messages

%files
%doc README
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/messages
%config(noreplace) %_sysconfdir/%name/timeouts
%_sbindir/%name
%_initdir/%name
%_man5dir/*
%_man8dir/*
%_unitdir/%name.*

%changelog
* Thu May 07 2026 Paul Wolneykien <manowar@altlinux.org> 1.5.4-alt1
- Version 1.5.4 (compilation fix release).

* Fri Nov 21 2025 Paul Wolneykien <manowar@altlinux.org> 1.5.3-alt1.1
- Rebuild to reflect fixes since the broken version v1.5-alt2.1
  (Fixes: OVE-20251121-0001).

* Thu Nov 14 2024 Paul Wolneykien <manowar@altlinux.org> 1.5.3-alt1
- Version: 1.5.3.
- Fixed build (string warnings and suggested parentheses).
- Fixed build with GCC 14 (localtime() function).

* Wed Aug 07 2024 Paul Wolneykien <manowar@altlinux.org> 1.5.2-alt2
- Fixed build: Pass unitdir to make.

* Thu Dec 22 2022 Paul Wolneykien <manowar@altlinux.org> 1.5.2-alt1
- Do not intercept SIGSEGV.
- Quit on SIGINT and SIGQUIT in foreground mode.

* Thu Dec 22 2022 Paul Wolneykien <manowar@altlinux.org> 1.5.1-alt2
- Fix: Use %config(noreplace) for timeouts.

* Wed Dec 21 2022 Paul Wolneykien <manowar@altlinux.org> 1.5.1-alt1
- Fix: Exit with 100 on SIGSEGV.
- Added the unit file.
- Updated the package summary.
- Fixed/improved handling of error cases.
- Fixed and enabled all debug/info messages.
- Build with libsystemd.
- Implemented systemd log levels for messages.
- Implemented command-line option processing.
- The localtime function takes a time_t* argument. (thx Steve Powers).

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2.1
- Fixed build

* Mon Jun 01 2009 Boris Savelev <boris@altlinux.org> 1.5-alt2
- add 'status' for init-script

* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 1.5-alt1
- intial build

