Name: repocop-report-prometeus
Version: 0.30
Release: alt2
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.15
#Requires: perl-JSON-XS
Obsoletes: repocop-prometeus < 0.22

BuildRequires: perl-devel perldoc 
#perl-JSON
BuildRequires: repocop

Source: %name-%version.tar

%description
Repocop is a repository unit tests platform.
%summary

%package -n repocop-report-prometeus2
Summary: repocop report script that dumps test results to prometeus2 format
Group: Development/Other
License: GPL or Artistic
Requires: repocop > 0.15
Obsoletes: repocop-report-heroku < 0.4

%description -n repocop-report-prometeus2
Repocop is a repository unit tests platform.
%summary

%prep
%setup
rm -f *.spec

%build

%install
mkdir -p %buildroot/%_bindir
install -m 755 repocop-report-prometeus* %buildroot/%_bindir/

%files
#doc README ChangeLog
%_bindir/repocop-report-prometeus-*
#%_man1dir/repocop-report-prometeus-*

%files -n repocop-report-prometeus2
%_bindir/repocop-report-prometeus2*

%changelog
* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- code cleanup; but still has old txt support for prometeus2.

* Fri Jul 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- added sqlite report

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- bugfix release (closes: 26741)

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- bugfix release

* Tue Dec 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added branch to sql

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added branch option

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2
- added repository option

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- new version

* Sun Nov 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2
- fix in repocop-report-prometeus2-patches

* Fri Nov 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- added repocop-report-prometeus2-patches

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- bugfixed format4 (prometeus2)

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- format4

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- renamed; now contains prometeus and prometeus2 reports

* Thu Sep 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- format3

* Wed Sep 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- format2

* Wed Sep 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- First build for Sisyphus.
