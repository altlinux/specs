%define orepo mageia
%define obranch cauldron
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.019
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
ln -s %obranch %buildroot/usr/share/distromap/%orepo/default
for type in binary source ; do
    for flag in flags/$type/* ; do
	if [ -d $flag ] && stat -t $flag/* >/dev/null 2>&1 ; then
	    install -m755 -d $destdir/$flag
	    install -m644 $flag/* $destdir/$flag/
	fi
    done
done

%files
/usr/share/distromap/*

%changelog
* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- db update

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- db update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- db update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- db update

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- db update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- db update

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- db update

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- db update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- db update

* Thu Nov 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- db update
