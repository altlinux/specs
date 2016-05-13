Name: distrodb-utils
Version: 0.02
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
	mkdistromap.pl \
	pkglist2distrodb.py \
	%buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib
install -m 644 D*.pm %buildroot%perl_vendor_privlib/

%files
%doc README
%_bindir/*
%perl_vendor_privlib/D*

%changelog
* Fri May 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added common lib

* Thu May 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first release
