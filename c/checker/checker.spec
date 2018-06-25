Name:     checker
Version:  0.7
Release:  alt1

Summary:  checker for unsafe settings
License:  GPLv2
Group:    Other
Url:      http://git.altlinux.ru/people/nbr/packages/checker.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
This program provides timer units and script for checks for unsafe user and filem settings.

%prep
%setup

%install
mkdir -p %buildroot/usr/sbin
mkdir -p %buildroot/lib/systemd/system
install -Dm 0700 checker/checkunsafe.sh %buildroot/usr/sbin/
install -Dm 0600 checker/checker.timer %buildroot/lib/systemd/system/
install -Dm 0600 checker/checker.service %buildroot/lib/systemd/system/

%files
/usr/sbin/checkunsafe.sh
/lib/systemd/system/checker.timer
/lib/systemd/system/checker.service


%changelog
* Mon Jun 25 2018 Denis Medvedev <nbr@altlinux.org> 0.7-alt1
- fix bug with missing / in find

* Wed Dec 13 2017 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
Initial release
