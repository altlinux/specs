Name: mysqltuner
Version: 1.7.0
Release: alt3

Summary: High Performance MySQL Tuning Script
License: GPLv3+
Group: Databases

Url: https://github.com/major/MySQLTuner-perl
Source0: %name-%version.tar.gz

BuildArch: noarch

BuildRequires: perl-podlators

# Automatically added by buildreq on Wed Sep 10 2008 (-bi)
BuildRequires: perl-devel

%define basedir %_datadir/%name

%description
MySQLTuner is a MySQL high performance tuning script written in perl that will
provide you with a snapshot of a MySQL server's health. Based on the statistics
gathered, specific recommendations will be provided that will increase a MySQL
server's efficiency and performance. The script gives you automated MySQL tuning
that is on the level of what you would receive from a MySQL DBA.

%prep
%setup

%build

%install
install -pD -m755 %name.pl %buildroot%_bindir/%name
install -pD -m644 vulnerabilities.csv %buildroot%basedir/vulnerabilities.csv
install -p -m644 basic_passwords.txt %buildroot%basedir/
install -p -m644 LICENSE %buildroot%basedir/
pod2man %name.pl > %name.1
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%basedir/*
%_man1dir/*

%changelog
* Fri Feb 03 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt3
- Fixed man (use pod2man).

* Fri Feb 03 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt2
- Added MAN, LICENSE, vulnerabilities.csv and basic_passwords.txt

* Fri Feb 03 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Mar 14 2011 Victor Forsiuk <force@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Wed Sep 10 2008 Victor Forsyuk <force@altlinux.org> 0.9.9-alt1
- Initial build.
