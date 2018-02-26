Summary: timeoutd enforces the time restrictions specified for each or all users.
Name: timeoutd
Version: 1.5
Release: alt2.1
License: GPL
Group: System/Base
Packager: Boris Savelev <boris@altlinux.org>
Source: %name-%version.tar.bz2
Source1: %name.init
Patch: %name-%version-full.patch

# Automatically added by buildreq on Sat Mar 14 2009
BuildRequires: libX11-devel libXScrnSaver-devel libXext-devel

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
%patch0 -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_man5dir
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%_sysconfdir/%name/messages/
install -m755 %name %buildroot%_sbindir/%name
install -m755 %SOURCE1 %buildroot%_initdir/%name
install -m644 timeouts %buildroot%_sysconfdir/%name
install -m644 timeouts.5 %buildroot%_man5dir
install -m644 %name.8 %buildroot%_man8dir

%files
%doc README
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/messages
%config %_sysconfdir/%name/timeouts
%_sbindir/%name
%_initdir/%name
%_man5dir/*
%_man8dir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2.1
- Fixed build

* Mon Jun 01 2009 Boris Savelev <boris@altlinux.org> 1.5-alt2
- add 'status' for init-script

* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 1.5-alt1
- intial build

