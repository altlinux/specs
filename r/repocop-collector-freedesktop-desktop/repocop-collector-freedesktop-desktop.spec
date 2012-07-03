%define collectorname freedesktop-desktop

Name: repocop-collector-%collectorname
Version: 0.12
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop >= 0.40 perl-DBI perl-DBD-SQLite
Requires: desktop-file-utils >= 0.18
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
%__install -m 644 %collectorname.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/init.sql.2
%__install -m 644 %collectorname.purge.sql $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/purge.sql
%__install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern

%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- handling of lost thumbnailers

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- excluded repocop-demo-menu-*

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added kde3/4 locations

* Sun Oct 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- bugfix release

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added filepattern

* Thu May 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added chomp for filename.

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- desktop-file-validate >= 0.15

* Mon Jul 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- clean up of desktop-file-validate messages
- added /usr/share/apps to the list of collected dirs.

* Sat Jul 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added raw file content column

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added exernal verification using desktop-file-validate

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added directories.

* Tue Jul 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
