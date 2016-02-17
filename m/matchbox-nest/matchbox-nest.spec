# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libmb)
# END SourceDeps(oneline)
Requires: xorg-xnest
Summary: 	X nesting for the Matchbox Desktop
Name: 		matchbox-nest
Version: 	0.3
Release: 	alt2_10
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel 
BuildRequires:	libXtst-devel 
BuildRequires:	libexpat-devel
Source44: import.info
Patch33: matchbox-nest-0.3-alt-Xnest-path.patch

%description
X nesting for the panel from Matchbox.

%prep
%setup -q
%patch33 -p1

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/%name




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_10
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_9
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_8
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_7
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_6
- update by mgaimport

* Sun Nov 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_5
- bugfix release

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import

