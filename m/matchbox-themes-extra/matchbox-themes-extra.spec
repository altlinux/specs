Summary: 	Themes for the Matchbox Desktop
Name: 		matchbox-themes-extra
Version: 	0.3
Release: 	alt1_10
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-themes-extra/%version/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Source44: import.info

%description
Extra themes for the Matchbox Desktop

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc README TODO
%_iconsdir/*
%_datadir/themes/*




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_10
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_9
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_8
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_6
- update by mgaimport

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import

