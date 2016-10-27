Name: distrodb-utils
Version: 0.10
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: utils for managing Distrodb databases
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://altlinux.org/

BuildRequires: rpm-build-perl perl(DistroMap.pm)

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 distrodb-helper-* \
	distrodb-list-duplicates.pl \
	distrodb-verify-newpkglist.pl \
	distrodb-perl-health-checker.pl \
	mkdistromap-*.pl \
	pkglist2distrodb.py \
	%buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib
install -m 644 D*.pm %buildroot%perl_vendor_privlib/

%files
%doc README
%_bindir/*
%perl_vendor_privlib/D*

%changelog
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
