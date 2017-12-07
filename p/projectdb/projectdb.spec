Name: projectdb
Version: 0.0.20171207
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: ProjectDb database data file
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: https://www.altlinux.org/Packaging_Automation/ProjectDb

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/projectdb
for dir in */; do
	type=`basename $dir`
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done

%files
/usr/share/projectdb

%changelog
* Thu Dec 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.20171207-alt1
- first release
