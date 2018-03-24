%define orepo suse
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.026
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
for type in source binary group-strict group-approx; do
    if [ -d $type ] && stat -t $type/* >/dev/null 2>&1 ; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
for type in binary source ; do
    for flag in flags/$type/* ; do
	if [ -d $flag ] && stat -t $flag/* >/dev/null 2>&1 ; then
	    install -m755 -d $destdir/$flag
	    install -m644 $flag/* $destdir/$flag/
	fi
    done
done
ln -s default %buildroot/usr/share/distromap/%orepo/tumbleweed
ln -s %orepo %buildroot/usr/share/distromap/open%orepo

%files
/usr/share/distromap/*

%changelog
* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- db update

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- db update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- db update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- db update

* Thu Nov 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- added packman
- db update

* Thu Oct 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- db update

* Mon Oct 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- db update

* Sun Jan 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
