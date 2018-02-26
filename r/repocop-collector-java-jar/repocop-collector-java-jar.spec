%define collectorname java-jar

Name: repocop-collector-%collectorname
Version: 0.05
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.08 perl-DBI perl-DBD-SQLite
Requires: fastjar
BuildRequires: perl-DBI

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/
%__install -m 755 %collectorname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/test
%__install -m 644 %collectorname.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/init.sql.0
%__install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern

%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- bugfix: correct disconnect

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- db check

* Sun Mar 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added Url and filepattern

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixes in sql

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
