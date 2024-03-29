Name: projectdb
Version: 0.0.20220121
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: ProjectDb database data file
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Source: %name-%version.tar
Url: https://www.altlinux.org/Packaging_Automation/ProjectDb

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot%_datadir/projectdb
for dir in */; do
	type=`basename $dir`
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done

%files
%_datadir/projectdb

%changelog
* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 0.0.20220121-alt1
- db update

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.20190413-alt1
- db update

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.20190204-alt1
- db update

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20180621-alt1
- db update

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20180324-alt1
- db update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20180307-alt1
- db update

* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.20171227-alt1
- db update

* Thu Dec 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.20171207-alt1
- first release
