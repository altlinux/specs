Name: mysqltuner
Version: 2.9.2
Release: alt2

Summary: High Performance MySQL Tuning Script
License: GPLv3+
Group: Databases

Url: https://github.com/major/MySQLTuner-perl
Source0: %name-%version.tar

BuildArch: noarch

Requires: perl(JSON.pm)

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
sed -i '1s|^#!/usr/bin/env perl|#!/usr/bin/perl|' %buildroot%_bindir/%name
install -pD -m644 vulnerabilities.csv %buildroot%basedir/vulnerabilities.csv
install -pD -m644 basic_passwords.txt %buildroot%basedir/basic_passwords.txt
pod2man --name=%name --section=1 %name.pl > %name.1
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%check
perl -c %name.pl

%files
%_bindir/%name
%basedir
%_man1dir/%name.1.*
%doc LICENSE *.md *.png

%changelog
* Sat Sep 12 2026 Anton Farygin <rider@altlinux.org> 2.9.2-alt2
- Added Requires: perl-JSON so --json/--prettyjson work (closes: #60507)
- Disabled --checkversion/--updateversion for packaged install (closes: #60509)
- Named mountpoint (not usage percent) in disk-space recommendation
- Skipped virtual filesystems by mount prefix only
- Detected hypervisor flag when it was last on the CPU flags line
- Kept --noprocess enabled instead of clearing it
- Honoured --noprocess when measuring other process memory
- Treated query_cache_type 0/OFF as disabled and ON as all requests
- Packaged LICENSE, installed with /usr/bin/perl shebang

* Sun Sep 06 2026 Anton Farygin <rider@altlinux.org> 2.9.2-alt1
- 1.7.2 -> 2.9.2

* Tue May 23 2017 Terechkov Evgenii <evg@altlinux.org> 1.7.2-alt1
- 1.7.2 (build from upstream git repo)

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
