%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.16
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-generic-default-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/fedora/rawhide/altlinux/sisyphus
for type in binary source noversion; do
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done
ln -s rawhide %buildroot/usr/share/distromap/fedora/default

%files
/usr/share/distromap/*

%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- db updates

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- db updates

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- db updates

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- db updates

* Wed Aug 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- db updates

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- db updates

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- db updates

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- db updates

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- db updates

* Thu Jan 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- bugfix release

* Wed Jan 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added default branch
