%define orepo mageia
%define obranch cauldron
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.013
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-generic-default-altlinux-sisyphus
Requires: distrodb-static-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
for type in source binary noversion group-strict group-approx; do
	if [ -d $type ]; then
		install -m755 -d $destdir/$type
		install -m644 $type/* $destdir/$type/
	fi
done
ln -s %obranch %buildroot/usr/share/distromap/%orepo/default

%files
/usr/share/distromap/*

%changelog
* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- db update

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- db update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- db update

* Thu Nov 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- db update

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- db update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- db update

* Fri Jun 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- db update

* Mon Jun 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- db update

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- db update

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- db update

* Thu May 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- db update

* Mon May 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- db update

* Fri Apr 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- db update
