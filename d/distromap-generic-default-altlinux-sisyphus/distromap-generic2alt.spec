%define orepo generic
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.15
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Provides: distromap-generic-generic-altlinux-sisyphus = %version-%release
Obsoletes: distromap-generic-generic-altlinux-sisyphus < 0.04

Requires: distrodb-static-altlinux-sisyphus

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

#for type in binary source ; do
for type in binary  ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done


%files
/usr/share/distromap/*

%changelog
* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added suse groups

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- more groups

* Sun Oct 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- added group mappings for Hihin Ruslan's trinity build

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- tde basic support

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added requires on distrodb-static-altlinux-sisyphus

* Mon Jun 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- more groups from mageia

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- db update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- db update

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- db update

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added flags

* Wed Oct 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt6
- new groups

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt5
- more groups

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
