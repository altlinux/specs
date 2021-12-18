Name: repocop-report-prometheus
Version: 0.40
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus1 format
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: http://repocop.altlinux.org

Requires: repocop > 0.80
Obsoletes: repocop-prometeus < 0.22
Obsoletes: repocop-report-prometeus < 0.31

BuildRequires: rpm-build-perl perl-devel perldoc
BuildRequires: repocop

Source: %name-%version.tar

%description
Repocop is a repository unit tests platform.
%summary

%package -n repocop-report-broken-metadata
Summary: repocop report script that finds broken metadata in rpm db
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Requires: repocop > 0.80

%description -n repocop-report-broken-metadata
Repocop is a repository unit tests platform.
%summary

%package -n repocop-report-packages.altlinux
Summary: repocop report script that dumps test results to packages.altlinux json format
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Requires: repocop > 0.80
BuildRequires: perl-JSON perl-JSON-XS

%description -n repocop-report-packages.altlinux
Repocop is a repository unit tests platform.
%summary

%package -n perl-Repocop-Report-Tools
Summary: shared library for repocop report scripts
Group: Development/Other
License: GPLv2+ or Artistic-2.0
#Requires: repocop > 0.80
BuildRequires: perl(IO/Compress/Bzip2.pm) perl(IO/Compress/Gzip.pm)

%description -n perl-Repocop-Report-Tools
Repocop is a repository unit tests platform.
This is shared library for some repocop-reports.

%prep
%setup
rm -f *.spec

%build

%install
mkdir -p %buildroot/%_bindir
# sisyphus.ru
# exclude repocop-report-prometheus-mysql
install -m 755 repocop-report-prometheus-dump %buildroot/%_bindir/
# new geiser
install -m 755 repocop-report-packages.altlinux %buildroot/%_bindir/
# tool
install -m 755 repocop-report-broken-metadata %buildroot/%_bindir/
# common lib
install -D -m 644 lib/Test/Repocop/Report/Tools.pm %buildroot%perl_vendor_privlib/Test/Repocop/Report/Tools.pm

%files
#doc README ChangeLog
%_bindir/repocop-report-prometheus-*
#%_man1dir/repocop-report-prometheus-*

%files -n repocop-report-packages.altlinux
%_bindir/repocop-report-packages.altlinux

%files -n repocop-report-broken-metadata
%_bindir/repocop-report-broken-metadata

%files -n perl-Repocop-Report-Tools
%perl_vendor_privlib/Test/Repocop/Report*

%changelog
* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.40-alt1
- repology import support

* Thu Dec 16 2021 Igor Vlasenko <viy@altlinux.org> 0.39-alt1
- prometheus2 engine is no more

* Thu Aug 26 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt1
- support for --out in prometheus-dump

* Thu Aug 19 2021 Igor Vlasenko <viy@altlinux.org> 0.37-alt1
- added repocop-report-packages.altlinux

* Thu Sep 17 2020 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- added repocop-report-broken-metadata

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- ported for repocop 0.81+

* Tue Jul 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- bugfix release 

* Tue Jul 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- adapted for repocop 0.77

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- support for TestDB

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- added Obsoletes

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- renamed to prometheus (closes: 28131)

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
