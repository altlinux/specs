%define module jpackage-default-altlinux-sisyphus

Name: distromap-%module
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-fedora-rawhide-altlinux-sisyphus distromap-generic-default-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/jpackage/6.0/altlinux/sisyphus
for type in binary source noversion; do
    if [ -d $type ]; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
ln -s 6.0 %buildroot/usr/share/distromap/jpackage/default

%files
/usr/share/distromap/*

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- db updates

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- db updates

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- db updates

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- db updates

* Thu Jan 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Wed Jan 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added default branch

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
