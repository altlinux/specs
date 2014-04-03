%define orepo cpan
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.01
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
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
#for type in group-strict group-approx;  do
#	install -m755 -d $destdir/$type
#	install -m644 $type/* $destdir/$type/
#done

#for type in binary source ; do
for type in source ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done


%files
/usr/share/distromap/*

%changelog
* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- db update
