Name: ovz-backup
Version: 0.02
Release: alt1

Summary: OpenVZ Container Backup - for containers using ploop storage

Group: Archiving/Backup
License: MPLv2.0
Url: https://github.com/AndSk/OVZ-Backup

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

%description
OVZ-Backup is a small python script that creates ploop snapshots of
OpenVZ containers and backs them up with rsync. It can either back up
all OpenVZ containers, or be given a list of container IDs that it
should either back up or exclude. All errors from OpenVZ or rsync are
logged with syslog. OVZ-Backup can also take a list of users or email
addresses that should be notified when errors occur.

%prep
%setup

%build

%install
install -pD -m0755 %name.py %buildroot%_bindir/%name.py

%files
%_bindir/%name.py
%doc README.md

%changelog
* Thu Nov 27 2014 Terechkov Evgenii <evg@altlinux.org> 0.02-alt1
- git-20141127

* Tue Nov 25 2014 Terechkov Evgenii <evg@altlinux.org> 0.01-alt1
- git-20141125
