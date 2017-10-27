%define collectorname description

Name: repocop-collector-%collectorname
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.40
BuildRequires: perl-DBI perl(RPM/Header.pm)

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/repocop/srccollectors/%collectorname/
install -m 755 %collectorname.test %buildroot%_datadir/repocop/srccollectors/%collectorname/test
install -m 644 %collectorname.options %buildroot%_datadir/repocop/srccollectors/%collectorname/options
sqlversion=`sed -n -e 's|^.*PRAGMA *user_version *= *\([0-9]*\).*$|\1|p' %collectorname.sql`
install -m 644 %collectorname.sql %buildroot%_datadir/repocop/srccollectors/%collectorname/init.sql.$sqlversion
#install -m 644 %collectorname.purge.sql %buildroot%_datadir/repocop/srccollectors/%collectorname/purge.sql


%files
#doc README ChangeLog
%_datadir/repocop/srccollectors/%collectorname

%changelog
* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
