%define collectorname altlinux-alternatives

Name: repocop-collector-%collectorname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.40 perl-DBI perl-DBD-SQLite
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
%__install -m 644 %collectorname.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/init.sql.5
%__install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern

%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Mon Mar 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added Url and filepattern

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added master/slave flag.

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- fixed duplication in xml alternatives

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- fixed handling of the master in xml alternatives

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fixed incorrect handling of xml alternatives

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed filenames

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
