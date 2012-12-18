%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.24
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
for type in binary source ; do
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done
ln -s rawhide %buildroot/usr/share/distromap/fedora/default
for type in binary source ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done

%files
/usr/share/distromap/*

%changelog
* Tue Dec 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- db updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- db updates

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- db updates

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- db updates

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- db updates

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- db updates

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- db updates

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- db updates

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
