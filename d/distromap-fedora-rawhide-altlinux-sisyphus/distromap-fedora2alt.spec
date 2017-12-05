%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.415
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
destdir=%buildroot/usr/share/distromap/fedora/rawhide/altlinux/sisyphus
for type in binary source group-strict group-approx; do
    if [ -d $type ] && stat -t $type/* >/dev/null 2>&1 ; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
ln -s rawhide %buildroot/usr/share/distromap/fedora/default
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
* Tue Dec 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.415-alt1
- db updates

* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.414-alt1
- db updates

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.413-alt1
- db updates

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.412-alt1
- db updates

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.411-alt1
- db updates

* Sat Sep 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.410-alt1
- db updates

* Thu Feb 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.409-alt1
- db updates

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.408-alt1
- db updates

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.407-alt1
- db updates

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.406-alt1
- db updates

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.405-alt1
- db updates

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.404-alt1
- db updates

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.403-alt1
- db updates

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.402-alt1
- db updates

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.401-alt1
- db updates

* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.400-alt1
- db updates (Jubilee)

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.399-alt1
- db updates

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.398-alt1
- db updates

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.397-alt1
- db updates

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.396-alt1
- db updates

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.395-alt1
- db cleanup

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.394-alt1
- db updates

* Mon May 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.393-alt1
- db updates

* Thu May 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.392-alt1
- db updates

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.391-alt1
- db updates
