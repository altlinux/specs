%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.39
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
* Tue Dec 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- db updates

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- db updates

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- db updates

* Thu Jan 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- db updates

* Wed Oct 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- db updates

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- db updates

* Thu May 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- db updates

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- db updates

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- db updates

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- db updates

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- db updates

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- db updates

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- db updates

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- db updates
