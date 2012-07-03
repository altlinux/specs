%define collectorname java-pom

Name: repocop-collector-%collectorname
Version: 0.05
Release: alt2
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.08 perl-DBI perl-DBD-SQLite
Requires: perl-XML-Simple
BuildRequires: perl-DBI perl-XML-Simple

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/
install -m 755 %collectorname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/test
install -m 644 %collectorname.sql.1 $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/init.sql.1
install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern


%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfixes

* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- dropped unused columns in pom

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- support for maven3

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- support for multiple calls

* Mon Mar 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- improvements in collector

* Fri Mar 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
