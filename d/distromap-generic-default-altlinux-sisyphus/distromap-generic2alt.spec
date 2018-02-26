%define orepo generic
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.05
Release: alt4
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Provides: distromap-generic-generic-altlinux-sisyphus = %version-%release
Obsoletes: distromap-generic-generic-altlinux-sisyphus < 0.04

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
for type in group-strict group-approx;  do
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done
ln -s default %buildroot/usr/share/distromap/%orepo/generic

%files
/usr/share/distromap/*

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4
- more groups

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3
- more froups

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfix

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added groups

* Wed Jan 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added default branch; renamed to generic-default

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added groups

* Wed Oct 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed packaging

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
