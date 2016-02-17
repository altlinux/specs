# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libmb)
# END SourceDeps(oneline)
%filter_from_requires /^.etc.matchbox.session/d
Summary: 	Shared files for the Matchbox Desktop
Name: 		matchbox-common
Version: 	0.9.1
Release: 	alt1_10
Url: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel
BuildArch:	noarch
Source44: import.info

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains graphics and scripts required by Matchbox.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc ChangeLog
%_bindir/matchbox-session
%_datadir/matchbox
%_datadir/pixmaps/*
%_iconsdir/blondie




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_10
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_9
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_8
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_7
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_6
- update by mgaimport

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_5
- mageia import

