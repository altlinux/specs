Name: distrodb-utils
Version: 0.20
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: utils for managing Distrodb databases
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://www.altlinux.org/Packaging_Automation/DistroMap

Requires: python-module-rpm

BuildRequires: rpm-build-perl perl(DistroMap.pm)
# for ProjectDB
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/RPM.pm)

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 projectdb-helper-* \
	distrodb-helper-* \
	distrodb-list-duplicates.pl \
	distrodb-verify-newpkglist.pl \
	distrodb-perl-health-checker.pl \
	mkdistromap-*.pl \
	*list2distrodb.py \
	%buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib
install -m 644 *.pm %buildroot%perl_vendor_privlib/

%files
%doc README
%_bindir/*
%perl_vendor_privlib/*.pm

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- new version

* Thu Dec 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- new version

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- new version

* Tue Dec 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- new version

* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- new version
- projectdb support

* Fri Dec 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new distrodb format

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- new version

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- support for rpm 4.0.4

* Thu Mar 30 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1
- Adapted to the new RPM (>= 4.13) Python API (ALT#32900),
  introduced in commit 5211039a20762b4a50c006ccf79666bff34967c2
  Author: jbj Date: Mon Aug 5 21:46:50 2002 +0000

* Thu Oct 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- new version

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new version

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- new version

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- generic source translation

* Thu Jun 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- pyegg db

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added management utils for manual maps

* Fri May 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added common lib

* Thu May 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first release
