%define _unpackaged_files_terminate_build 1

Name: withlock
Version: 0.5
Release: alt1
Summary: Locking wrapper script
Group: System/Servers
License: ASL 2.0
Url: https://github.com/poeml/withlock.git
Source: %name-%version.tar
BuildArch: noarch

%description
withlock is a locking wrapper script to make sure that some program
isn't run more than once. It is ideal to prevent periodic jobs spawned
by cron from stacking up.
The locks created are valid only while the wrapper is running, and
thus will never require additional cleanup, even after a reboot. This
makes the wrapper safe and easy to use, and much better than
implementing half-hearted locking within scripts.

%prep
%setup

%install
rm -rf %buildroot
install -d %buildroot%_bindir
install -d %buildroot%_mandir/man1
install -m 0755 withlock %buildroot%_bindir
install -m 0644 withlock.1 %buildroot%_man1dir

%files
%doc README.md
%_bindir/withlock
%_man1dir/withlock.1*

%changelog
* Wed Apr 6 2018 Alexandr Antonov <aas@altlinux.org> 0.5-alt1
- initial build for ALT
