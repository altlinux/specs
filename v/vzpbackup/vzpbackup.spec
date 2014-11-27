Name: vzpbackup
Version: 1.4
Release: alt1

Summary: OpenVZ Container Backup - for containers using ploop storage

Group: Archiving/Backup
License: GPLv3
Url: https://github.com/andreasfaerber/vzpbackup

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

%description
The scripts are meant to provide a backup solution to backup
containers that use ploop storage. Traditional storage is not
supported by the scripts. The scripts are based on the OpenVZ wiki
page regarding image backup: http://openvz.org/Ploop/Backup

%prep
%setup

%build

%install
install -pD -m0755 %name.sh %buildroot%_bindir/%name.sh
install -pD -m0755 vzprestore.sh %buildroot%_bindir/vzprestore.sh

%files
%_bindir/%name.sh
%_bindir/vzprestore.sh
%doc README.md ChangeLog.md TODO

%changelog
* Tue Nov 25 2014 Terechkov Evgenii <evg@altlinux.org> 1.4-alt1
- 1.4-6-gab839ce
