Summary: Automatically logout users by idle timeouts
Name: timeoutd
Version: 1.5.1
Release: alt2
License: GPL
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>
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
%makeinstall_std
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

