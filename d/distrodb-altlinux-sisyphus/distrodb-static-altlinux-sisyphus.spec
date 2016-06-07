%define repo altlinux
%define branch sisyphus
%define module %repo-%branch

Name: distrodb-%module
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroDb database static part
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: https://www.altlinux.org/Packaging_Automation/DistroMap

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distrodb/%repo/%branch
for dir in data/*; do
	type=`basename $dir`
	install -m755 -d $destdir/$type
	install -m644 data/$type/* $destdir/$type/
done
ln -s %branch %buildroot/usr/share/distrodb/%repo/default

%files
/usr/share/distrodb/*

%changelog
* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- db update
