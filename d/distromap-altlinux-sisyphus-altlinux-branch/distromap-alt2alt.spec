%define module altlinux-sisyphus-altlinux-branch

Name: distromap-%module
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/altlinux/sisyphus/altlinux/
for branch in p6 t6 p5 5.1;  do
	for type in binary group-strict;  do
		if [ -d $type/$branch ]; then
			install -m755 -d $destdir/$branch/$type
			install -m644 $type/$branch/* $destdir/$branch/$type/
		fi
	done
done

%files
/usr/share/distromap/*

%changelog
* Tue Nov 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added binary mappings for cronport

* Wed Oct 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed packaging

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
